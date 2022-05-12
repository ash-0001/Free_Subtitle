import pandas as pd
import numpy as np

def answer_one():
    energy = pd.ExcelFile(r"C:\Users\ash\Downloads\Energy Indicators.xls")
# print(dir(energy))
    energy = energy[16:243]
    energy = energy.drop(energy.columns[[0, 1]], axis=1)
    energy.rename(columns={'Environmental Indicators: Energy': 'Country','Unnamed: 3':'Energy Supply','Unnamed: 4':'Energy Supply per Capita','Unnamed: 5':'% Renewable'}, inplace=True)
    energy.replace('...', np.nan,inplace = True)
    energy['Energy Supply'] *= 1000000
    def remove_digit(data):
        newData = ''.join([i for i in data if not i.isdigit()])
        i = newData.find('(')
        if i>-1: newData = newData[:i]
        return newData.strip()
    energy['Country'] = energy['Country'].apply(remove_digit)
    di = {"Republic of Korea": "South Korea",
    "United States of America": "United States",
    "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
    "China, Hong Kong Special Administrative Region": "Hong Kong"}
    energy.replace({"Country": di},inplace = True)
    
    ###################################################################################
    GDP = pd.read_csv('world_bank.csv', skiprows=4)
    GDP.replace({"Korea, Rep.": "South Korea", 
                "Iran, Islamic Rep.": "Iran",
                "Hong Kong SAR, China": "Hong Kong"}, inplace=True)
    GDP.rename(columns={'Country Name': 'Country'}, inplace=True)
    ScimEn = pd.read_excel('scimagojr-3.xlsx')

    df = pd.merge(pd.merge(energy, GDP, on='Country'), ScimEn, on='Country')
    df.set_index('Country',inplace=True)
    df = df[['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations', 'Citations per document', 'H index', 'Energy Supply', 'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
    df = (df.loc[df['Rank'].isin([i for i in range(1, 16)])])
    df.sort('Rank',inplace=True)
    return df

answer_one()
