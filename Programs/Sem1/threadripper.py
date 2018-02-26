import _thread
import http.client # module for making HTTP request to website
import winsound # module for making beep like noise once website is up
from time import sleep # module for putting a desired delay to reduce load on computer system
count=0 
import timeit
start_time = timeit.default_timer()
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

import time

# Define a function for the thread
def print_time( threadName, i,imax):
	l=""
	text_file = open("Output4.txt", "a")
	while(i<imax):
		if(i<10):
			l="http://result.vtu.ac.in/cbcs_results2017.aspx?usn=1KS16CS00"+str(i)+"&sem=1"
		elif(i>9 and i<100):
			l="http://result.vtu.ac.in/cbcs_results2017.aspx?usn=1KS16CS0"+str(i)+"&sem=1"
		else:
			l="http://result.vtu.ac.in/cbcs_results2017.aspx?usn=1KS16CS"+str(i)+"&sem=1"
		
		soup = BeautifulSoup(urlopen(l),"html.parser")
		try:
			result = soup.find("span", {"id":"lblSGPA"})
			output = soup.find(attrs={"id": "txtName"})['value']
			output1 = soup.find(attrs={"id": "txtGP1"})['value']
			output2 = soup.find(attrs={"id": "txtGP2"})['value']
			output3 = soup.find(attrs={"id": "txtGP3"})['value']
			output4 = soup.find(attrs={"id": "txtGP4"})['value']
			output5 = soup.find(attrs={"id": "txtGP5"})['value']
			output6 = soup.find(attrs={"id": "txtGP6"})['value']
			output7 = soup.find(attrs={"id": "txtGP7"})['value']
			output8 = soup.find(attrs={"id": "txtGP8"})['value']
			#output = inputTag
			print ('{0}:{1}:{2}:{3}:{4}:{5}:{6}:{7}:{8}:{9}:{10}'.format(output,i,output1,output2,output3,output4,output5,output6,output7,output8,result.text))
			text_file.write('\n{0}:{1}:{2}:{3}:{4}:{5}:{6}:{7}:{8}:{9}:{10}'.format(output,i,output1,output2,output3,output4,output5,output6,output7,output8,result.text))
			
		except:
			print("error:{0}",i)
		i=i+1
	text_file.close()
# Create two threads as follows
try:
   _thread.start_new_thread( print_time, ("Thread-1", 1,10 ) )
   _thread.start_new_thread( print_time, ("Thread-2", 10,20 ) )
except:
   print ("Error: unable to start thread")

while 1:
	pass
