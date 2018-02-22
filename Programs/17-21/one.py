#All imports
import requests
import http.client 
from time import sleep
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import timeit
import sys
import winsound
####################################################################
#Random initializations
global gradesum

count=0 

ccurl=0 #starting college code
ccend=100 #ending college code

urlerror=0 #number of urlerrors,will check if its greater than 6 and terminate

start_time = timeit.default_timer()


var1=0
var2=0

skip=0

usn=92
uusn=""
nuerror=0
ccycle="P"
cdone="false"

#college lists
clist=["1cd","1cg","1ce","1dt","1ds","1db","1da","1cc","1gv","1ec","1ep","1ew","1gs","1gc","1ga","1gd","1sk","1gg","1hk","1hm","1ic","1ii","1jv","1js","1jt","1ks","1ki"]
#clist=["1KS"]
####################################################################

#Urls
url1="http://results.vtu.ac.in/vitaviresultcbcs/resultpage.php"
url5=""

url31="16"
url32="CS"
url3=url31+url32
susn=""


gradesum=0
ln=0
#####################################################################
#Calulations

#loop through all given colleges
while ccurl<=ccend:
	#Get current college code   
	#ucc=(clist[ccurl]).upper()
	ucc="1KS"
	text_file = open("17-sen-Sem1.txt", "a")
		
	if(cdone=="done" or skip>5):
		print("\nGoing to next college")
		text_file.close()
		text_file = open("S1-17.txt", "a")
		#No more usn's remaining,go to next college
		cdone="false"
		ccurl=ccurl+1
		usn=0
		nuerror=0
		
	elif(cdone=="y"):
		sys.exit(0)
	else:
		sgpa=0
		

		ln=ln+1
		print(ln)
		
		nuerror=0
		usn=92
		skip=0
		#Get VTU URL
		#usn=usn+1
		
		if(usn==93):
			sys.exit(0)
		elif(usn<10):
			if(usn>8):
				sys.exit(0)
			uusn="00"+str(usn)
		elif(usn<100):
			uusn="0"+str(usn)
		else:
			uusn=str(usn)
		url=url1+ucc+url3+uusn+url5
		susn=ucc+url3+uusn
		ultusn=ucc+url3+uusn+url5
		
		print(ultusn)
		try:
			response =requests.post('http://results.vtu.ac.in/vitaviresultcbcs/resultpage.php', data={'usn':ultusn}, timeout=30)
				
			soup = BeautifulSoup(response.content,"html.parser")
			
			tables = soup.findChildren("div", {"class":"divTableBody"})
	
			rows = tables[0].findChildren("div", {"class":"divTableRow"})
	
			ll=1
			i1=i2=i3=i4=i5=i6=i7=i8=0;
			sgpa=0
			valuen=4
			valuesum=0
			gradesum=0
			
			i1 = rows[1].findAll("div", {"class": "divTableCell"})[4].string
			i2 = rows[2].findAll("div", {"class": "divTableCell"})[4].string
			i3 = rows[3].findAll("div", {"class": "divTableCell"})[4].string
			i4 = rows[4].findAll("div", {"class": "divTableCell"})[4].string
			i5 = rows[5].findAll("div", {"class": "divTableCell"})[4].string
			i6 = rows[6].findAll("div", {"class": "divTableCell"})[4].string
			i7 = rows[7].findAll("div", {"class": "divTableCell"})[4].string
			i8 = rows[8].findAll("div", {"class": "divTableCell"})[4].string
			var1=0
			for row in rows:
				volume = row.findAll("div", {"class": "divTableCell"})[4].string
	
				if var1!=0:
					value=int(volume)
					
					if (var1==7 or var1==8):
						var2=2
					else:
						var2=4
	
	
					if(value>=40 and value<45):
						value2=4
					elif(value>=45 and value<50):
						value2=5
					elif(value>=50 and value<60):
						value2=6
					elif(value>=60 and value<70):
						value2=7
					elif(value>=70 and value<80):
						value2=8
					elif(value>=80 and value<90):
						value2=9
					elif(value>=90):
						value2=10
					elif(value<40):
						value2=0
					gradesum=gradesum+(value2*var2)
		
	
				var1=var1+1
			sgpa=round((gradesum/28),2)

			
			if(sgpa==0):
				nuerror=nuerror+1
				if(nuerror>6):
					cdone="done"
					break
	
			else:
				print ('{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}'.format(ucc,susn,sgpa,i1,i2,i3,i4,i5,i6,i7,i8))
				text_file.write('{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}\n'.format(ucc,susn,sgpa,i1,i2,i3,i4,i5,i6,i7,i8))
				text_file.close()
	
				text_file = open("17-sen-Sem1.txt", "a")
				nuerror=0
				skip=0
		except Exception as e:
			print(e)
			usn=usn-1
			nuerror=nuerror+1
			if(nuerror>3):
				if(skip>4):
					cdone="y"
				else:
					print("Skipping usn ")
					skip=skip+1
					usn=usn+1
					nuerror=0
			print("Error")
			continue

	
def getMarks(cell,valuen):
	global gradesum
	value = int(cell.string)
	if(value>=40 and value<45):
			value2=4
	if(value>=45 and value<50):
			value2=5
	if(value>=50 and value<60):
			value2=6
	if(value>=60 and value<70):
			value2=7
	if(value>=70 and value<80):
			value2=8
	if(value>=80 and value<90):
			value2=9
	if(value>=90):
			value2=10
	if(value<40):
			value2=0
	gradesum=gradesum+(value2*valuen)
	#return gradesum
	
print("My watch has ended")
elapsed = timeit.default_timer() - start_time
print(elapsed)
