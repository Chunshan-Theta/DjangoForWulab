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
class BSA:
    def __init__(self,CsvSource,TypeNum,SourceType="csv"):
        self.SelectedArray = [[]]        
        self.TypeNum = TypeNum

        if SourceType == "csv":
            try:
                self.listmotion = self.ReadFile(CsvSource)
            except:
                self.listmotion = self.ReadCSV(CsvSource.encode("utf-8"))
            self.ComputeMotionALL()
        elif SourceType == "json":
            pass
        else:
            return "error 0.2: Unsupported input type"
        
          
        ####


    def ComputeMotionGroup(self,wantSet):
        FirstMotion = -1
        SecondMotion = -1
        TypeNum = self.TypeNum    
        listmotion = self.listmotion
        TypeNum +=1 # Because Data not contain 0
        MotionSet=numpy.zeros((TypeNum,TypeNum),int)
        ####

        for index in range(TypeNum-1):
            MotionSet[0][index+1]=index+1
            MotionSet[index+1][0]=index+1

        for index in range(len(listmotion)-1):
            if listmotion[index][0] == listmotion[index+1][0] and str(wantSet) == str(listmotion[index][0]):
                # if not same group, pass
                # if didn't select group, pass
                FirstMotion = listmotion[index][1]
                SecondMotion = listmotion[index+1][1]
                
                MotionSet[FirstMotion][SecondMotion] += 1
        #print MotionSet
        self.SelectedArray = MotionSet

    def ComputeMotionALL(self):
        FirstMotion = -1
        SecondMotion = -1
        TypeNum = self.TypeNum    
        listmotion = self.listmotion
        TypeNum +=1 # Because Data not contain 0
        MotionSet=numpy.zeros((TypeNum,TypeNum),int)
        ####
        
        for index in range(TypeNum-1): # Set Title of Raw
            MotionSet[0][index+1]=index+1
            MotionSet[index+1][0]=index+1
        
        for index in range(len(listmotion)-1):
                FirstMotion = listmotion[index][1]
                SecondMotion = listmotion[index+1][1]
                MotionSet[FirstMotion][SecondMotion] += 1
        self.SelectedArray = MotionSet

    def ReadFile(self,FileDir):
        listmotion = []
        Tfile = open(FileDir, 'r')
        csvCursor = csv.reader(Tfile)
        ####

        for row in csvCursor:
            try:
                if row[2] != '':
                    listmotion.append([str(row[0]),int(row[2])])# Group , type
            except:
                print "warring: Input data:\'"+str(row[2])+'\' not Int'
        Tfile.close()
        return listmotion


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

    def show(self,Actiontype=0):
        if Actiontype ==1: #without title
            for i in range(1,self.TypeNum+1):
                PrintStr =''
                for p in range(1,self.TypeNum+1):
                    PrintStr += str(self.SelectedArray[i,p])
                    PrintStr += ','
                print PrintStr

        elif Actiontype == 0:            
            print self.SelectedArray

        elif Actiontype == 2: # list of count
            '''
                1,1 99 \n 1,2 99 \n 1,3 99 \n 1,4 99 \n 1,5 99 \n 1,6 99 \n .....
            '''
            PrintStr = ""
            for i in range(1,self.TypeNum+1):
                for p in range(1,self.TypeNum+1):
                    PrintStr += str(i)+" "+str(p)+" "
                    PrintStr += str(self.SelectedArray[i,p])
                    PrintStr += "\n"
            return PrintStr
        else:
            print "Not found the action type"

    def ReNumOfMotionSet(self,Fir,Sec):
        return self.SelectedArray[Fir,Sec]
    
    def Re_MotionArray_Label(self):
        '''
        brief: return result of Behavior Sequential Analysis that with label string 
        output:
            [[1,1 1383],[1,2 157],[1,3 81],[1,4 334],[2,1 178],[2,2 657],[2,3 114],[2,4 511],[3,1 76],[3,2 118],[3,3 280],[3,4 208],[4,1 317],[4,2 528],[4,3 208],[4,4 742]
        '''
        reArray=[]
        for i in range(1,self.TypeNum+1):
            for p in range(1,self.TypeNum+1):
                label = str(i)+","+str(p)+" "
                Num = int(self.SelectedArray[i,p])
                reArray.append([label,Num])
        return reArray

    def Re_MotionArray_Json(self):
        '''
        brief:return result of Behavior Sequential Analysis with Json 

        output:
            {["1":"1383","1,2":"183".......],["1":"1383","1,2":"183".......],[...],...,[...]}
        '''
        
        return self.Np2JsonString(self.SelectedArray,self.TypeNum,self.TypeNum)


    def Np2JsonString(self,np,x,y):
        '''
        brief:Convert Numpy Array to Json (only x*y array) 
        input:
             np : NumpyArray(x*y)
             x  : Width of np
             y  : height of np
        output:
            {["1":"1383","1,2":"183".......],["1":"1383","1,2":"183".......],[...],...,[...]}
        '''
        reJsonString="{"
        for i in range(1,x+1):
            reJsonString += "["
            for p in range(1,y+1):
                reJsonString += "\""+str(p)+"\":"                
                if p != int(self.TypeNum):
                    reJsonString += "\""+str(np[i,p])+"\","
                else:# For End process
                    reJsonString += "\""+str(np[i,p])+"\""
            if i != int(self.TypeNum):
                reJsonString += "],"
            else:# For End process
                reJsonString += "]"
        reJsonString = reJsonString + "}"
        return reJsonString
        

'''
##using
FirstBSA = BSA('組別,ID,group_argu_code,論證內容,time\n4,s10008,1,唯有穩健減核，才能兼顧能源安全、經濟發展與民眾福祉，進而打造綠能低碳環境，逐步邁向非核家園。,4/14/2016 14:11\n4,s10008,1,核能發電對於經濟發展與國計民生，扮演舉足輕重的角色。,4/14/2016 14:12\n4,s10007,1,核廢料的汙染尚無法解決，若是發生問題會發生無法挽救的汙染。,4/14/2016 14:13',6)
FirstBSA.show()

FirstBSA.ComputeMotionGroup('4')


FirstBSA.ComputeMotionGroup('5')
FirstBSA.show()

FirstBSA.ComputeMotionALL()
print FirstBSA.show(2)

print FirstBSA.ReNumOfMotionSet(1,3)

'''
