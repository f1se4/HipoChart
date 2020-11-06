# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:35:38 2020

@author: f1se4
"""
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rcParams

def f_label(val, lab):
    return lab + " {:.1f}%".format(val)


def f_make_hipo_chart(df):
    a = 1 - float(df['Average'][0]) / 100
    b = 1 - float(df.iloc[0][0]) / 100
    c = 1 - float(df.iloc[0][1]) / 100 
    
    rcParams['figure.facecolor'] = df['BackgroundColor'][0]
    rcParams['text.color'] = df['LabelColor'][0]
    
    plt.figure(figsize=(9,7),dpi=300)
    
    # Average
    wedges, labels =plt.pie([50,50], 
                            radius=1-a, 
                            labels=[f_label(float(df['Average'][0]),'Average'),''],
                            colors=[df['Average'][1]])
    wedges[1].set_visible(False)
    
    # Categories
    if b > c:
        wedges2, labels2=plt.pie([50,50], 
                                 radius=1-c, 
                                 labels=['',f_label(float(df.iloc[0][1]),df.columns[1])],
                                 colors=[df.iloc[1][0]])
        wedges2[0].set_visible(False)
        for t in labels2:
            t.set_horizontalalignment('left')
        wedges3, labels3 = plt.pie([50,50], 
                                 radius=1-b, 
                                 labels=['',f_label(float(df.iloc[0][0]),df.columns[0])],
                                 colors=[df.iloc[1][1]])
        wedges3[0].set_visible(False)
        for t in labels3:
            t.set_horizontalalignment('right')    
    else:
        wedges2, labels2 =plt.pie([50,50], 
                                 radius=1-b, 
                                 labels=['',f_label(float(df.iloc[0][0]),df.columns[0])],
                                 colors=[df.iloc[1][1]])
        wedges2[0].set_visible(False)
        for t in labels2:
            t.set_horizontalalignment('left')    
        wedges3, labels3 = plt.pie([50,50], 
                                 radius=1-c, 
                                 labels=['',f_label(float(df.iloc[0][1]),df.columns[1])],
                                 colors=[df.iloc[1][0]])
        wedges3[0].set_visible(False)
        for t in labels3:
            t.set_horizontalalignment('right')     
    
    #Save fig
    plt.savefig("./static/hipograf.svg",format='svg')
    
def f_make_dataframe(nameA,
                    nameB,
                    valueA,
                    valueB,
                    colorA,
                    colorB,
                    average,
                    averagecolor,
                    backgroundcolor,
                    textcolor):
    df = pd.DataFrame()
    df[nameA] = [valueA,colorA]
    df[nameB] = [valueB,colorB]
    df['Average'] = [average,averagecolor]
    df['BackgroundColor'] = [backgroundcolor,'null']
    df['LabelColor'] = [textcolor,'null']
    return df

def f_validaciones(valueA,
                    valueB,
                    colorA,
                    colorB,
                    average,
                    averagecolor):
    if valueA == '':
        return 'All fields must be informed'
    elif valueB == '':
        return 'All fields must be informed'
    elif colorA == '':
        return 'All fields must be informed'
    elif colorB == '':
        return 'All fields must be informed'
    elif average == '':
        return 'All fields must be informed'
    elif averagecolor == '':
        return 'All fields must be informed'
    else:
        return 'ok'

def main():
    df = pd.read_excel("ChartFile.xlsx")
    f_make_hipo_chart(df)
        
    
if __name__ == "__main__":
    main()

