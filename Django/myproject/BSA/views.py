# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render
from BSAClass import BSA
from BSAClass import BTest
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import os
import SQLconnect
import DB2csv
###### show view ######

def hello_world(request):
    template = 'hello_world.html'
    responds = {'current_time': str(datetime.now()),}
    return render(request,template,responds )

def BSA_sample(request):
    template = 'sample.csv'
    responds = {}
    return render(request,template,responds )

def catch_from_SQL(request):
    SQLconnect.connectDB()
    SQLconnect.status()
    Data = SQLconnect.exeSQl("SELECT * FROM `main`")
    SQLconnect.close()
    SQLconnect.status()
    template = 'showData.html'
    responds = {"Data":Data}


    #SQLconnect.db.closed()
    return render(request,template,responds )

def BehaviorList(request,stu_id):
    SQLconnect.connectDB()
    Data = SQLconnect.exeSQl("SELECT * FROM `main`")
    SQLconnect.close()
    NewData=[]
    for sqe in Data:
        if stu_id in sqe:
            NewData.append(sqe)
    template = 'showData.html'
    responds = {"Data":NewData}
    return render(request,template,responds )

def BehaviorAllList(request):#
    SQLconnect.connectDB()
    SQLconnect.status()
    UserList = SQLconnect.exeSQl("SELECT DISTINCT `Stu_Id` FROM `main`")    
    Data = SQLconnect.exeSQl("SELECT * FROM `main`")
    SQLconnect.close()
    SQLconnect.status()
    
    NewData=[]
    for u in UserList:
        NewSqe=[]
        u = ''.join(u)         
        NewSqe.append(u) 
        for sqe in Data:       
            if u in sqe[2]:               
                NewSqe.append(sqe[1])
        NewData.append(NewSqe)
    template = 'showData.html'
    responds = {"Data":NewData}


    return render(request,template,responds )

def Catch_From_DB_to_BSA(request,num='4',group='-1'):
    SQLconnect.connectDB()
    Data = SQLconnect.exeSQl("SELECT * FROM `main`")
    #TypeList = SQLconnect.exeSQl("SELECT * FROM `TypeDoc`")
    SQLconnect.close()  

    NumOfBS    = int(num)
    Group      = str(group)
    print NumOfBS,Group
    #input_text = DB2csv.re_csv(Data,TypeList)
    input_text = DB2csv.re_csv(Data)
    content    = "\n".join(input_text.splitlines())
        
    
    if Group != str(-1):
        #print Group
        TheBSA = BSA(content,NumOfBS)
        TheBSA.ComputeMotionGroup(str(Group))
        content = TheBSA.Re_MotionArray_Label()
    else:
        content = BSA(content,NumOfBS).Re_MotionArray_Label()
    
    #content=[["hello"]]    
    template = 'showData.html'
    responds = {"Data":content}

    return render(request,template,responds )

def draw_ZScore(request):
    import json
    import numpy
    try:
        JsonString = str(request.POST['JsonString'])
        holder = numpy.zeros(37,int)
        holder_source = numpy.zeros(37,float)
        jdata = json.loads(JsonString)
    except Exception as e:
        #print 'using default json',
        #JsonString = '[{"1":"0.583","2":"-0.399","3":"-0.383","4":"-0.257"},{"1":"-0.405","2":"0.54","3":"-0.176","4":"0.154"},{"1":"-0.457","2":"-0.163","3":"1.692","4":"0.027"},{"1":"-0.28","2":"0.17","3":"0.026","4":"0.198"}]'
        #holder = numpy.zeros(37,int)
        #jdata = json.loads(JsonString)
        return HttpResponse("error : Invalid Json input value :  "+str(e))
    
    #print jdata[0]['1']
    for i in range(len(jdata)):
        for j in jdata[i]:
            if float(jdata[i][j])>1.96:
                holder[(i*6+int(j))] = 1
            else:
                holder[(i*6+int(j))] = 0
            holder_source[(i*6+int(j))] = jdata[i][j]
    #print holder
    template = 'drawZScore.html'
    responds = {
        '1_1': holder[1],'1_2': holder[2],'1_3': holder[3],'1_4': holder[4],'1_5': holder[5],'1_6': holder[6],
        '2_1': holder[7],'2_2': holder[8],'2_3': holder[9],'2_4': holder[10],'2_5': holder[11],'2_6': holder[12],
        '3_1': holder[13],'3_2': holder[14],'3_3': holder[15],'3_4': holder[16],'3_5': holder[17],'3_6': holder[18],
        '4_1': holder[19],'4_2': holder[20],'4_3': holder[21],'4_4': holder[22],'4_5': holder[23],'4_6': holder[24],
        '5_1': holder[25],'5_2': holder[26],'5_3': holder[27],'5_4': holder[28],'5_5': holder[29],'5_6': holder[30],
        '6_1': holder[31],'6_2': holder[32],'6_3': holder[33],'6_4': holder[34],'6_5': holder[35],'6_6': holder[36],
        't1_1': holder_source[1],'t1_2': holder_source[2],'t1_3': holder_source[3],'t1_4': holder_source[4],'t1_5': holder_source[5],'t1_6': holder_source[6],
        't2_1': holder_source[7],'t2_2': holder_source[8],'t2_3': holder_source[9],'t2_4': holder_source[10],'t2_5': holder_source[11],'t2_6': holder_source[12],
        't3_1': holder_source[13],'t3_2': holder_source[14],'t3_3': holder_source[15],'t3_4': holder_source[16],'t3_5': holder_source[17],'t3_6': holder_source[18],
        't4_1': holder_source[19],'t4_2': holder_source[20],'t4_3': holder_source[21],'t4_4': holder_source[22],'t4_5': holder_source[23],'t4_6': holder_source[24],
        't5_1': holder_source[25],'t5_2': holder_source[26],'t5_3': holder_source[27],'t5_4': holder_source[28],'t5_5': holder_source[29],'t5_6': holder_source[30],
        't6_1': holder_source[31],'t6_2': holder_source[32],'t6_3': holder_source[33],'t6_4': holder_source[34],'t6_5': holder_source[35],'t6_6': holder_source[36],
        't1':'Null','t2':'Null','t3':'Null','t4':'Null','t5':'Null','t6':'Null','title':"Title is here."
        
    }
    return render(request,template,responds )

