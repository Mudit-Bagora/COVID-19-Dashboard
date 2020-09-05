from django.shortcuts import render
import pandas as pd


# Create your views here.

def merge(list1, list2): 
      
    merged_list = [[list1[i], list2[i]] for i in range(0, len(list1))] 
    return merged_list


def indexPage(request):
    data_india = pd.read_csv('template/dataset/covid_19_india.csv')
     #find total +ve cases
    df1 = data_india.groupby(["Date"]).sum()
    df1.head()
    totalCount = df1['Confirmed'].max()
    Cured = df1['Cured'].max()
    Active = totalCount - Cured
    Death =  df1['Deaths'].max()

    # find +ve cases statewise
    df1 = data_india.groupby(["State/UnionTerritory"]).max()
    df1.head()
    plot = df1['Confirmed'].sort_values(ascending=False)
    plot.columns=['State/UnionTerritory','Values']
    statesplot = plot.index.tolist()
    values = plot.values.tolist()

    # last updated data
    last_date = data_india["Date"].max()
    # total people tested
    tests = pd.read_csv('E:/Projects/Short Project/COVID-19 Dashboard/secondDashboard/template/dataset/StatewiseTestingDetails.csv')
    df2 = tests.groupby(["Date"]).sum().max()
    tested = df2['TotalSamples']

    # get map data
    statesplot = [element.lower() for element in statesplot]
    datamap = merge(statesplot,values)


    context={
        'totalCount': totalCount,
        'statesplot':statesplot,
        'values':values,
        'Cured':Cured,
        'Active':Active,
        'Death':Death,
        'last_date':last_date,
        'tested':tested,
        'datamap':datamap
        }
    return render(request,'index.html',context)
