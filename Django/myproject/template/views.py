# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render
from BSAClass import BSA
import os

###### show view ######

def hello_world(request):
    template = 'hello_world.html'
    responds = {'current_time': str(datetime.now()),}
    return render(request,template,responds )

def BSA_sample(request):
    template = 'sample.csv'
    responds = {}
    return render(request,template,responds )

def BSA_in_SQL(request):
    os.system("python /home/gavin/Desktop/wulab/Django/myproject/BSA/catch.py")
    template = 'exportExample.csv'
    responds = {}
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



###### show view END######




