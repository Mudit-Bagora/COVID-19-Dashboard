from django.shortcuts import render
from datetime import datetime
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

    # total people tested
    tests = pd.read_csv('template/dataset/StatewiseTestingDetails.csv')
    df2 = tests.groupby(["Date"]).sum().max()
    tested = df2['TotalSamples']

    # get map data
    statesplot = [element.lower() for element in statesplot]
    datamap = merge(statesplot,values)
    showIndia = True

    # daily confirmed patients
    dataDatewise = data_india.groupby(["Date"]).sum()
    dataDatewise = dataDatewise['Confirmed']
    dataDatewise = dataDatewise.sort_values(ascending=True)
    dataDatewise = dataDatewise.tolist()

    # dates
    data_india['State/UnionTerritory'] = [element.lower() for element in data_india['State/UnionTerritory']]
    statename = 'kerala'
    data = data_india[data_india['State/UnionTerritory'] == statename]
    date = data['Date']
    date = date.tolist()
    # last updated data
    last_date = date[-1]

    context={
        'totalCount': totalCount,
        'statesplot':statesplot,
        'values':values,
        'Cured':Cured,
        'Active':Active,
        'Death':Death,
        'last_date':last_date,
        'tested':tested,
        'datamap':datamap,
        'showIndia':showIndia,
        'date':date,
        'dataDatewise':dataDatewise
        }
    return render(request,'index.html',context)

def selectStateData(request):
    merged_list = [[list1[i], list2[i]] for i in range(0, len(list1))] 
    return merged_list


def viewStatedata(request):
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

    # total people tested
    tests = pd.read_csv('template/dataset/StatewiseTestingDetails.csv')
    df2 = tests.groupby(["Date"]).sum().max()
    tested = df2['TotalSamples']

    # get map data
    statesplot = [element.lower() for element in statesplot]
    datamap = merge(statesplot,values)
    showIndia = False
    

    # get state wise data
    data_india['State/UnionTerritory'] = [element.lower() for element in data_india['State/UnionTerritory']]
    statename = request.POST.get('state')
    dataState = data_india[data_india['State/UnionTerritory'] == statename]
    dateState = dataState['Date']
    dateState = dateState.tolist()
    confirmedState = dataState['Confirmed']
    recoveredState = dataState['Cured']
    deathState = dataState['Deaths']
    activeState = dataState['Confirmed'] - dataState['Cured']
    # total cases right now
    totalState = confirmedState.tail(1)
    totalState = totalState.values[0]

    # last updated data
    last_date = dateState[-1]

    # total active right now
    totalActiveState = activeState.tail(1)
    totalActiveState = totalActiveState.values[0]

    # total cured right now
    totalCuredState = recoveredState.tail(1)
    totalCuredState = totalCuredState.values[0]
    
    # total death right now
    totaldeathState = deathState.tail(1)
    totaldeathState = totaldeathState.values[0]
    

    confirmedState = confirmedState.tolist()
    activeState = activeState.tolist()
    recoveredState = recoveredState.tolist()
    deathState = deathState.tolist()
    

    context={
        'totalCount': totalCount,
        'statesplot':statesplot,
        'values':values,
        'Cured':Cured,
        'Active':Active,
        'Death':Death,
        'last_date':last_date,
        'tested':tested,
        'datamap':datamap,
        'statename':statename,
        'showIndia':showIndia,
        'confirmedState':confirmedState,
        'dateState':dateState,
        'activeState':activeState,
        'recoveredState':recoveredState,
        'deathState':deathState,
        'totalState':totalState,
        'totalActiveState':totalActiveState,
        'totalCuredState':totalCuredState,
        'totaldeathState':totaldeathState
        }
    return render(request,'index.html',context)
