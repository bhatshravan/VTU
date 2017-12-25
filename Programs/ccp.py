#All imports
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
ccend=8 #ending college code

urlerror=0 #number of urlerrors,will check if its greater than 6 and terminate

start_time = timeit.default_timer()

usn=0
uusn=""
nuerror=0
ccycle="P"
cdone="false"

#college lists
clist=["1ay","1ap","1aa","1ao","1ah","1aj","1ak","1ac","1am","1ar","1as","1at","1au","1bg","1bt","1bc","1bi","1bh","1bs","1bm","1by","1bo","1ck","1cr","1cd","1cg","1ce","1dt","1ds","1db","1da","1cc","1gv","1ec","1ep","1ew","1gs","1gc","1ga","1gd","1sk","1gg","1hk","1hm","1ic","1ii","1jv","1js","1jt","1ks","1ki","1kn","1me","1mj","1nj","1nc","1nh","1ox","1pn","1pe","1ri","1rl","1rr","1rg","1re","1rn","1sj","1va","1st","1sz","1sg","1sc","1sp","1hs","1sb","1sv","1mv","1jb","1sw","1bn","1kt","1kh","1rc","1ve","1tj","1vi","1vj","1vk","1yd","4ad","4ai","4al","4bw","4bb","4bd","4bp","4cb","4ci","4dm","4ek","4mg","4gm","4ge","4gh","4gl","4gk","4gw","4jn","4kv","4km","4mh","4mt","4mk","4nn","4pa","4pm","4pr","4ra","4sf","4sh","4mw","4sm","4su","4sn","4es","4so","4ub","4vv","4vm","4vp","4yg"]

####################################################################

#Urls
url1="http://result.vtu.ac.in/cbcs_results2016.aspx?usn="
url5="&sem=1&prg=UG"
url3="16CS"
susn=""

#####################################################################
#Calulations

#loop through all given colleges
while ccurl<=ccend:
	
	#Get current college code
	ucc=(clist[ccurl]).upper()
	text_file = open("Output.txt", "a")
	
	if(usn==1):
		print("\nGoing to next college")
		text_file.close()
		text_file = open("Output.txt", "a")
		#No more usn's remaining,go to next college
		cdone="false"
		ccurl=ccurl+1
		usn=0
		
		
	else:
	
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
		
		#Try connecting to the url
		try:
			soup = BeautifulSoup(urlopen(url),"html.parser")
			cycle = soup.find(attrs={"id": "txtCode2"})['value']
			if(cycle=="15PHY12"):
				ccycle="P"
			else:
				ccycle="C"
			
			sgpa = soup.find("span", {"id":"lblSGPA"})
			name = soup.find(attrs={"id": "txtName"})['value']
			s1 = soup.find(attrs={"id": "txtGP1"})['value']
			s2 = soup.find(attrs={"id": "txtGP2"})['value']
			s3 = soup.find(attrs={"id": "txtGP3"})['value']
			s4 = soup.find(attrs={"id": "txtGP4"})['value']
			s5 = soup.find(attrs={"id": "txtGP5"})['value']
			s6 = soup.find(attrs={"id": "txtGP6"})['value']
			s7 = soup.find(attrs={"id": "txtGP7"})['value']
			s8 = soup.find(attrs={"id": "txtGP8"})['value']

			print ('{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12}'.format(ucc,susn,ccycle,name,sgpa.text,s1,s2,s3,s4,s5,s6,s7,s8))
			text_file.write('\n{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12}'.format(ucc,susn,ccycle,name,sgpa.text,s1,s2,s3,s4,s5,s6,s7,s8))
			nuerror=0
		except:
			#Could not connect to url
			nuerror=nuerror+1
			if(nuerror>5):
				cdone="done"
			print("Error")

print("My watch has ended")
elapsed = timeit.default_timer() - start_time
print(elapsed)