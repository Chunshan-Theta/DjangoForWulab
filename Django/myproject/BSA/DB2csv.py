


def re_csv(Data,TypeList):
	input_text=''
	for i in Data:
		IType='99'        
		for t in TypeList:
			if t[1] == str(i[1]):
			    #print t[1],str(i[1]),t[0]        
			    IType = int(t[0])
		input_text+=str(i[5])+','+str(i[2])+','+str(IType)+','+str(i[3])+','+str(i[4])+'\n'
		print i[0]
	return input_text
    
