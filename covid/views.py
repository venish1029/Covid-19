from django.shortcuts import render,HttpResponse
import requests
import json
# Create your views here.
def index(request):
    re=requests.get('https://corona.azure-api.net/summary')
    data=json.loads(re.text)
    list_country=[]
    for i in data['countries']:
        list_country.append((i['Country_Region'],i['Code'].lower(),i['Confirmed'],i['Deaths'],i['Active']))
    list_len=len(list_country)
    global_data=data['globalData']
    string_confirm=''
    for i in data['countries']:
        string_confirm=string_confirm+"  "+i['Country_Region']+"  "+str(i['Confirmed'])
    string_death=''
    for i in data['countries']:
        string_death=string_death+"  "+i['Country_Region']+"  "+str(i['Deaths'])
    
    return render(request,'index.html',{'global_data':global_data,'list_len':list_len,'list_country':list_country,'string_confirm':string_confirm,'string_death':string_death})


def state(request,state_name):
    str1 = "https://corona.azure-api.net//country//{}".format(state_name)
    re=requests.get(str1)
    data=json.loads(re.text)
    data1=data['Summary']
    for i,j in data1.items():
        if(i=='Code'):
            data1[i]=j.lower()
    
    return render(request,'state.html',{'data':data['State'],'data1':data1})
