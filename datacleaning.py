import pandas as pd
import numpy as np
import os, sys
import matplotlib.pyplot as plt

def totalUpRows(states, years):
    total_rows = 0
    for year in years:
        for state in states:
            csv_file = state + "_nat_" + year + ".csv"
            csv_name = state + "_" + year
            csv_name = pd.read_csv(csv_file)
            total_rows += csv_name.shape[0]
        print(("total of rows = "))
        return total_rows

def merge(states, years):
    merged = []
    for year in years:
        for state in states:
            csv_file = state + "_nat_" + year + ".csv"
            csv_name = state + "_" + year
            csv_name = pd.read_csv(csv_file)
            csv_name['state'] = state
            merged.append(csv_name)

    result = pd.concat(merged)
    result.to_csv("merged.csv")

states = ['nc', 'ny', 'oh', 'tx', 'wi']
years = ['1933', '1939']

totalUpRows(states, years)

mergedData = pd.read_csv("merger.csv")

def assetLoanRatio(mergedData):
    mergedData = mergedData.assign(loanratio=(mergedData["loans"] / mergedData["assets"]))
    mergedData.to_csv('merger.csv')

assetLoanRatio(mergedData)
mergedData = pd.read_csv('merger.csv')

def bottom10(mergedData):
    mergedData = mergedData[["name", "city", "state", "loanratio"]]
    mergedData = mergedData.sort_values(loanratio)
    print ("Bottom 10 banks for loan-ratio")
    print (mergedData[:10])

bottom10(mergedData)

def top10Graph(mergedData):
    mergedData = mergedData[["id", "loanratio"]]
    mergedData = mergedData.sort_values("loanratio")
    mergedData = mergedData [-10:]
    print (mergedData)

    plt.figure()
    mergedData["loanratio"].plot(kind="bar")
    plt.xlabel("Bank ID")
    plt.ylabel("Loan-Asset Ratio")
    plt.title("Top 10 Banks for Loan-Asset Ratio")
    plt.show()

def top10(mergedData):
    mergedData = mergedData[["name", "city", "state", "loanratio"]]
    mergedData = mergedData.sort_values("loanratio")
    print ("Top 10 Banks for loan-ratios:")
    print (mergedData[-10:])

top10(mergedData)
top10Graph(mergedData)
