__author__ = 'Abi'


import pandas as pd
from sklearn import tree
import sklearn



data = pd.DataFrame()
data = pd.read_csv("C:/Users/Mithus/Documents/testdata.csv")
clf = tree.DecisionTreeClassifier()
data = data.dropna()
data = data.reset_index()
data = data[data["12th"]!="#VALUE!"]
data = data.reset_index()



deptMacro = {"ECE":0,"Mech":1,"AE":2,"CHE":3,"CIVIL":4,"CSE":5,"EIE":6,"EEE":7}

boardMacro = {"SB-HP":0,"SB-GJ":1,"SB-MH":2,"SB-AP":3,"SB-TN":4,"SB-BI":5,"SB-KA":6,"CBSE":7,"ISC":8,"-1":111,"SB-RJ":9,"SB-KL":10}

#ASMacro = {"4.5":4.5,"8":8.0,"3.3":3.3,"NP-0":0.0}

COMPMacro = {"NP-D":-1,"T2":2,"T1":1,"T3":3,"NP-NE":4,"NP":0,"NP-NI":5}

#offersMacro = {"1":1,"2":2,"3":3,"NP-0":0}

genderMcro = {'M':0,'F':1}

for index in range(len(data)):
	#Macro Based Changes
	data.loc[index,"Gender"] = int(genderMcro[data.loc[index,"Gender"]])
	data.loc[index,"Dept"] = int(deptMacro[data.loc[index,"Dept"]])
	data.loc[index,"Board"] = int(boardMacro[data.loc[index,"Board"]])
	#data.loc[index,"AS"] = float(ASMacro[data.loc[index,"AS"]])
	#data.loc[index,"offers"] = int(offersMacro[data.loc[index,"offers"]])
	data.loc[index,"COMP"] = int(COMPMacro[data.loc[index,"COMP"]])


	#String based changes
	if len(data.loc[index,"Location"])>3:
		data.loc[index,"Location"] = int(data.loc[index,"Location"][:3])

	elif len(data.loc[index,"Location"])<3 and data.loc[index,"Location"]=="-1":
		data.loc[index,"Location"] = int(000)

	data.loc[index,"12th"] = float(data.loc[index,"12th"])


tempY = data["COMP"]
dropList = ["COMP","level_0","index"]

data.drop(dropList,inplace=True,axis=1)
X = data.values
factors = X.tolist()

Y =tempY.values
predictors = Y.tolist()

stoVal = 0

for x in factors:
	for el in x:
		if type(el) == str:
			stoval = factors.index(x)
			factors.remove(x)
			#print stoVal
			predictors.remove(Y[stoVal])

clf = clf.fit(factors, predictors)
print "Modelling succesful"
f=open("C:/Users/Mithus/Documents/NetBeansProjects/projectgui/upload.txt","r")
path=f.readline()
#print path
ppath= path.replace('\\','/')
#print ppath
from pandas import DataFrame
import xlrd
import xlwt
#wbk = xlwt.Workbook()
#wkst = wbk.add_sheet('sheet1')  

workbook = xlrd.open_workbook(ppath)
worksheet = workbook.sheet_by_name('Sheet1')
num_rows = worksheet.nrows - 1
num_cells = worksheet.ncols - 1
curr_row = -1
fdept=[]
fgender=[]
fboard=[]
flocation=[]
ftwth=[]
fna=[]
fah=[]
fcgpa=[]
fr=[]

while curr_row < num_rows:
	curr_row += 1
	row = worksheet.row(curr_row)
	print 'Row:', curr_row
	curr_cell = -1
	if (curr_row>0):
		while curr_cell < num_cells:
			curr_cell += 1
		# Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
			cell_type = worksheet.cell_type(curr_row, curr_cell)
			cell_value = worksheet.cell_value(curr_row, curr_cell)

			if(curr_cell==0):
				dept=str(cell_value)
				fdept.append(dept)
			elif(curr_cell==1):
				gender=str(cell_value)
				fgender.append(gender)
			elif(curr_cell==2):
				board=str(cell_value)
				fboard.append(board)
			elif(curr_cell==3):
				location=str(cell_value)
				flocation.append(location)
			elif(curr_cell==4):
				twth=str(cell_value)
				ftwth.append(twth)
			elif(curr_cell==5):
				na=str(cell_value)
				fna.append(na)
				#print na
				#print type(na)
			elif(curr_cell==6):
				ah=str(cell_value)
				fah.append(ah)
			elif(curr_cell==7):
				cgpa=str(cell_value)
				fcgpa.append(cgpa)
			else:
				print "error occured"
        
            
		lm=location[:3]
		tm=float(twth)
		arm=int(float(na))
		ahm=int(float(ah))
		cm=float(cgpa)
    
		if dept=="ECE":
			dm=0
		elif dept=="Mech":
			dm=1
		elif dept=="AE":
			dm=2
		elif dept=="CHE":
			dm=3
		elif dept=="CIVIL":
			dm=4
		elif dept=="CSE":
			dm=5
		elif dept=="EIE\n":
			dm=6
		elif dept=="EEE\n":
			dm=7
		else:
			print "department not selected"
    
		if gender=="M":
			gm=0
		elif gender=="F":
			gm=1
		else:
			print "gender not selected"
    
		if board=="SB-HP":
			bm=0
		elif board=="SB-GJ":
			bm=1
		elif board=="SB-MH":
			bm=2
		elif board=="SB-AP":
			bm=3
		elif board=="SB-TN":
			bm=4
		elif board=="SB-BI":
			bm=5
		elif board=="SB-KA":
			bm=6
		elif board=="CBSE":
			bm=7
		elif board=="ISC":
			bm=8
		elif board=="SB-RJ":
			bm=9
		elif board=="SB-KL":
			bm=10
		else:
			print "board not selected"
    
		#print "result"
		result=clf.predict([dm,gm,bm,lm,tm,arm,ahm,cm])
		#print result
		k=result[0]

		if k==0:
			r="Not Placed"
			print r
			fr.append(r)
		elif k==1:
			r="Dream Company"
			print r
			fr.append(r)
		elif k==2:
			r="Core Company"
			print r            
			fr.append(r)
		elif k==3:
			r="Mass Recruiter"
			print r            
			fr.append(r)
		elif k==4:
			r="Not Eligible"
			print r            
			fr.append(r)
		elif k==5:
			r="Not Interested"
			print r            
			fr.append(r)
		else:
			print "Error Occured"
l1=fdept
l2=fgender
l3=fboard
l4=flocation
l5=ftwth
l6=fna
l7=fah
l8=fcgpa
l9=fr
print len(fdept)
print len(fgender)
print len(fboard)
print len(flocation)
print len(ftwth)
print len(fna)
print len(fah)
print len(fcgpa)
print len(fr)

g=open('C:/Users/Mithus/Documents/NetBeansProjects/projectgui/new.txt','w')
g.write("worked")
g.close()



df=DataFrame({'Department':l1,'Gender':l2, 'Board':l3,'Location':l4, '12th':l5, 'NA':l6, 'AH':l7, 'CGPA':l8, 'COMP':l9})
df.to_excel('C:/Users/Mithus/Desktop/newthree.xlsx', sheet_name='sheet1', index='false')
