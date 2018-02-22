#All imports
import requests
import http.client 
from time import sleep
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import timeit

####################################################################
#Random initializations
count=0 

ccurl=0 #starting college code
ccend=100 #ending college code

urlerror=0 #number of urlerrors,will check if its greater than 6 and terminate

start_time = timeit.default_timer()

usn=0
uusn=""
nuerror=0
ccycle="P"
cdone="false"

#college lists
clist=["1cd","1cg","1ce","1dt","1ds","1db","1da","1cc","1gv","1ec","1ep","1ew","1gs","1gc","1ga","1gd","1sk","1gg","1hk","1hm","1ic","1ii","1jv","1js","1jt","1ks","1ki"]

####################################################################

#Urls
url1="http://results.vtu.ac.in/cbcs_17/result_page.php?usn="
url5=""
url3="16CS"
susn=""

#####################################################################
#Calulations

#loop through all given colleges
while ccurl<=ccend:
	
	#Get current college code
	ucc=(clist[ccurl]).upper()
	text_file = open("Sem2-re.txt", "a")
		
	if(cdone=="done"):
		print("\nGoing to next college")
		text_file.close()
		text_file = open("SS2-16.txt", "a")
		#No more usn's remaining,go to next college
		cdone="false"
		ccurl=ccurl+1
		usn=0
		nuerror=0
		
		
	else:
		sgpa=0
		#Get VTU URL
		usn=usn+1
		if(usn<10):
			uusn="00"+str(usn)
		elif(usn<100):
			uusn="0"+str(usn)
		else:
			uusn=str(usn)
		url=url1+ucc+url3+uusn+url5
		susn=ucc+url3+uusn
		
		response =requests.post('http://results.vtu.ac.in/cbcs_17/result_page.php', files={'usn': (None,ucc+url3+uusn+url5), 'value_2': (None, '67890')})
		#print(response.status_code)
		#print(response.content)

		#Try connecting to the url
		soup = BeautifulSoup(response.content,"html.parser")
		tables = soup.findChildren('table')
		my_table = tables[1]
		rows = my_table.findChildren(['th', 'tr'])
		ll=1
		i1=i2=i3=i4=i5=i6=i7=i8=0;
		sgpa=0
		value2=0
		valuen=4
		valuesum=0
		gradesum=0
		for row in rows:
				j=1
				valuen=4
				cells = row.findChildren('td')
				for cell in cells:
						j=j+1
						if(j==6):
								if(ll==14 or ll==13):
										valuen=2
								if(ll==15):
										valuen=0
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
								
				#print(ll)
				if(ll==8):
						i1=value
				if(ll==9):
						i2=value
				if(ll==10):
						i3=value
				if(ll==11):
						i4=value
				if(ll==12):
						i5=value
				if(ll==13):
						i6=value
				if(ll==14):
						i7=value
				if(ll==15):
						i8=value
				ll=ll+1
		sgpa=round((gradesum/24),2)
		
		if(sgpa==0):
			nuerror=nuerror+1
			if(nuerror>6):
				cdone="done"
		else:
			print ('{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}'.format(ucc,susn,sgpa,i1,i2,i3,i4,i5,i6,i7,i8))
			text_file.write('\n{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}'.format(ucc,susn,sgpa,i1,i2,i3,i4,i5,i6,i7,i8))
			nuerror=0

	
print("My watch has ended")
elapsed = timeit.default_timer() - start_time
print(elapsed)
