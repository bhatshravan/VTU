#All imports
import requests
import http.client 
from time import sleep
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import timeit

cdone="ndone"
i=0
####################################################################
#Random initializations

response =requests.post('http://localhost/vt.html', data={'usn':'1ks'})
soup = BeautifulSoup(response.content,"html.parser")
sgpa = soup.find("div", {"class":"divTableBody"})
#print(sgpa)
rows = sgpa.findChildren("div", {"class":"divTableRow"})

n1 = soup.findChildren("table")
#n = n1.find("td")
rows = soup.findChildren(['th', 'tr'])

for row in rows:	
	print(row.encode("utf-8"))

for row in rows:
	if i!=0:
		volume = row.findAll("div", {"class": "divTableCell"})[4].string
		print(volume)
	i=i+1
		
	"""
	cells = row.findChildren("div", {"class":"divTableCell"})
	for cell in cells:
		j=j+1
		#if j==10 or j==16 or j==22 or j==28 or j==34 or j==40 or j==46:
		#s1 = cell.find(attrs={"class": "divTableCell"})['value']
		print(cell)
	"""
	#	print("\n")


"""
for my_table in tables:
	try:
		i=-1
		rows = my_table.findChildren(['divTableRow'])
		print("\n\nTABLE------{0}\n{1}\n".format(j))
		j=j+1
		for row in rows:
			i=i+1
			print(i)
			print(row)
	except Exception as e:
		print("Error in table")
		print(e)
				
"""