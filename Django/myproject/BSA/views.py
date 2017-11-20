# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render
from BSAClass import BSA
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
'''
def Catch_BSA(request,num='4',group='-1'):
    SQLconnect.connectDB()
    Data = SQLconnect.exeSQl("SELECT * FROM `main`")
    TypeList = SQLconnect.exeSQl("SELECT * FROM `TypeDoc`")
    SQLconnect.close()  

    NumOfBS    = int(num)
    Group      = str(group)
    print NumOfBS,Group
    input_text = DB2csv.re_csv(Data,TypeList)
    content    = "\n".join(input_text.splitlines())
        
    
    if Group != str(-1):
        #print Group
        TheBSA = BSA(content,NumOfBS)
        TheBSA.ComputeMotionGroup(int(Group))
        content = TheBSA.Re_MotionArray_Label()
    else:
        content = BSA(content,NumOfBS).Re_MotionArray_Label()
    
    #content=[["hello"]]    
    template = 'showData.html'
    responds = {"Data":content}

    return render(request,template,responds )
'''
def Catch_From_DB_to_BSA(request,num='4',group='-1'):
    SQLconnect.connectDB()
    Data = SQLconnect.exeSQl("SELECT * FROM `main`")
    TypeList = SQLconnect.exeSQl("SELECT * FROM `TypeDoc`")
    SQLconnect.close()  

    NumOfBS    = int(num)
    Group      = str(group)
    print NumOfBS,Group
    input_text = DB2csv.re_csv(Data,TypeList)
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
def Cal_BSA(request):
    try:
        input_text = request.POST['content']#linebreaks
        NumOfBS = int(request.POST['NumOfBS'])
        Group = int(request.POST['Group'])
        content = "\n".join(input_text.splitlines())
        #print content
    except Exception as e:
        print e
        print "error!! Can NOT catch POST['content']"
        content = "empty"
        input_text = "empty"
        NumOfBS = 6
        Group= -1
    if content != "empty":
        try:
            if Group != -1:
                print Group
                TheBSA = BSA(content,NumOfBS)
                TheBSA.ComputeMotionGroup(int(Group))
                content = TheBSA.show(2)
            else:
                content = BSA(content,NumOfBS).show(2)
        except Exception as e:
            print "Error when convert to BSA ",e

    
    template = 'CalBSA.html'
    responds = {'current_time': str(datetime.now()),
        'csv_data': input_text,
        'array_BSA': content,
        'NumOfBS':NumOfBS,
        'Group':Group
                }
    return render(request,template,responds )


def API_BSA_Json(request,num='4',group='-1',ApiType="BArray",source="DB"):
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
            content    = "\n".join(input_text.splitlines())
        except:
            return "error 0.3: couldn't connect to DB"
    elif source == "inputCsv":
        pass
    elif source == "inputJson":
        pass
        
    else:
        return "error 0.1: Unknow Source"

    #####
    # Data compute
    if str(ApiType) == "BArray":
        content = ReBArrayOfApi(content,num,group)
    elif str(ApiType)=="Zscore":
        content = ReZscoreOfApi(content,num,group)
    else:
        return "error 2.1: Unknow API Enterance"

    template = 'showString.html'
    responds = {"Data":content}
    return render(request,template,responds )


###### show view END######

def ReBArrayOfApi(content,num='4',group='-1'):
    
    JsonString="initial"
    NumOfBS    = int(num)
    Group      = str(group)

    TheBSA = BSA(content,NumOfBS)
    if Group != str(-1):       
        TheBSA.ComputeMotionGroup(int(Group))
    JsonString = TheBSA.Re_MotionArray_Json()
    return JsonString

    
def ReZscoreOfApi(content,num='4',group='-1'):
    
    JsonString="initial"
    NumOfBS    = int(num)
    Group      = str(group)

    TheBSA = BSA(content,NumOfBS)
    if Group != str(-1):       
        TheBSA.ComputeMotionGroup(int(Group))
    JsonString = TheBSA.Re_ZscoreArray_Json()
    
    return JsonString


