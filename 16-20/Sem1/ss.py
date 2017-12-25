import csv

#----------------------------------------------------------------------
def csv_dict_reader(file_obj):
	text_file = open("CC_avg2.txt", "a")

	"""
	Read a CSV file using csv.DictReader
	"""
	reader = csv.DictReader(file_obj, delimiter=',')
	ns=0
	avg=0
	n=0
	avtemp=0.0
	temp=0.0 
	clist=["1aa","1ac","1ah","1aj","1ak","1am","1ao","1ap","1ar","1as","1at","1au","1ay","1bc","1bg","1bh","1bi","1bm","1bn","1bo","1bs","1bt","1by","1cc","1cd","1ce","1cg","1ck","1cr","1da","1db","1ds","1dt","1ec","1ep","1ew","1ga","1gc","1gd","1gg","1gs","1gv","1hk","1hm","1hs","1ic","1ii","1jb","1js","1jt","1jv","1kh","1ki","1kn","1ks","1kt","1me","1mj","1mv","1nc","1nh","1nj","1ox","1pe","1pn","1rc","1re","1rg","1ri","1rl","1rn","1rr","1sb","1sc","1sg","1sj","1sk","1sp","1st","1sv","1sw","1sz","1tj","1va","1ve","1vi","1vj","1vk","1yd"]
	cname=["Acharya NRV School of Architecture","Alpha College of Engineering","ACS COLLEGE OF ENGINEERING","Adarsha Institute of Technology","AKSHAYA INSTITUTE OF TECHNOLOGY","Amc Engineering College","ACHUTHA INSTITUTE OF TECHNOLOGY","Acharaya Patha Shala(A.P.S) College of Engg.","AMRUTHA INSTITUTE OF ENGINEERING AND MGMT. SCIENCES","AMRUTHA INSTITUTE OF ENGINEERING AND MGMT. SCIENCES","Atria Institute of Technology","Auden Technology and Mgmt. Academy","Acharaya Institute of Technology","Bangalore College of Engineering and Technology","B.N.M.Institute of Technology","Bangalore TECHNOLOGICAL INSTITUTE","Bangalore Institute of Technology","Bms College of Engineering","Sri Belimatha Maha Sahamsthana Institute of Technology","BRINDAVAN COLLEGE OF ENGG","Basava Academy of Engineering","B.T.L.Institute of Technology","Bms Institute of Technology","Dr. Sri Sri Sri SHIVKUMAR MAHASWAMY, COLLEGE OF ENGG.","Cambridge Institute of Technology","City Engineering College","Channa Basaveshwara Institute of Technology","C Byregowda Insititute Of Technology","C.M.R Institute of Technology","Dr. Ambedkar Institute of Technology","Don Bosco Institute of Technology","Dayananda Sagar College of Engineering","DAYANANDA SAGAR ACADEMY OF TECHNOLOGY AND MGMT.","EAST POINT COLLEGE OF ENGG. FOR WOMEN","East Point College of Engineering and Technology","East West Institute of Technology","Global Academy of Technology","Ghousia College of Engineering","GOPALAN COLLEGE OF ENGINEERING MANAGEMENT","Govt. Engineering College Ramnagar","G.S.S.Institute of Technology","Dr. T Thimaiah Institute of Technology","Hkbk College of Engineering","Hms Institute of Technology","SHASHIB COLLEGE OF ENGINEERING","Impact College of Engineering","Islamiah Institute of Technology","Sjb Institute of Technology","Jss Academy of Technicial Education","JYOTHY INSTITUTE OF TECHNOLOGY","Jnana Vikas Institute of Technology,","SRI KRISHNA SCHOOL OF ENGINEERING MANAGEMENT","Kalpataru Institute of Technology","Kns Institute of Technology","K.S.Institute of Technology","Sri Krishna Institute of Technology","M.S.Engineering College","Mvj College of Engineering","Sir M. Visvesvaraya Institute of Technology","Nagarjuna College of Engineering and Technology","New Horizon College of Engineering","Nadgir Institute of Engineering and Technology","Oxford College of Engineering","Pes School of Engineering","P N S WOMENS INSTITUTE OF TECHNOLOGY","Sri Revanasiddeshwara Institute of Technology","Reva Institute of Technology and Mangement","Rajiv Gandhi Institute of Technology","R R INSTITUTE OF TECHNOLOGY","R.L.Jalappa Institute of Technology","Rns Institute of Technology","Rajarajeswari College of Engineering","Shirdi Sai Engineering College","Sct Institute of Technology","Sapthagiri College of Engineering","S.J.C Institute of Technology","Government SKSJT Institute of Technology","Sea College of Engineering and Technology","Sambhram Institute of Technology","Shridevi Institute of Engineering and Technology","SRI BASAVESHWAR INSTITUTE OF TECHNOLOGY","SAMPOORNA INSTITUTE OF TECHNOLOGY? RESEARCH","T. John Institute of Technology","SAI VIDYA INSTITUTE OF TECHNOLOGY","Sri Venkateshwara College of Engineering","Vemana Institute of Technology","VIJAYA VITTALA INSTITUTE OF TECHNOLOGY","Vivekananda Institute of Technology","Yellamma Dasappa Institute of Technology"]
	for line in reader:
		if(line["sgpa"]==0):
			continue
		if(line["CC"]==((clist[n]).upper())):
			avg=avg+float(line["sgpa"])
			ns=ns+1
			#print(line)
		else:
			if ns==0:
				while (line["CC"]!=((clist[n]).upper())):
					n=n+1
					avg=avg+float(line["sgpa"])
					ns=ns+1
			#	print((clist[n]).upper())
			#	print(avg,line["CC"])
			#	n=n+1
		
			else:
				print("N={0},Average:{1},Cname:{2}\n".format(ns,avg/ns,cname[n]))
				text_file.write("{0},{1},{2}\n".format(ns,avg/ns,cname[n]))
				n=n+1
				ns=0
				avg=0
				avg=avg+float(line["sgpa"])
				ns=ns+1
			#	print(line)
			#	print("##N={0},Avg:{1}".format(ns,avg/ns))
				
				text_file.close()
				text_file = open("CC_avg2.txt", "a")

	print("N={0},Average:{1},Cname:{2}\n".format(ns,avg/ns,cname[n]))
	text_file.write("{0},{1},{2}\n".format(ns,avg/ns,cname[n]))
	text_file.close()
				
#----------------------------------------------------------------------
if __name__ == "__main__":
	with open("BLR_2.csv") as f_obj:
		csv_dict_reader(f_obj)