def Cal_BSA(request):
    
    content = "empty"
    input_text = "empty"
    NumOfBS = 6
    Group= -1
    
    template = 'CalBSA.html'
    responds = {'current_time': str(datetime.now()),
        'csv_data': input_text,
        'array_BSA': content,
        'NumOfBS':NumOfBS,
        'Group':Group
                }
    return render(request,template,responds )

@csrf_exempt #csrf skip
def API_BSA_Json(request,num='4',group='-1',ApiType="BArray",source="DB",con='none'):
    try:
        num = str(request.POST['num'])#linebreaks
        group = str(request.POST['group'])
        ApiType = str(request.POST['ApiType'])
        source = str(request.POST['source'])
        con = str(request.POST['con'])
    except Exception as e:
            return HttpResponse("error 0: Not catch post\n"+str(e))
    #####
    # source Defined
    content =""
    if source=="DB":
        try:
            SQLconnect.connectDB()
            Data = SQLconnect.exeSQl("SELECT * FROM `main`")
            TypeList = SQLconnect.exeSQl("SELECT * FROM `TypeDoc`")
            SQLconnect.close()      
            input_text = DB2csv.re_csv(Data,TypeList)
            source_type = "csv"
            content    = "\n".join(input_text.splitlines())
        except Exception as e:
            return HttpResponse("error 1.3: couldn't connect to DB\n"+str(e))
    elif source[:5] == "input":#input-csv
        if source[6:] == "csv":
            content = con
            source_type = "csv"
            try:                
                TheBSA = BTest(content,int(num),source_type)
            except Exception as e:
                return HttpResponse("error 2.1: Invalid CSV input value\n"+str(e))
        elif source[6:] == "json":
            try:
                pass
            except Exception as e:
                return HttpResponse("error 2.2:Invalid JSON input value\n"+str(e))
        else:
            return HttpResponse("error 1.2:Unsupported input type")
    else:
        return HttpResponse("error 1.1: Unknow Source")

    #####
    # Data compute
    if str(ApiType) == "BArray":
        content = ReBArrayOfApi(content,num,group,source_type)
    elif str(ApiType)=="ZScore":
        try:
            content = ReZscoreOfApi(content,num,group,source_type)
        except Exception as e:
                return HttpResponse("error 4.1:Invalid value in setting\n"+str(e))
    else: 
        return HttpResponse("error 3.1: Unknow API Enterance : "+str(ApiType))

 

    return HttpResponse(content)#context_instance = RequestContext(request)

###### show view END######

def ReBArrayOfApi(content,num,group,ContentType):
    JsonString="initial"
    NumOfBS    = int(num)
    Group      = str(group)

    TheBSA = BSA(content,NumOfBS,ContentType)
    if Group != str(-1):       
	    TheBSA.ComputeMotionGroup(int(Group))
    JsonString = TheBSA.Re_MotionArray_Json()
    return JsonString

    
def ReZscoreOfApi(content,num,group,ContentType):
    
    JsonString="initial"
    NumOfBS    = int(num)
    Group      = str(group)

    TheBSA = BSA(content,NumOfBS,ContentType)
    if Group != str(-1):       
        TheBSA.ComputeMotionGroup(int(Group))
    JsonString = TheBSA.Re_ZscoreArray_Json()
    
    return JsonString



