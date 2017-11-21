#coding:utf-8
#Csv file of Source Data convert to Behavior Sequential class
'''
using;

FirstBSA = BSA('DataFormWuret.csv',6)
print FirstBSA.SelectedArray

FirstBSA.ComputeMotionGroup('21')
print FirstBSA.SelectedArray
'''


import csv
import numpy
class B_source:
    def __init__(self,con,FType="csv"):
        self.content = str(con)
        self.FileType = str(FType)
        self.Re_list = []
        if self.FileType == "csv":
            try:
                self.Re_list = self.ReadCSV(self.content)
            except:
                return "error 1.1: Invalid CSV input value"
        elif self.FileType == "json":
            try:
                self.Re_list = self.ReadCSV(self.content)
            except:
                return "error 1.1: Invalid CSV input value"
        else:
            return "error 0.2: Unsupported input type"
        ####


   

    def ReadCSV(self,CSV_TEXT):
        listmotion = []
        CSV_TEXT = CSV_TEXT.split('\n')
        csvCursor = csv.reader(CSV_TEXT)
        ####
        for row in csvCursor:
            
            try:
                if row[2] != '':
                    listmotion.append([str(row[0]),int(row[2])])# Group , type
            except:
                print "warning: Input data:\'"+str(row)+'\' is warning'
                print "warning: Input data:\'"+str(row[2])+'\' not Int'

        return listmotion

    

         
        
        return self.Np2JsonString(ZscoreArray,self.TypeNum,self.TypeNum)

