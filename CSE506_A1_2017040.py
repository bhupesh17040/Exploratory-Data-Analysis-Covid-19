import pandas as pd 
import json as js
import numpy as np
import matplotlib.pyplot as plt

states_arr=["an","ap","ar","as","br","ch","ct","dd","dl","dn","ga","gj","hp","hr","jh","jk","ka","kl","la","ld",
			"mh","ml","mn","mp","mz","nl","or","pb","py","rj","sk","tg","tn","tr","up","ut","wb"]

# states_arr includes all states + union territories. This is an assumption because no specific label is mentioned for state or union territory.


def Q1_1(json_file_path, start_date, end_date):
	start_format=start_date.split("-",3)
	end_format=end_date.split("-",3)
	
	dd_start=start_format[2] #starting date
	dd_end=end_format[2]
	
	mm_start=" " # starting month
	mm_end=" " # ending month
	
	yr_start="20" #starting year
	yr_end="20" #ending year

	if(start_format[1]=="03"):
		mm_start="Mar"
	elif(start_format[1]=="04"):
		mm_start="Apr"
	elif(start_format[1]=="05"):
		mm_start="May"
	elif(start_format[1]=="06" ):
		mm_start="Jun"
	elif(start_format[1]=="07" ):
		mm_start="Jul"
	elif(start_format[1]=="08"):
		mm_start="Aug"
	elif(start_format[1]=="09"):
		mm_start="Sep"
	
	if(end_format[1]=="03"):
		mm_end="Mar"
	elif(end_format[1]=="04"):
		mm_end="Apr"
	elif(end_format[1]=="05"):
		mm_end="May"
	elif(end_format[1]=="06" ):
		mm_end="Jun"
	elif(end_format[1]=="07" ):
		mm_end="Jul"
	elif(end_format[1]=="08"):
		mm_end="Aug"
	elif(end_format[1]=="09"):
		mm_end="Sep"

	final_start_date=dd_start + "-" + mm_start + "-" + yr_start # starting date according to format in json
	final_end_date=dd_end + "-" + mm_end + "-" + yr_end  # ending date according to format in json

	with open(json_file_path) as df:
		dataf=js.load(df)
	all_dates=[]
	for i in dataf["states_daily"]:
		if(i["status"]=="Confirmed"):  # We can use any of "Confirmed","Deceased"  or "Recovered" to store dates
			all_dates.append(i["date"])

	start_index= all_dates.index(final_start_date) # Finding the index which is used later 
	end_index= all_dates.index(final_end_date)
	
	confirmed_count=0
	recovered_count=0
	deceased_count=0
	
	confirmed_arr=[]             # Storing each days confirmed count which is later used to iterate based on date
	recovered_arr=[]			# Storing each days recovered count which is later used to iterate based on date
	deceased_arr=[]				 #Storing each days deceased count which is later used to iterate based on date

	#states_arr=["an","ap","ar","as","br","ch","ct","dd","dl","dn","ga","gj","hp","hr","jh","jk","ka","kl","la","ld",
		#	"mh","ml","mn","mp","mz","nl","or","pb","py","rj","sk","tg","tn","tr","up","ut","wb"]

	# The variables "tt" and "un" have not been included in the states
	for j in range(start_index,3*(end_index)+3):  # Instead of creating a separate array[which will increase the length of the program],the code runs till 3*(end_index) + 3 to include all the three: confirmed,recovered and deceased
		#										  # This is different from the above 3 parts[ creating an array for each state will be redundant], that is the reason for using "count"
		if(dataf["states_daily"][j]["status"]=="Confirmed"):
			temp_x=dataf["states_daily"][j]
			for i in range(len(states_arr)):
				confirmed_arr.append(int(temp_x[states_arr[i]]))
		elif(dataf["states_daily"][j]["status"]=="Recovered"):
			temp_x=dataf["states_daily"][j]
			for i in range(len(states_arr)):
				recovered_arr.append(int(temp_x[states_arr[i]]))
		elif(dataf["states_daily"][j]["status"]=="Deceased"):
			temp_x=dataf["states_daily"][j]
			for i in range(len(states_arr)):
				deceased_arr.append(int(temp_x[states_arr[i]]))
	confirmed_count=sum(confirmed_arr)
	recovered_count=sum(recovered_arr)
	deceased_count=sum(deceased_arr)
	
	print('confirmed_count: ',confirmed_count, 'recovered_count:',recovered_count, 'deceased_count: ',deceased_count)

def Q1_2(json_file_path, start_date, end_date):
	start_format=start_date.split("-",3)
	end_format=end_date.split("-",3)
	
	dd_start=start_format[2] #starting date
	dd_end=end_format[2]
	
	mm_start=" " # starting month
	mm_end=" " # ending month
	
	yr_start="20" #starting year
	yr_end="20" #ending year

	if(start_format[1]=="03"):
		mm_start="Mar"
	elif(start_format[1]=="04"):
		mm_start="Apr"
	elif(start_format[1]=="05"):
		mm_start="May"
	elif(start_format[1]=="06" ):
		mm_start="Jun"
	elif(start_format[1]=="07" ):
		mm_start="Jul"
	elif(start_format[1]=="08"):
		mm_start="Aug"
	elif(start_format[1]=="09"):
		mm_start="Sep"
	
	if(end_format[1]=="03"):
		mm_end="Mar"
	elif(end_format[1]=="04"):
		mm_end="Apr"
	elif(end_format[1]=="05"):
		mm_end="May"
	elif(end_format[1]=="06" ):
		mm_end="Jun"
	elif(end_format[1]=="07" ):
		mm_end="Jul"
	elif(end_format[1]=="08"):
		mm_end="Aug"
	elif(end_format[1]=="09"):
		mm_end="Sep"

	final_start_date=dd_start + "-" + mm_start + "-" + yr_start # starting date according to format in json
	final_end_date=dd_end + "-" + mm_end + "-" + yr_end  # ending date according to format in json

	with open(json_file_path) as df:
		dataf=js.load(df)
	all_dates=[]
	for i in dataf["states_daily"]:
		if(i["status"]=="Confirmed"):  # We can use any of "Confirmed","Deceased"  or "Recovered" to store dates
			all_dates.append(i["date"])

	start_index= all_dates.index(final_start_date) # Finding the index which is used later 
	end_index= all_dates.index(final_end_date)

	confirmed_count=0
	recovered_count=0
	deceased_count=0
	
	confirmed_arr=[]             # Storing each days confirmed count which is later used to iterate based on date
	recovered_arr=[]			# Storing each days recovered count which is later used to iterate based on date
	deceased_arr=[]				 #Storing each days deceased count which is later used to iterate based on date

	for i in dataf["states_daily"]:       # Total cases(confirmed,deceased & recovered) for the state Delhi are stored in the variable "dl"
		if(i["status"]=="Confirmed"):
			confirmed_arr.append(int(i["dl"]))
		elif(i["status"]=="Recovered"):
			recovered_arr.append(int(i["dl"]))
		elif(i["status"]=="Deceased"):
			deceased_arr.append(int(i["dl"]))
	#print(confirmed_count)
	for i in range(start_index,end_index+1):   # Using the index to iterate over input dates(starting and ending)
		confirmed_count+=confirmed_arr[i]
		recovered_count+=recovered_arr[i]
		deceased_count+=deceased_arr[i]

	print('confirmed_count: ',confirmed_count, 'recovered_count:',recovered_count, 'deceased_count: ',deceased_count)

def Q1_3(json_file_path, start_date, end_date):
	start_format=start_date.split("-",3)
	end_format=end_date.split("-",3)
	
	dd_start=start_format[2] #starting date
	dd_end=end_format[2]
	
	mm_start=" " # starting month
	mm_end=" " # ending month
	
	yr_start="20" #starting year
	yr_end="20" #ending year

	if(start_format[1]=="03"):
		mm_start="Mar"
	elif(start_format[1]=="04"):
		mm_start="Apr"
	elif(start_format[1]=="05"):
		mm_start="May"
	elif(start_format[1]=="06" ):
		mm_start="Jun"
	elif(start_format[1]=="07" ):
		mm_start="Jul"
	elif(start_format[1]=="08"):
		mm_start="Aug"
	elif(start_format[1]=="09"):
		mm_start="Sep"
	
	if(end_format[1]=="03"):
		mm_end="Mar"
	elif(end_format[1]=="04"):
		mm_end="Apr"
	elif(end_format[1]=="05"):
		mm_end="May"
	elif(end_format[1]=="06" ):
		mm_end="Jun"
	elif(end_format[1]=="07" ):
		mm_end="Jul"
	elif(end_format[1]=="08"):
		mm_end="Aug"
	elif(end_format[1]=="09"):
		mm_end="Sep"

	final_start_date=dd_start + "-" + mm_start + "-" + yr_start # starting date according to format in json
	final_end_date=dd_end + "-" + mm_end + "-" + yr_end  # ending date according to format in json

	with open(json_file_path) as df:
		dataf=js.load(df)
	all_dates=[]
	for i in dataf["states_daily"]:
		if(i["status"]=="Confirmed"):  # We can use any of "Confirmed","Deceased"  or "Recovered" to store dates
			all_dates.append(i["date"])

	start_index= all_dates.index(final_start_date) # Finding the index which is used later 
	end_index= all_dates.index(final_end_date)

	confirmed_count=0
	recovered_count=0
	deceased_count=0
	
	confirmed_arr=[]             # Storing each days confirmed count which is later used to iterate based on date
	recovered_arr=[]			# Storing each days recovered count which is later used to iterate based on date
	deceased_arr=[]				 #Storing each days deceased count which is later used to iterate based on date

	for i in dataf["states_daily"]:       # Total cases(confirmed,deceased & recovered) for the state Delhi are stored in the variable "dl"
		if(i["status"]=="Confirmed"):     # and for Maharashtra, they are stored in the variable "mh"
			confirmed_arr.append(int(i["dl"]) + int(i["mh"]))
		elif(i["status"]=="Recovered"):
			recovered_arr.append(int(i["dl"]) + int(i["mh"]))
		elif(i["status"]=="Deceased"):
			deceased_arr.append(int(i["dl"]) + int(i["mh"]))
	#print(confirmed_count)
	for i in range(start_index,end_index+1):   # Using the index to iterate over input dates(starting and ending)
		confirmed_count+=confirmed_arr[i]
		recovered_count+=recovered_arr[i]
		deceased_count+=deceased_arr[i]

	print('confirmed_count: ',confirmed_count, 'recovered_count:',recovered_count, 'deceased_count: ',deceased_count)

def Q1_4(json_file_path, start_date, end_date):  # The variables "tt" and "un" are not included in states
	start_format=start_date.split("-",3)
	end_format=end_date.split("-",3)
	
	dd_start=start_format[2] #starting date
	dd_end=end_format[2]
	
	mm_start=" " # starting month
	mm_end=" " # ending month
	
	yr_start="20" #starting year
	yr_end="20" #ending year

	if(start_format[1]=="03"):
		mm_start="Mar"
	elif(start_format[1]=="04"):
		mm_start="Apr"
	elif(start_format[1]=="05"):
		mm_start="May"
	elif(start_format[1]=="06" ):
		mm_start="Jun"
	elif(start_format[1]=="07" ):
		mm_start="Jul"
	elif(start_format[1]=="08"):
		mm_start="Aug"
	elif(start_format[1]=="09"):
		mm_start="Sep"
	
	if(end_format[1]=="03"):
		mm_end="Mar"
	elif(end_format[1]=="04"):
		mm_end="Apr"
	elif(end_format[1]=="05"):
		mm_end="May"
	elif(end_format[1]=="06" ):
		mm_end="Jun"
	elif(end_format[1]=="07" ):
		mm_end="Jul"
	elif(end_format[1]=="08"):
		mm_end="Aug"
	elif(end_format[1]=="09"):
		mm_end="Sep"

	final_start_date=dd_start + "-" + mm_start + "-" + yr_start # starting date according to format in json
	final_end_date=dd_end + "-" + mm_end + "-" + yr_end  # ending date according to format in json

	with open(json_file_path) as df:
		dataf=js.load(df)
	all_dates=[]
	for i in dataf["states_daily"]:
		if(i["status"]=="Confirmed"):  # We can use any of "Confirmed","Deceased"  or "Recovered" to store dates
			all_dates.append(i["date"])

	start_index= all_dates.index(final_start_date) # Finding the index which is used later 
	end_index= all_dates.index(final_end_date)

	#states_arr=["an","ap","ar","as","br","ch","ct","dd","dl","dn","ga","gj","hp","hr","jh","jk","ka","kl","la","ld",
	#		"mh","ml","mn","mp","mz","nl","or","pb","py","rj","sk","tg","tn","tr","up","ut","wb"]
	count_an_confirmed , count_ap_confirmed , count_ar_confirmed , count_as_confirmed , count_br_confirmed, count_ch_confirmed=0,0,0,0,0,0
	count_ct_confirmed , count_dd_confirmed , count_dl_confirmed , count_dn_confirmed , count_ga_confirmed, count_gj_confirmed=0,0,0,0,0,0
	count_hp_confirmed , count_hr_confirmed , count_jh_confirmed , count_jk_confirmed , count_ka_confirmed, count_kl_confirmed=0,0,0,0,0,0
	count_la_confirmed , count_ld_confirmed , count_mh_confirmed , count_ml_confirmed , count_mn_confirmed, count_mp_confirmed=0,0,0,0,0,0
	count_mz_confirmed , count_nl_confirmed , count_or_confirmed , count_pb_confirmed , count_py_confirmed, count_rj_confirmed=0,0,0,0,0,0
	count_sk_confirmed , count_tg_confirmed , count_tn_confirmed , count_tr_confirmed , count_up_confirmed, count_ut_confirmed=0,0,0,0,0,0
	count_wb_confirmed=0


	count_an_recovered , count_ap_recovered , count_ar_recovered , count_as_recovered , count_br_recovered, count_ch_recovered=0,0,0,0,0,0
	count_ct_recovered , count_dd_recovered , count_dl_recovered , count_dn_recovered , count_ga_recovered, count_gj_recovered=0,0,0,0,0,0
	count_hp_recovered , count_hr_recovered , count_jh_recovered , count_jk_recovered , count_ka_recovered, count_kl_recovered=0,0,0,0,0,0
	count_la_recovered , count_ld_recovered , count_mh_recovered , count_ml_recovered , count_mn_recovered, count_mp_recovered=0,0,0,0,0,0
	count_mz_recovered , count_nl_recovered , count_or_recovered , count_pb_recovered , count_py_recovered, count_rj_recovered=0,0,0,0,0,0
	count_sk_recovered , count_tg_recovered , count_tn_recovered , count_tr_recovered , count_up_recovered, count_ut_recovered=0,0,0,0,0,0
	count_wb_recovered=0
	
	count_an_deceased , count_ap_deceased , count_ar_deceased , count_as_deceased , count_br_deceased , count_ch_deceased=0,0,0,0,0,0
	count_ct_deceased , count_dd_deceased , count_dl_deceased , count_dn_deceased , count_ga_deceased , count_gj_deceased=0,0,0,0,0,0
	count_hp_deceased , count_hr_deceased , count_jh_deceased , count_jk_deceased , count_ka_deceased , count_kl_deceased=0,0,0,0,0,0
	count_la_deceased , count_ld_deceased , count_mh_deceased , count_ml_deceased , count_mn_deceased , count_mp_deceased=0,0,0,0,0,0
	count_mz_deceased , count_nl_deceased , count_or_deceased , count_pb_deceased , count_py_deceased , count_rj_deceased=0,0,0,0,0,0
	count_sk_deceased , count_tg_deceased , count_tn_deceased , count_tr_deceased , count_up_deceased , count_ut_deceased=0,0,0,0,0,0
	count_wb_deceased=0

	for j in range(start_index,3*(end_index)+3):  # Instead of creating a separate array[which will increase the length of the program],the code runs till 3*(end_index) + 3 to include all the three: confirmed,recovered and deceased
		#										  # This is different from the above 3 parts[ creating an array for each state will be redundant], that is the reason for using "count"
		if(dataf["states_daily"][j]["status"]=="Confirmed"):
			temp_x=dataf["states_daily"][j]
			count_an_confirmed+=int(temp_x["an"])
			count_ap_confirmed+=int(temp_x["ap"])
			count_ar_confirmed+=int(temp_x["ar"]) 
			count_as_confirmed+=int(temp_x["as"])
			count_br_confirmed+=int(temp_x["br"])
			count_ch_confirmed+=int(temp_x["ch"])
			count_ct_confirmed+=int(temp_x["ct"]) 
			count_dd_confirmed+=int(temp_x["dd"]) 
			count_dl_confirmed+=int(temp_x["dl"])
			count_dn_confirmed+=int(temp_x["dn"])
			count_ga_confirmed+=int(temp_x["ga"])
			count_gj_confirmed+=int(temp_x["gj"])
			count_hp_confirmed+=int(temp_x["hp"])
			count_hr_confirmed+=int(temp_x["hr"])
			count_jh_confirmed+=int(temp_x["jh"]) 
			count_jk_confirmed+=int(temp_x["jk"]) 
			count_ka_confirmed+=int(temp_x["ka"])
			count_kl_confirmed+=int(temp_x["kl"])
			count_la_confirmed+=int(temp_x["la"])
			count_ld_confirmed+=int(temp_x["ld"]) 
			count_mh_confirmed+=int(temp_x["mh"])
			count_ml_confirmed+=int(temp_x["ml"]) 
			count_mn_confirmed+=int(temp_x["mn"])
			count_mp_confirmed+=int(temp_x["mp"])
			count_mz_confirmed+=int(temp_x["mz"])
			count_nl_confirmed+=int(temp_x["nl"])
			count_or_confirmed+=int(temp_x["or"]) 
			count_pb_confirmed+=int(temp_x["pb"]) 
			count_py_confirmed+=int(temp_x["py"]) 
			count_rj_confirmed+=int(temp_x["rj"])
			count_sk_confirmed+=int(temp_x["sk"])
			count_tg_confirmed+=int(temp_x["tg"]) 
			count_tn_confirmed+=int(temp_x["tn"]) 
			count_tr_confirmed+=int(temp_x["tr"]) 
			count_up_confirmed+=int(temp_x["up"])
			count_ut_confirmed+=int(temp_x["ut"])
			count_wb_confirmed+=int(temp_x["wb"])
		elif(dataf["states_daily"][j]["status"]=="Recovered"):
			temp_x=dataf["states_daily"][j]
			count_an_recovered+=int(temp_x["an"])
			count_ap_recovered+=int(temp_x["ap"])
			count_ar_recovered+=int(temp_x["ar"]) 
			count_as_recovered+=int(temp_x["as"])
			count_br_recovered+=int(temp_x["br"])
			count_ch_recovered+=int(temp_x["ch"])
			count_ct_recovered+=int(temp_x["ct"]) 
			count_dd_recovered+=int(temp_x["dd"]) 
			count_dl_recovered+=int(temp_x["dl"])
			count_dn_recovered+=int(temp_x["dn"])
			count_ga_recovered+=int(temp_x["ga"])
			count_gj_recovered+=int(temp_x["gj"])
			count_hp_recovered+=int(temp_x["hp"])
			count_hr_recovered+=int(temp_x["hr"])
			count_jh_recovered+=int(temp_x["jh"]) 
			count_jk_recovered+=int(temp_x["jk"]) 
			count_ka_recovered+=int(temp_x["ka"])
			count_kl_recovered+=int(temp_x["kl"])
			count_la_recovered+=int(temp_x["la"])
			count_ld_recovered+=int(temp_x["ld"]) 
			count_mh_recovered+=int(temp_x["mh"])
			count_ml_recovered+=int(temp_x["ml"]) 
			count_mn_recovered+=int(temp_x["mn"])
			count_mp_recovered+=int(temp_x["mp"])
			count_mz_recovered+=int(temp_x["mz"])
			count_nl_recovered+=int(temp_x["nl"])
			count_or_recovered+=int(temp_x["or"]) 
			count_pb_recovered+=int(temp_x["pb"]) 
			count_py_recovered+=int(temp_x["py"]) 
			count_rj_recovered+=int(temp_x["rj"])
			count_sk_recovered+=int(temp_x["sk"])
			count_tg_recovered+=int(temp_x["tg"]) 
			count_tn_recovered+=int(temp_x["tn"]) 
			count_tr_recovered+=int(temp_x["tr"]) 
			count_up_recovered+=int(temp_x["up"])
			count_ut_recovered+=int(temp_x["ut"])
			count_wb_recovered+=int(temp_x["wb"])
		elif(dataf["states_daily"][j]["status"]=="Deceased"):
			temp_x=dataf["states_daily"][j]
			count_an_deceased+=int(temp_x["an"])
			count_ap_deceased+=int(temp_x["ap"])
			count_ar_deceased+=int(temp_x["ar"]) 
			count_as_deceased+=int(temp_x["as"])
			count_br_deceased+=int(temp_x["br"])
			count_ch_deceased+=int(temp_x["ch"])
			count_ct_deceased+=int(temp_x["ct"]) 
			count_dd_deceased+=int(temp_x["dd"]) 
			count_dl_deceased+=int(temp_x["dl"])
			count_dn_deceased+=int(temp_x["dn"])
			count_ga_deceased+=int(temp_x["ga"])
			count_gj_deceased+=int(temp_x["gj"])
			count_hp_deceased+=int(temp_x["hp"])
			count_hr_deceased+=int(temp_x["hr"])
			count_jh_deceased+=int(temp_x["jh"]) 
			count_jk_deceased+=int(temp_x["jk"]) 
			count_ka_deceased+=int(temp_x["ka"])
			count_kl_deceased+=int(temp_x["kl"])
			count_la_deceased+=int(temp_x["la"])
			count_ld_deceased+=int(temp_x["ld"]) 
			count_mh_deceased+=int(temp_x["mh"])
			count_ml_deceased+=int(temp_x["ml"]) 
			count_mn_deceased+=int(temp_x["mn"])
			count_mp_deceased+=int(temp_x["mp"])
			count_mz_deceased+=int(temp_x["mz"])
			count_nl_deceased+=int(temp_x["nl"])
			count_or_deceased+=int(temp_x["or"]) 
			count_pb_deceased+=int(temp_x["pb"]) 
			count_py_deceased+=int(temp_x["py"]) 
			count_rj_deceased+=int(temp_x["rj"])
			count_sk_deceased+=int(temp_x["sk"])
			count_tg_deceased+=int(temp_x["tg"]) 
			count_tn_deceased+=int(temp_x["tn"]) 
			count_tr_deceased+=int(temp_x["tr"]) 
			count_up_deceased+=int(temp_x["up"])
			count_ut_deceased+=int(temp_x["ut"])
			count_wb_deceased+=int(temp_x["wb"])

	# Creating arrays for each of confirmed,recovered and deceased cases which will be used for mapping in the global states_arr
	states_confirmed=[count_an_confirmed , count_ap_confirmed , count_ar_confirmed , count_as_confirmed , count_br_confirmed, count_ch_confirmed,
					  count_ct_confirmed , count_dd_confirmed , count_dl_confirmed , count_dn_confirmed , count_ga_confirmed, count_gj_confirmed,
					  count_hp_confirmed , count_hr_confirmed , count_jh_confirmed , count_jk_confirmed , count_ka_confirmed, count_kl_confirmed,
					  count_la_confirmed , count_ld_confirmed , count_mh_confirmed , count_ml_confirmed , count_mn_confirmed, count_mp_confirmed,
					  count_mz_confirmed , count_nl_confirmed , count_or_confirmed , count_pb_confirmed , count_py_confirmed, count_rj_confirmed,
					  count_sk_confirmed , count_tg_confirmed , count_tn_confirmed , count_tr_confirmed , count_up_confirmed, count_ut_confirmed,
					  count_wb_confirmed]
	
	states_recovered = [count_an_recovered , count_ap_recovered , count_ar_recovered , count_as_recovered , count_br_recovered, count_ch_recovered,
					  count_ct_recovered, count_dd_recovered , count_dl_recovered , count_dn_recovered , count_ga_recovered, count_gj_recovered,
					  count_hp_recovered , count_hr_recovered , count_jh_recovered , count_jk_recovered , count_ka_recovered, count_kl_recovered,
					  count_la_recovered , count_ld_recovered , count_mh_recovered , count_ml_recovered , count_mn_recovered, count_mp_recovered,
					  count_mz_recovered , count_nl_recovered , count_or_recovered , count_pb_recovered , count_py_recovered, count_rj_recovered,
					  count_sk_recovered , count_tg_recovered , count_tn_recovered , count_tr_recovered , count_up_recovered, count_ut_recovered,
					  count_wb_recovered] 

	states_deceased= [count_an_deceased , count_ap_deceased , count_ar_deceased , count_as_deceased , count_br_deceased, count_ch_deceased,
					  count_ct_deceased, count_dd_deceased , count_dl_deceased , count_dn_deceased , count_ga_deceased, count_gj_deceased,
					  count_hp_deceased , count_hr_deceased , count_jh_deceased , count_jk_deceased , count_ka_deceased, count_kl_deceased,
					  count_la_deceased , count_ld_deceased , count_mh_deceased , count_ml_deceased , count_mn_deceased, count_mp_deceased,
					  count_mz_deceased , count_nl_deceased , count_or_deceased , count_pb_deceased , count_py_deceased, count_rj_deceased,
					  count_sk_deceased , count_tg_deceased , count_tn_deceased , count_tr_deceased , count_up_deceased, count_ut_deceased,
					  count_wb_deceased]
	# In case of more than one maximum [confirmed,recovered,deceased] , report all such states with their counts.
	max_confirmed_index=[]
	max_confirmed_value=max(states_confirmed)
	index_c=0
	for i in range(len(states_confirmed)):
		if(states_confirmed[i]==max_confirmed_value):
			max_confirmed_index.append(index_c)
		index_c+=1
	
	state_code_confirmed=[]         # The array has been created to handle the case where there will be multiple values
	for i in max_confirmed_index:
		state_code_confirmed.append(states_arr[i])

	#print(max_confirmed_value)

	max_recovered_index=[]
	max_recovered_value=max(states_recovered)
	index_r=0
	for i in range(len(states_recovered)):
		if(states_recovered[i]==max_recovered_value):
			max_recovered_index.append(index_r)
		index_r+=1

	state_code_recovered=[]
	for i in max_recovered_index:
		state_code_recovered.append(states_arr[i])

	#print(max_recovered_value)

	max_deceased_index=[]
	max_deceased_value=max(states_deceased)
	index_d=0
	for i in range(len(states_deceased)):
		if(states_deceased[i]==max_deceased_value):
			max_deceased_index.append(index_d)
		index_d+=1
	
	state_code_deceased=[]         # The array has been created to handle the case where there will be multiple values
	for i in max_deceased_index:
		state_code_deceased.append(states_arr[i])
	#print(state_code_deceased)
	#print(max_deceased_value)



	print('Confirmed \n')
	print('Highest affected State is/are: ' + str(state_code_confirmed))
	print('Highest affected State count is: ' + str(max_confirmed_value))
	print('Recovered \n')
	print('Highest affected State is/are: ' + str(state_code_recovered))
	print('Highest affected State count is: ' + str(max_recovered_value))
	print('Deceased \n')
	print('Highest affected State is/are: ' + str(state_code_deceased))
	print('Highest affected State count is: ' + str(max_deceased_value))

def Q1_5(json_file_path, start_date, end_date):
	start_format=start_date.split("-",3)
	end_format=end_date.split("-",3)
	
	dd_start=start_format[2] #starting date
	dd_end=end_format[2]
	
	mm_start=" " # starting month
	mm_end=" " # ending month
	
	yr_start="20" #starting year
	yr_end="20" #ending year

	if(start_format[1]=="03"):
		mm_start="Mar"
	elif(start_format[1]=="04"):
		mm_start="Apr"
	elif(start_format[1]=="05"):
		mm_start="May"
	elif(start_format[1]=="06" ):
		mm_start="Jun"
	elif(start_format[1]=="07" ):
		mm_start="Jul"
	elif(start_format[1]=="08"):
		mm_start="Aug"
	elif(start_format[1]=="09"):
		mm_start="Sep"
	
	if(end_format[1]=="03"):
		mm_end="Mar"
	elif(end_format[1]=="04"):
		mm_end="Apr"
	elif(end_format[1]=="05"):
		mm_end="May"
	elif(end_format[1]=="06" ):
		mm_end="Jun"
	elif(end_format[1]=="07" ):
		mm_end="Jul"
	elif(end_format[1]=="08"):
		mm_end="Aug"
	elif(end_format[1]=="09"):
		mm_end="Sep"

	final_start_date=dd_start + "-" + mm_start + "-" + yr_start # starting date according to format in json
	final_end_date=dd_end + "-" + mm_end + "-" + yr_end  # ending date according to format in json

	with open(json_file_path) as df:
		dataf=js.load(df)
	all_dates=[]
	for i in dataf["states_daily"]:
		if(i["status"]=="Confirmed"):  # We can use any of "Confirmed","Deceased"  or "Recovered" to store dates
			all_dates.append(i["date"])

	start_index= all_dates.index(final_start_date) # Finding the index which is used later 
	end_index= all_dates.index(final_end_date)

	#states_arr=["an","ap","ar","as","br","ch","ct","dd","dl","dn","ga","gj","hp","hr","jh","jk","ka","kl","la","ld",
	#		"mh","ml","mn","mp","mz","nl","or","pb","py","rj","sk","tg","tn","tr","up","ut","wb"]
	count_an_confirmed , count_ap_confirmed , count_ar_confirmed , count_as_confirmed , count_br_confirmed, count_ch_confirmed=0,0,0,0,0,0
	count_ct_confirmed , count_dd_confirmed , count_dl_confirmed , count_dn_confirmed , count_ga_confirmed, count_gj_confirmed=0,0,0,0,0,0
	count_hp_confirmed , count_hr_confirmed , count_jh_confirmed , count_jk_confirmed , count_ka_confirmed, count_kl_confirmed=0,0,0,0,0,0
	count_la_confirmed , count_ld_confirmed , count_mh_confirmed , count_ml_confirmed , count_mn_confirmed, count_mp_confirmed=0,0,0,0,0,0
	count_mz_confirmed , count_nl_confirmed , count_or_confirmed , count_pb_confirmed , count_py_confirmed, count_rj_confirmed=0,0,0,0,0,0
	count_sk_confirmed , count_tg_confirmed , count_tn_confirmed , count_tr_confirmed , count_up_confirmed, count_ut_confirmed=0,0,0,0,0,0
	count_wb_confirmed=0


	count_an_recovered , count_ap_recovered , count_ar_recovered , count_as_recovered , count_br_recovered, count_ch_recovered=0,0,0,0,0,0
	count_ct_recovered , count_dd_recovered , count_dl_recovered , count_dn_recovered , count_ga_recovered, count_gj_recovered=0,0,0,0,0,0
	count_hp_recovered , count_hr_recovered , count_jh_recovered , count_jk_recovered , count_ka_recovered, count_kl_recovered=0,0,0,0,0,0
	count_la_recovered , count_ld_recovered , count_mh_recovered , count_ml_recovered , count_mn_recovered, count_mp_recovered=0,0,0,0,0,0
	count_mz_recovered , count_nl_recovered , count_or_recovered , count_pb_recovered , count_py_recovered, count_rj_recovered=0,0,0,0,0,0
	count_sk_recovered , count_tg_recovered , count_tn_recovered , count_tr_recovered , count_up_recovered, count_ut_recovered=0,0,0,0,0,0
	count_wb_recovered=0
	
	count_an_deceased , count_ap_deceased , count_ar_deceased , count_as_deceased , count_br_deceased , count_ch_deceased=0,0,0,0,0,0
	count_ct_deceased , count_dd_deceased , count_dl_deceased , count_dn_deceased , count_ga_deceased , count_gj_deceased=0,0,0,0,0,0
	count_hp_deceased , count_hr_deceased , count_jh_deceased , count_jk_deceased , count_ka_deceased , count_kl_deceased=0,0,0,0,0,0
	count_la_deceased , count_ld_deceased , count_mh_deceased , count_ml_deceased , count_mn_deceased , count_mp_deceased=0,0,0,0,0,0
	count_mz_deceased , count_nl_deceased , count_or_deceased , count_pb_deceased , count_py_deceased , count_rj_deceased=0,0,0,0,0,0
	count_sk_deceased , count_tg_deceased , count_tn_deceased , count_tr_deceased , count_up_deceased , count_ut_deceased=0,0,0,0,0,0
	count_wb_deceased=0

	for j in range(start_index,3*(end_index)+3):  # Instead of creating a separate array[which will increase the length of the program],the code runs till 3*(end_index) + 3 to include all the three: confirmed,recovered and deceased
		#										  # This is different from the above 3 parts[ creating an array for each state will be redundant], that is the reason for using "count"
		if(dataf["states_daily"][j]["status"]=="Confirmed"):
			temp_x=dataf["states_daily"][j]
			count_an_confirmed+=int(temp_x["an"])
			count_ap_confirmed+=int(temp_x["ap"])
			count_ar_confirmed+=int(temp_x["ar"]) 
			count_as_confirmed+=int(temp_x["as"])
			count_br_confirmed+=int(temp_x["br"])
			count_ch_confirmed+=int(temp_x["ch"])
			count_ct_confirmed+=int(temp_x["ct"]) 
			count_dd_confirmed+=int(temp_x["dd"]) 
			count_dl_confirmed+=int(temp_x["dl"])
			count_dn_confirmed+=int(temp_x["dn"])
			count_ga_confirmed+=int(temp_x["ga"])
			count_gj_confirmed+=int(temp_x["gj"])
			count_hp_confirmed+=int(temp_x["hp"])
			count_hr_confirmed+=int(temp_x["hr"])
			count_jh_confirmed+=int(temp_x["jh"]) 
			count_jk_confirmed+=int(temp_x["jk"]) 
			count_ka_confirmed+=int(temp_x["ka"])
			count_kl_confirmed+=int(temp_x["kl"])
			count_la_confirmed+=int(temp_x["la"])
			count_ld_confirmed+=int(temp_x["ld"]) 
			count_mh_confirmed+=int(temp_x["mh"])
			count_ml_confirmed+=int(temp_x["ml"]) 
			count_mn_confirmed+=int(temp_x["mn"])
			count_mp_confirmed+=int(temp_x["mp"])
			count_mz_confirmed+=int(temp_x["mz"])
			count_nl_confirmed+=int(temp_x["nl"])
			count_or_confirmed+=int(temp_x["or"]) 
			count_pb_confirmed+=int(temp_x["pb"]) 
			count_py_confirmed+=int(temp_x["py"]) 
			count_rj_confirmed+=int(temp_x["rj"])
			count_sk_confirmed+=int(temp_x["sk"])
			count_tg_confirmed+=int(temp_x["tg"]) 
			count_tn_confirmed+=int(temp_x["tn"]) 
			count_tr_confirmed+=int(temp_x["tr"]) 
			count_up_confirmed+=int(temp_x["up"])
			count_ut_confirmed+=int(temp_x["ut"])
			count_wb_confirmed+=int(temp_x["wb"])
		elif(dataf["states_daily"][j]["status"]=="Recovered"):
			temp_x=dataf["states_daily"][j]
			count_an_recovered+=int(temp_x["an"])
			count_ap_recovered+=int(temp_x["ap"])
			count_ar_recovered+=int(temp_x["ar"]) 
			count_as_recovered+=int(temp_x["as"])
			count_br_recovered+=int(temp_x["br"])
			count_ch_recovered+=int(temp_x["ch"])
			count_ct_recovered+=int(temp_x["ct"]) 
			count_dd_recovered+=int(temp_x["dd"]) 
			count_dl_recovered+=int(temp_x["dl"])
			count_dn_recovered+=int(temp_x["dn"])
			count_ga_recovered+=int(temp_x["ga"])
			count_gj_recovered+=int(temp_x["gj"])
			count_hp_recovered+=int(temp_x["hp"])
			count_hr_recovered+=int(temp_x["hr"])
			count_jh_recovered+=int(temp_x["jh"]) 
			count_jk_recovered+=int(temp_x["jk"]) 
			count_ka_recovered+=int(temp_x["ka"])
			count_kl_recovered+=int(temp_x["kl"])
			count_la_recovered+=int(temp_x["la"])
			count_ld_recovered+=int(temp_x["ld"]) 
			count_mh_recovered+=int(temp_x["mh"])
			count_ml_recovered+=int(temp_x["ml"]) 
			count_mn_recovered+=int(temp_x["mn"])
			count_mp_recovered+=int(temp_x["mp"])
			count_mz_recovered+=int(temp_x["mz"])
			count_nl_recovered+=int(temp_x["nl"])
			count_or_recovered+=int(temp_x["or"]) 
			count_pb_recovered+=int(temp_x["pb"]) 
			count_py_recovered+=int(temp_x["py"]) 
			count_rj_recovered+=int(temp_x["rj"])
			count_sk_recovered+=int(temp_x["sk"])
			count_tg_recovered+=int(temp_x["tg"]) 
			count_tn_recovered+=int(temp_x["tn"]) 
			count_tr_recovered+=int(temp_x["tr"]) 
			count_up_recovered+=int(temp_x["up"])
			count_ut_recovered+=int(temp_x["ut"])
			count_wb_recovered+=int(temp_x["wb"])
		elif(dataf["states_daily"][j]["status"]=="Deceased"):
			temp_x=dataf["states_daily"][j]
			count_an_deceased+=int(temp_x["an"])
			count_ap_deceased+=int(temp_x["ap"])
			count_ar_deceased+=int(temp_x["ar"]) 
			count_as_deceased+=int(temp_x["as"])
			count_br_deceased+=int(temp_x["br"])
			count_ch_deceased+=int(temp_x["ch"])
			count_ct_deceased+=int(temp_x["ct"]) 
			count_dd_deceased+=int(temp_x["dd"]) 
			count_dl_deceased+=int(temp_x["dl"])
			count_dn_deceased+=int(temp_x["dn"])
			count_ga_deceased+=int(temp_x["ga"])
			count_gj_deceased+=int(temp_x["gj"])
			count_hp_deceased+=int(temp_x["hp"])
			count_hr_deceased+=int(temp_x["hr"])
			count_jh_deceased+=int(temp_x["jh"]) 
			count_jk_deceased+=int(temp_x["jk"]) 
			count_ka_deceased+=int(temp_x["ka"])
			count_kl_deceased+=int(temp_x["kl"])
			count_la_deceased+=int(temp_x["la"])
			count_ld_deceased+=int(temp_x["ld"]) 
			count_mh_deceased+=int(temp_x["mh"])
			count_ml_deceased+=int(temp_x["ml"]) 
			count_mn_deceased+=int(temp_x["mn"])
			count_mp_deceased+=int(temp_x["mp"])
			count_mz_deceased+=int(temp_x["mz"])
			count_nl_deceased+=int(temp_x["nl"])
			count_or_deceased+=int(temp_x["or"]) 
			count_pb_deceased+=int(temp_x["pb"]) 
			count_py_deceased+=int(temp_x["py"]) 
			count_rj_deceased+=int(temp_x["rj"])
			count_sk_deceased+=int(temp_x["sk"])
			count_tg_deceased+=int(temp_x["tg"]) 
			count_tn_deceased+=int(temp_x["tn"]) 
			count_tr_deceased+=int(temp_x["tr"]) 
			count_up_deceased+=int(temp_x["up"])
			count_ut_deceased+=int(temp_x["ut"])
			count_wb_deceased+=int(temp_x["wb"])

	# Creating arrays for each of confirmed,recovered and deceased cases which will be used for mapping in the global states_arr
	states_confirmed=[count_an_confirmed , count_ap_confirmed , count_ar_confirmed , count_as_confirmed , count_br_confirmed, count_ch_confirmed,
					  count_ct_confirmed , count_dd_confirmed , count_dl_confirmed , count_dn_confirmed , count_ga_confirmed, count_gj_confirmed,
					  count_hp_confirmed , count_hr_confirmed , count_jh_confirmed , count_jk_confirmed , count_ka_confirmed, count_kl_confirmed,
					  count_la_confirmed , count_ld_confirmed , count_mh_confirmed , count_ml_confirmed , count_mn_confirmed, count_mp_confirmed,
					  count_mz_confirmed , count_nl_confirmed , count_or_confirmed , count_pb_confirmed , count_py_confirmed, count_rj_confirmed,
					  count_sk_confirmed , count_tg_confirmed , count_tn_confirmed , count_tr_confirmed , count_up_confirmed, count_ut_confirmed,
					  count_wb_confirmed]
	
	states_recovered = [count_an_recovered , count_ap_recovered , count_ar_recovered , count_as_recovered , count_br_recovered, count_ch_recovered,
					  count_ct_recovered, count_dd_recovered , count_dl_recovered , count_dn_recovered , count_ga_recovered, count_gj_recovered,
					  count_hp_recovered , count_hr_recovered , count_jh_recovered , count_jk_recovered , count_ka_recovered, count_kl_recovered,
					  count_la_recovered , count_ld_recovered , count_mh_recovered , count_ml_recovered , count_mn_recovered, count_mp_recovered,
					  count_mz_recovered , count_nl_recovered , count_or_recovered , count_pb_recovered , count_py_recovered, count_rj_recovered,
					  count_sk_recovered , count_tg_recovered , count_tn_recovered , count_tr_recovered , count_up_recovered, count_ut_recovered,
					  count_wb_recovered] 

	states_deceased= [count_an_deceased , count_ap_deceased , count_ar_deceased , count_as_deceased , count_br_deceased, count_ch_deceased,
					  count_ct_deceased, count_dd_deceased , count_dl_deceased , count_dn_deceased , count_ga_deceased, count_gj_deceased,
					  count_hp_deceased , count_hr_deceased , count_jh_deceased , count_jk_deceased , count_ka_deceased, count_kl_deceased,
					  count_la_deceased , count_ld_deceased , count_mh_deceased , count_ml_deceased , count_mn_deceased, count_mp_deceased,
					  count_mz_deceased , count_nl_deceased , count_or_deceased , count_pb_deceased , count_py_deceased, count_rj_deceased,
					  count_sk_deceased , count_tg_deceased , count_tn_deceased , count_tr_deceased , count_up_deceased, count_ut_deceased,
					  count_wb_deceased]
	# In case of more than one maximum [confirmed,recovered,deceased] , report all such states with their counts.
	min_confirmed_index=[]
	min_confirmed_value=min(states_confirmed)
	index_c=0
	for i in range(len(states_confirmed)):
		if(states_confirmed[i]==min_confirmed_value):
			min_confirmed_index.append(index_c)
		index_c+=1
	
	state_code_confirmed=[]         # The array has been created to handle the case where there will be multiple values
	for i in min_confirmed_index:
		state_code_confirmed.append(states_arr[i])

	#print(max_confirmed_value)

	min_recovered_index=[]
	min_recovered_value=min(states_recovered)
	index_r=0
	for i in range(len(states_recovered)):
		if(states_recovered[i]==min_recovered_value):
			min_recovered_index.append(index_r)
		index_r+=1

	state_code_recovered=[]
	for i in min_recovered_index:
		state_code_recovered.append(states_arr[i])


	min_deceased_index=[]
	min_deceased_value=min(states_deceased)
	index_d=0
	for i in range(len(states_deceased)):
		if(states_deceased[i]==min_deceased_value):
			min_deceased_index.append(index_d)
		index_d+=1
	
	state_code_deceased=[]         # The array has been created to handle the case where there will be multiple values
	for i in min_deceased_index:
		state_code_deceased.append(states_arr[i])



	print("\n")
	print('Confirmed \n')
	print('Lowest affected State is: ' + str(state_code_confirmed))
	print('Lowest affected State count is: ' + str(min_confirmed_value))
	print("\n")
	print('Recovered \n')
	print('Lowest affected State is: ' + str(state_code_recovered))
	print('Lowest affected State count is: ' + str(min_recovered_value))
	print("\n")
	print('Deceased \n')
	print('Lowest affected State is: ' + str(state_code_deceased))
	print('Lowest affected State count is: ' + str(min_deceased_value))

def Q1_6(json_file_path, start_date, end_date):
	start_format=start_date.split("-",3)
	end_format=end_date.split("-",3)
	
	dd_start=start_format[2] #starting date
	dd_end=end_format[2]
	
	mm_start=" " # starting month
	mm_end=" " # ending month
	
	yr_start="20" #starting year
	yr_end="20" #ending year

	if(start_format[1]=="03"):
		mm_start="Mar"
	elif(start_format[1]=="04"):
		mm_start="Apr"
	elif(start_format[1]=="05"):
		mm_start="May"
	elif(start_format[1]=="06" ):
		mm_start="Jun"
	elif(start_format[1]=="07" ):
		mm_start="Jul"
	elif(start_format[1]=="08"):
		mm_start="Aug"
	elif(start_format[1]=="09"):
		mm_start="Sep"
	
	if(end_format[1]=="03"):
		mm_end="Mar"
	elif(end_format[1]=="04"):
		mm_end="Apr"
	elif(end_format[1]=="05"):
		mm_end="May"
	elif(end_format[1]=="06" ):
		mm_end="Jun"
	elif(end_format[1]=="07" ):
		mm_end="Jul"
	elif(end_format[1]=="08"):
		mm_end="Aug"
	elif(end_format[1]=="09"):
		mm_end="Sep"

	final_start_date=dd_start + "-" + mm_start + "-" + yr_start # starting date according to format in json
	final_end_date=dd_end + "-" + mm_end + "-" + yr_end  # ending date according to format in json

	with open(json_file_path) as df:
		dataf=js.load(df)
	all_dates=[]
	for i in dataf["states_daily"]:
		if(i["status"]=="Confirmed"):  # We can use any of "Confirmed","Deceased"  or "Recovered" to store dates
			all_dates.append(i["date"])

	start_index= all_dates.index(final_start_date) # Finding the index which is used later 
	end_index= all_dates.index(final_end_date)
	
	confirmed_arr=[]             # Storing each days confirmed count which is later used to iterate based on date
	recovered_arr=[]			# Storing each days recovered count which is later used to iterate based on date
	deceased_arr=[]				 #Storing each days deceased count which is later used to iterate based on date

	for i in dataf["states_daily"]:       # Total cases(confirmed,deceased & recovered) for the state Delhi are stored in the variable "dl"
		if(i["status"]=="Confirmed"):
			confirmed_arr.append(int(i["dl"]))
		elif(i["status"]=="Recovered"):
			recovered_arr.append(int(i["dl"]))
		elif(i["status"]=="Deceased"):
			deceased_arr.append(int(i["dl"]))

	new_confirmed_arr=[]    # Holding count for the range of dates which are given as input.
	new_recovered_arr=[]	
	new_deceased_arr=[]
	new_dates=[]
	for i in range(start_index,end_index+1):
		new_confirmed_arr.append(confirmed_arr[i])
		new_recovered_arr.append(recovered_arr[i])
		new_deceased_arr.append(deceased_arr[i])
		new_dates.append(all_dates[i])

	Highest_spike_confirmed_count=max(new_confirmed_arr)
	Highest_spike_recovered_count=max(new_recovered_arr)
	#print(Highest_spike_recovered_count)
	Highest_spike_deceased_count=max(new_deceased_arr)
	#print(Highest_spike_deceased_count)
	#print(len(new_confirmed_arr))
	#print(len(new_recovered_arr))
	#print(len(new_deceased_arr))

	index_max_confirmed = 0      # Storing indexes corresponding to maximum value
	index_max_recovered = 0
	index_max_deceased = 0

	for i in range(len(new_confirmed_arr)):
		if(new_confirmed_arr[i]==Highest_spike_confirmed_count):
			index_max_confirmed=i
			#print(index_max_confirmed)
	for j in range(len(new_recovered_arr)):
		if(new_recovered_arr[j]==Highest_spike_recovered_count):
			index_max_recovered=j
			#print(index_max_recovered)
	for k in range(len(new_recovered_arr)):
		if(new_deceased_arr[k]==Highest_spike_deceased_count):
			index_max_deceased=k
			#print(index_max_deceased)

	Highest_spike_confirmed_day= new_dates[index_max_confirmed]      # Using the index to find the corresponding date
	Highest_spike_recovered_day= new_dates[index_max_recovered]
	Highest_spike_deceased_day= new_dates[index_max_deceased]
	
	print("\n")
	print('Confirmed \n')
	print('Day: ',Highest_spike_confirmed_day)
	print('Count: ',Highest_spike_confirmed_count)
	print("\n")
	print('Recovered \n')
	print('Day: ',Highest_spike_recovered_day)
	print('Count: ',Highest_spike_recovered_count)
	print("\n")
	print('Deceased \n')
	print('Day: ',Highest_spike_deceased_day)
	print('Count: ',Highest_spike_deceased_count)

def Q1_7(json_file_path, start_date, end_date):
	start_format=start_date.split("-",3)
	end_format=end_date.split("-",3)
	
	dd_start=start_format[2] #starting date
	dd_end=end_format[2]
	
	mm_start=" " # starting month
	mm_end=" " # ending month
	
	yr_start="20" #starting year
	yr_end="20" #ending year

	if(start_format[1]=="03"):
		mm_start="Mar"
	elif(start_format[1]=="04"):
		mm_start="Apr"
	elif(start_format[1]=="05"):
		mm_start="May"
	elif(start_format[1]=="06" ):
		mm_start="Jun"
	elif(start_format[1]=="07" ):
		mm_start="Jul"
	elif(start_format[1]=="08"):
		mm_start="Aug"
	elif(start_format[1]=="09"):
		mm_start="Sep"
	
	if(end_format[1]=="03"):
		mm_end="Mar"
	elif(end_format[1]=="04"):
		mm_end="Apr"
	elif(end_format[1]=="05"):
		mm_end="May"
	elif(end_format[1]=="06" ):
		mm_end="Jun"
	elif(end_format[1]=="07" ):
		mm_end="Jul"
	elif(end_format[1]=="08"):
		mm_end="Aug"
	elif(end_format[1]=="09"):
		mm_end="Sep"

	final_start_date=dd_start + "-" + mm_start + "-" + yr_start # starting date according to format in json
	final_end_date=dd_end + "-" + mm_end + "-" + yr_end  # ending date according to format in json

	with open(json_file_path) as df:
		dataf=js.load(df)
	all_dates=[]
	for i in dataf["states_daily"]:
		if(i["status"]=="Confirmed"):  # We can use any of "Confirmed","Deceased"  or "Recovered" to store dates
			all_dates.append(i["date"])

	start_index= all_dates.index(final_start_date) # Finding the index which is used later 
	end_index= all_dates.index(final_end_date)

	#states_arr=["an","ap","ar","as","br","ch","ct","dd","dl","dn","ga","gj","hp","hr","jh","jk","ka","kl","la","ld",
	#		"mh","ml","mn","mp","mz","nl","or","pb","py","rj","sk","tg","tn","tr","up","ut","wb"]
	count_an_confirmed , count_ap_confirmed , count_ar_confirmed , count_as_confirmed , count_br_confirmed, count_ch_confirmed=0,0,0,0,0,0
	count_ct_confirmed , count_dd_confirmed , count_dl_confirmed , count_dn_confirmed , count_ga_confirmed, count_gj_confirmed=0,0,0,0,0,0
	count_hp_confirmed , count_hr_confirmed , count_jh_confirmed , count_jk_confirmed , count_ka_confirmed, count_kl_confirmed=0,0,0,0,0,0
	count_la_confirmed , count_ld_confirmed , count_mh_confirmed , count_ml_confirmed , count_mn_confirmed, count_mp_confirmed=0,0,0,0,0,0
	count_mz_confirmed , count_nl_confirmed , count_or_confirmed , count_pb_confirmed , count_py_confirmed, count_rj_confirmed=0,0,0,0,0,0
	count_sk_confirmed , count_tg_confirmed , count_tn_confirmed , count_tr_confirmed , count_up_confirmed, count_ut_confirmed=0,0,0,0,0,0
	count_wb_confirmed=0


	count_an_recovered , count_ap_recovered , count_ar_recovered , count_as_recovered , count_br_recovered, count_ch_recovered=0,0,0,0,0,0
	count_ct_recovered , count_dd_recovered , count_dl_recovered , count_dn_recovered , count_ga_recovered, count_gj_recovered=0,0,0,0,0,0
	count_hp_recovered , count_hr_recovered , count_jh_recovered , count_jk_recovered , count_ka_recovered, count_kl_recovered=0,0,0,0,0,0
	count_la_recovered , count_ld_recovered , count_mh_recovered , count_ml_recovered , count_mn_recovered, count_mp_recovered=0,0,0,0,0,0
	count_mz_recovered , count_nl_recovered , count_or_recovered , count_pb_recovered , count_py_recovered, count_rj_recovered=0,0,0,0,0,0
	count_sk_recovered , count_tg_recovered , count_tn_recovered , count_tr_recovered , count_up_recovered, count_ut_recovered=0,0,0,0,0,0
	count_wb_recovered=0
	
	count_an_deceased , count_ap_deceased , count_ar_deceased , count_as_deceased , count_br_deceased , count_ch_deceased=0,0,0,0,0,0
	count_ct_deceased , count_dd_deceased , count_dl_deceased , count_dn_deceased , count_ga_deceased , count_gj_deceased=0,0,0,0,0,0
	count_hp_deceased , count_hr_deceased , count_jh_deceased , count_jk_deceased , count_ka_deceased , count_kl_deceased=0,0,0,0,0,0
	count_la_deceased , count_ld_deceased , count_mh_deceased , count_ml_deceased , count_mn_deceased , count_mp_deceased=0,0,0,0,0,0
	count_mz_deceased , count_nl_deceased , count_or_deceased , count_pb_deceased , count_py_deceased , count_rj_deceased=0,0,0,0,0,0
	count_sk_deceased , count_tg_deceased , count_tn_deceased , count_tr_deceased , count_up_deceased , count_ut_deceased=0,0,0,0,0,0
	count_wb_deceased=0

	for j in range(start_index,3*(end_index)+3):  # Instead of creating a separate array[which will increase the length of the program],the code runs till 3*(end_index) + 3 to include all the three: confirmed,recovered and deceased
		#										  # This is different from the above 3 parts[ creating an array for each state will be redundant], that is the reason for using "count"
		if(dataf["states_daily"][j]["status"]=="Confirmed"):
			temp_x=dataf["states_daily"][j]
			count_an_confirmed+=int(temp_x["an"])
			count_ap_confirmed+=int(temp_x["ap"])
			count_ar_confirmed+=int(temp_x["ar"]) 
			count_as_confirmed+=int(temp_x["as"])
			count_br_confirmed+=int(temp_x["br"])
			count_ch_confirmed+=int(temp_x["ch"])
			count_ct_confirmed+=int(temp_x["ct"]) 
			count_dd_confirmed+=int(temp_x["dd"]) 
			count_dl_confirmed+=int(temp_x["dl"])
			count_dn_confirmed+=int(temp_x["dn"])
			count_ga_confirmed+=int(temp_x["ga"])
			count_gj_confirmed+=int(temp_x["gj"])
			count_hp_confirmed+=int(temp_x["hp"])
			count_hr_confirmed+=int(temp_x["hr"])
			count_jh_confirmed+=int(temp_x["jh"]) 
			count_jk_confirmed+=int(temp_x["jk"]) 
			count_ka_confirmed+=int(temp_x["ka"])
			count_kl_confirmed+=int(temp_x["kl"])
			count_la_confirmed+=int(temp_x["la"])
			count_ld_confirmed+=int(temp_x["ld"]) 
			count_mh_confirmed+=int(temp_x["mh"])
			count_ml_confirmed+=int(temp_x["ml"]) 
			count_mn_confirmed+=int(temp_x["mn"])
			count_mp_confirmed+=int(temp_x["mp"])
			count_mz_confirmed+=int(temp_x["mz"])
			count_nl_confirmed+=int(temp_x["nl"])
			count_or_confirmed+=int(temp_x["or"]) 
			count_pb_confirmed+=int(temp_x["pb"]) 
			count_py_confirmed+=int(temp_x["py"]) 
			count_rj_confirmed+=int(temp_x["rj"])
			count_sk_confirmed+=int(temp_x["sk"])
			count_tg_confirmed+=int(temp_x["tg"]) 
			count_tn_confirmed+=int(temp_x["tn"]) 
			count_tr_confirmed+=int(temp_x["tr"]) 
			count_up_confirmed+=int(temp_x["up"])
			count_ut_confirmed+=int(temp_x["ut"])
			count_wb_confirmed+=int(temp_x["wb"])
		elif(dataf["states_daily"][j]["status"]=="Recovered"):
			temp_x=dataf["states_daily"][j]
			count_an_recovered+=int(temp_x["an"])
			count_ap_recovered+=int(temp_x["ap"])
			count_ar_recovered+=int(temp_x["ar"]) 
			count_as_recovered+=int(temp_x["as"])
			count_br_recovered+=int(temp_x["br"])
			count_ch_recovered+=int(temp_x["ch"])
			count_ct_recovered+=int(temp_x["ct"]) 
			count_dd_recovered+=int(temp_x["dd"]) 
			count_dl_recovered+=int(temp_x["dl"])
			count_dn_recovered+=int(temp_x["dn"])
			count_ga_recovered+=int(temp_x["ga"])
			count_gj_recovered+=int(temp_x["gj"])
			count_hp_recovered+=int(temp_x["hp"])
			count_hr_recovered+=int(temp_x["hr"])
			count_jh_recovered+=int(temp_x["jh"]) 
			count_jk_recovered+=int(temp_x["jk"]) 
			count_ka_recovered+=int(temp_x["ka"])
			count_kl_recovered+=int(temp_x["kl"])
			count_la_recovered+=int(temp_x["la"])
			count_ld_recovered+=int(temp_x["ld"]) 
			count_mh_recovered+=int(temp_x["mh"])
			count_ml_recovered+=int(temp_x["ml"]) 
			count_mn_recovered+=int(temp_x["mn"])
			count_mp_recovered+=int(temp_x["mp"])
			count_mz_recovered+=int(temp_x["mz"])
			count_nl_recovered+=int(temp_x["nl"])
			count_or_recovered+=int(temp_x["or"]) 
			count_pb_recovered+=int(temp_x["pb"]) 
			count_py_recovered+=int(temp_x["py"]) 
			count_rj_recovered+=int(temp_x["rj"])
			count_sk_recovered+=int(temp_x["sk"])
			count_tg_recovered+=int(temp_x["tg"]) 
			count_tn_recovered+=int(temp_x["tn"]) 
			count_tr_recovered+=int(temp_x["tr"]) 
			count_up_recovered+=int(temp_x["up"])
			count_ut_recovered+=int(temp_x["ut"])
			count_wb_recovered+=int(temp_x["wb"])
		elif(dataf["states_daily"][j]["status"]=="Deceased"):
			temp_x=dataf["states_daily"][j]
			count_an_deceased+=int(temp_x["an"])
			count_ap_deceased+=int(temp_x["ap"])
			count_ar_deceased+=int(temp_x["ar"]) 
			count_as_deceased+=int(temp_x["as"])
			count_br_deceased+=int(temp_x["br"])
			count_ch_deceased+=int(temp_x["ch"])
			count_ct_deceased+=int(temp_x["ct"]) 
			count_dd_deceased+=int(temp_x["dd"]) 
			count_dl_deceased+=int(temp_x["dl"])
			count_dn_deceased+=int(temp_x["dn"])
			count_ga_deceased+=int(temp_x["ga"])
			count_gj_deceased+=int(temp_x["gj"])
			count_hp_deceased+=int(temp_x["hp"])
			count_hr_deceased+=int(temp_x["hr"])
			count_jh_deceased+=int(temp_x["jh"]) 
			count_jk_deceased+=int(temp_x["jk"]) 
			count_ka_deceased+=int(temp_x["ka"])
			count_kl_deceased+=int(temp_x["kl"])
			count_la_deceased+=int(temp_x["la"])
			count_ld_deceased+=int(temp_x["ld"]) 
			count_mh_deceased+=int(temp_x["mh"])
			count_ml_deceased+=int(temp_x["ml"]) 
			count_mn_deceased+=int(temp_x["mn"])
			count_mp_deceased+=int(temp_x["mp"])
			count_mz_deceased+=int(temp_x["mz"])
			count_nl_deceased+=int(temp_x["nl"])
			count_or_deceased+=int(temp_x["or"]) 
			count_pb_deceased+=int(temp_x["pb"]) 
			count_py_deceased+=int(temp_x["py"]) 
			count_rj_deceased+=int(temp_x["rj"])
			count_sk_deceased+=int(temp_x["sk"])
			count_tg_deceased+=int(temp_x["tg"]) 
			count_tn_deceased+=int(temp_x["tn"]) 
			count_tr_deceased+=int(temp_x["tr"]) 
			count_up_deceased+=int(temp_x["up"])
			count_ut_deceased+=int(temp_x["ut"])
			count_wb_deceased+=int(temp_x["wb"])

	# Creating arrays for each of confirmed,recovered and deceased cases which will be used for mapping in the global states_arr
	states_confirmed=[count_an_confirmed , count_ap_confirmed , count_ar_confirmed , count_as_confirmed , count_br_confirmed, count_ch_confirmed,
					  count_ct_confirmed , count_dd_confirmed , count_dl_confirmed , count_dn_confirmed , count_ga_confirmed, count_gj_confirmed,
					  count_hp_confirmed , count_hr_confirmed , count_jh_confirmed , count_jk_confirmed , count_ka_confirmed, count_kl_confirmed,
					  count_la_confirmed , count_ld_confirmed , count_mh_confirmed , count_ml_confirmed , count_mn_confirmed, count_mp_confirmed,
					  count_mz_confirmed , count_nl_confirmed , count_or_confirmed , count_pb_confirmed , count_py_confirmed, count_rj_confirmed,
					  count_sk_confirmed , count_tg_confirmed , count_tn_confirmed , count_tr_confirmed , count_up_confirmed, count_ut_confirmed,
					  count_wb_confirmed]
	
	states_recovered = [count_an_recovered , count_ap_recovered , count_ar_recovered , count_as_recovered , count_br_recovered, count_ch_recovered,
					  count_ct_recovered, count_dd_recovered , count_dl_recovered , count_dn_recovered , count_ga_recovered, count_gj_recovered,
					  count_hp_recovered , count_hr_recovered , count_jh_recovered , count_jk_recovered , count_ka_recovered, count_kl_recovered,
					  count_la_recovered , count_ld_recovered , count_mh_recovered , count_ml_recovered , count_mn_recovered, count_mp_recovered,
					  count_mz_recovered , count_nl_recovered , count_or_recovered , count_pb_recovered , count_py_recovered, count_rj_recovered,
					  count_sk_recovered , count_tg_recovered , count_tn_recovered , count_tr_recovered , count_up_recovered, count_ut_recovered,
					  count_wb_recovered] 

	states_deceased= [count_an_deceased , count_ap_deceased , count_ar_deceased , count_as_deceased , count_br_deceased, count_ch_deceased,
					  count_ct_deceased, count_dd_deceased , count_dl_deceased , count_dn_deceased , count_ga_deceased, count_gj_deceased,
					  count_hp_deceased , count_hr_deceased , count_jh_deceased , count_jk_deceased , count_ka_deceased, count_kl_deceased,
					  count_la_deceased , count_ld_deceased , count_mh_deceased , count_ml_deceased , count_mn_deceased, count_mp_deceased,
					  count_mz_deceased , count_nl_deceased , count_or_deceased , count_pb_deceased , count_py_deceased, count_rj_deceased,
					  count_sk_deceased , count_tg_deceased , count_tn_deceased , count_tr_deceased , count_up_deceased, count_ut_deceased,
					  count_wb_deceased]

	active_cases=[] # This array will contain the state by state active cases tally
	for i in range(len(states_confirmed)):
		active_cases.append(states_confirmed[i] - (states_recovered[i] + states_deceased[i]))

	print("State by State active cases are given as follows:")
	for i in range(len(active_cases)):
		print("State name: " + states_arr[i] + " " + "Active cases: " + str(active_cases[i]))

def Q2_1(json_file_path, start_date, end_date):
	# Take cumulative values
	start_format=start_date.split("-",3)
	end_format=end_date.split("-",3)
	
	dd_start=start_format[2] #starting date
	dd_end=end_format[2]
	
	mm_start=" " # starting month
	mm_end=" " # ending month
	
	yr_start="20" #starting year
	yr_end="20" #ending year

	if(start_format[1]=="03"):
		mm_start="Mar"
	elif(start_format[1]=="04"):
		mm_start="Apr"
	elif(start_format[1]=="05"):
		mm_start="May"
	elif(start_format[1]=="06" ):
		mm_start="Jun"
	elif(start_format[1]=="07" ):
		mm_start="Jul"
	elif(start_format[1]=="08"):
		mm_start="Aug"
	elif(start_format[1]=="09"):
		mm_start="Sep"
	
	if(end_format[1]=="03"):
		mm_end="Mar"
	elif(end_format[1]=="04"):
		mm_end="Apr"
	elif(end_format[1]=="05"):
		mm_end="May"
	elif(end_format[1]=="06" ):
		mm_end="Jun"
	elif(end_format[1]=="07" ):
		mm_end="Jul"
	elif(end_format[1]=="08"):
		mm_end="Aug"
	elif(end_format[1]=="09"):
		mm_end="Sep"

	final_start_date=dd_start + "-" + mm_start + "-" + yr_start # starting date according to format in json
	final_end_date=dd_end + "-" + mm_end + "-" + yr_end  # ending date according to format in json

	with open(json_file_path) as df:
		dataf=js.load(df)
	all_dates=[]
	for i in dataf["states_daily"]:
		if(i["status"]=="Confirmed"):  # We can use any of "Confirmed","Deceased"  or "Recovered" to store dates
			all_dates.append(i["date"])

	start_index= all_dates.index(final_start_date) # Finding the index which is used later 
	end_index= all_dates.index(final_end_date)

	confirmed_values=[]
	recovered_values=[]
	deceased_values=[]
	for j in range(start_index,3*(end_index)+3):  										  
		if(dataf["states_daily"][j]["status"]=="Confirmed"):
			temp_x=dataf["states_daily"][j]
			for i in range(len(states_arr)):
				confirmed_values.append(int(temp_x[states_arr[i]]))
		elif(dataf["states_daily"][j]["status"]=="Recovered"):
			temp_x=dataf["states_daily"][j]
			for i in range(len(states_arr)):
				recovered_values.append(int(temp_x[states_arr[i]]))
		elif(dataf["states_daily"][j]["status"]=="Deceased"):
			temp_x=dataf["states_daily"][j]
			for i in range(len(states_arr)):
				deceased_values.append(int(temp_x[states_arr[i]]))

	dates_in_range=all_dates[start_index:end_index+1]   # All the dates in given range of dates. This is used for plotting
	individual_confirmed_values = []
	individual_recovered_values = []
	individual_deceased_values = []
	#print(confirmed_values[0:37])
	for i in range(0,len(confirmed_values),37):         # 37 is the total number of states[states+ ut included]
		sum_confirmed=0
		sum_confirmed=sum(confirmed_values[i:i+37])
		sum_recovered=0
		sum_recovered=sum(recovered_values[i:i+37])
		sum_deceased=0
		sum_deceased=sum(deceased_values[i:i+37])
		individual_confirmed_values.append(sum_confirmed)
		individual_recovered_values.append(sum_recovered)
		individual_deceased_values.append(sum_deceased)
	
	cumulative_confirmed_values=[]                    #storing cumulative values starting from start_date i.e 
	cumulative_recovered_values=[]					  # considering start_date as the 1st date
	cumulative_deceased_values=[]
	c=0
	r=0
	d=0
	for i in range(len(individual_confirmed_values)):
		c+=individual_confirmed_values[i]
		r+=individual_recovered_values[i]
		d+=individual_deceased_values[i]
		cumulative_confirmed_values.append(c)
		cumulative_recovered_values.append(r)
		cumulative_deceased_values.append(d)

	# For plots
	plot_values = {"Confirmed":cumulative_confirmed_values, "Recovered": cumulative_recovered_values, "Deceased":cumulative_deceased_values}
	plot_dates=dates_in_range
	data_frame=pd.DataFrame(plot_values,index=plot_dates)
	data_frame.plot(kind='area',stacked=False)
	plt.xlabel('Dates')
	plt.ylabel('Number of cases')
	plt.show()

def Q2_2(json_file_path, start_date, end_date):
	start_format=start_date.split("-",3)
	end_format=end_date.split("-",3)
	
	dd_start=start_format[2] #starting date
	dd_end=end_format[2]
	
	mm_start=" " # starting month
	mm_end=" " # ending month
	
	yr_start="20" #starting year
	yr_end="20" #ending year

	if(start_format[1]=="03"):
		mm_start="Mar"
	elif(start_format[1]=="04"):
		mm_start="Apr"
	elif(start_format[1]=="05"):
		mm_start="May"
	elif(start_format[1]=="06" ):
		mm_start="Jun"
	elif(start_format[1]=="07" ):
		mm_start="Jul"
	elif(start_format[1]=="08"):
		mm_start="Aug"
	elif(start_format[1]=="09"):
		mm_start="Sep"
	
	if(end_format[1]=="03"):
		mm_end="Mar"
	elif(end_format[1]=="04"):
		mm_end="Apr"
	elif(end_format[1]=="05"):
		mm_end="May"
	elif(end_format[1]=="06" ):
		mm_end="Jun"
	elif(end_format[1]=="07" ):
		mm_end="Jul"
	elif(end_format[1]=="08"):
		mm_end="Aug"
	elif(end_format[1]=="09"):
		mm_end="Sep"

	final_start_date=dd_start + "-" + mm_start + "-" + yr_start # starting date according to format in json
	final_end_date=dd_end + "-" + mm_end + "-" + yr_end  # ending date according to format in json

	with open(json_file_path) as df:
		dataf=js.load(df)
	all_dates=[]
	for i in dataf["states_daily"]:
		if(i["status"]=="Confirmed"):  # We can use any of "Confirmed","Deceased"  or "Recovered" to store dates
			all_dates.append(i["date"])

	start_index= all_dates.index(final_start_date) # Finding the index which is used later 
	end_index= all_dates.index(final_end_date)
	
	confirmed_arr=[]             # Storing each days confirmed count which is later used to iterate based on date
	recovered_arr=[]			# Storing each days recovered count which is later used to iterate based on date
	deceased_arr=[]				 #Storing each days deceased count which is later used to iterate based on date

	for i in dataf["states_daily"]:       # Total cases(confirmed,deceased & recovered) for the state Delhi are stored in the variable "dl"
		if(i["status"]=="Confirmed"):
			confirmed_arr.append(int(i["dl"]))
		elif(i["status"]=="Recovered"):
			recovered_arr.append(int(i["dl"]))
		elif(i["status"]=="Deceased"):
			deceased_arr.append(int(i["dl"]))

	new_confirmed_arr=[]    # Holding count for the range of dates which are given as input.
	new_recovered_arr=[]	
	new_deceased_arr=[]
	new_dates=[]
	for i in range(start_index,end_index+1):
		new_confirmed_arr.append(confirmed_arr[i])
		new_recovered_arr.append(recovered_arr[i])
		new_deceased_arr.append(deceased_arr[i])
		new_dates.append(all_dates[i])

	cumulative_confirmed_values=[]                    #storing cumulative values starting from start_date i.e 
	cumulative_recovered_values=[]					  # considering start_date as the 1st date
	cumulative_deceased_values=[]
	c=0
	r=0
	d=0
	for i in range(len(new_confirmed_arr)):
		c+=new_confirmed_arr[i]
		r+=new_recovered_arr[i]
		d+=new_deceased_arr[i]
		cumulative_confirmed_values.append(c)
		cumulative_recovered_values.append(r)
		cumulative_deceased_values.append(d)
	
	plot_values = {"Confirmed":cumulative_confirmed_values, "Recovered": cumulative_recovered_values, "Deceased":cumulative_deceased_values}
	plot_dates=new_dates
	data_frame=pd.DataFrame(plot_values,index=plot_dates)
	data_frame.plot(kind='area',stacked=False)
	plt.xlabel('Dates')
	plt.ylabel('Number of cases for Delhi')
	plt.show()

def Q2_3(json_file_path, start_date, end_date):
	start_format=start_date.split("-",3)
	end_format=end_date.split("-",3)
	
	dd_start=start_format[2] #starting date
	dd_end=end_format[2]
	
	mm_start=" " # starting month
	mm_end=" " # ending month
	
	yr_start="20" #starting year
	yr_end="20" #ending year

	if(start_format[1]=="03"):
		mm_start="Mar"
	elif(start_format[1]=="04"):
		mm_start="Apr"
	elif(start_format[1]=="05"):
		mm_start="May"
	elif(start_format[1]=="06" ):
		mm_start="Jun"
	elif(start_format[1]=="07" ):
		mm_start="Jul"
	elif(start_format[1]=="08"):
		mm_start="Aug"
	elif(start_format[1]=="09"):
		mm_start="Sep"
	
	if(end_format[1]=="03"):
		mm_end="Mar"
	elif(end_format[1]=="04"):
		mm_end="Apr"
	elif(end_format[1]=="05"):
		mm_end="May"
	elif(end_format[1]=="06" ):
		mm_end="Jun"
	elif(end_format[1]=="07" ):
		mm_end="Jul"
	elif(end_format[1]=="08"):
		mm_end="Aug"
	elif(end_format[1]=="09"):
		mm_end="Sep"

	final_start_date=dd_start + "-" + mm_start + "-" + yr_start # starting date according to format in json
	final_end_date=dd_end + "-" + mm_end + "-" + yr_end  # ending date according to format in json

	with open(json_file_path) as df:
		dataf=js.load(df)
	all_dates=[]
	for i in dataf["states_daily"]:
		if(i["status"]=="Confirmed"):  # We can use any of "Confirmed","Deceased"  or "Recovered" to store dates
			all_dates.append(i["date"])

	start_index= all_dates.index(final_start_date) # Finding the index which is used later 
	end_index= all_dates.index(final_end_date)

	confirmed_values=[]
	recovered_values=[]
	deceased_values=[]
	for j in range(start_index,3*(end_index)+3):  										  
		if(dataf["states_daily"][j]["status"]=="Confirmed"):
			temp_x=dataf["states_daily"][j]
			for i in range(len(states_arr)):
				confirmed_values.append(int(temp_x[states_arr[i]]))
		elif(dataf["states_daily"][j]["status"]=="Recovered"):
			temp_x=dataf["states_daily"][j]
			for i in range(len(states_arr)):
				recovered_values.append(int(temp_x[states_arr[i]]))
		elif(dataf["states_daily"][j]["status"]=="Deceased"):
			temp_x=dataf["states_daily"][j]
			for i in range(len(states_arr)):
				deceased_values.append(int(temp_x[states_arr[i]]))

	dates_in_range=all_dates[start_index:end_index+1]   # All the dates in given range of dates. This is used for plotting
	individual_confirmed_values = []
	individual_recovered_values = []
	individual_deceased_values = []
	#print(confirmed_values[0:37])
	for i in range(0,len(confirmed_values),37):         # 37 is the total number of states[states+ ut included]
		sum_confirmed=0
		sum_confirmed=sum(confirmed_values[i:i+37])
		sum_recovered=0
		sum_recovered=sum(recovered_values[i:i+37])
		sum_deceased=0
		sum_deceased=sum(deceased_values[i:i+37])
		individual_confirmed_values.append(sum_confirmed)
		individual_recovered_values.append(sum_recovered)
		individual_deceased_values.append(sum_deceased)

	individual_active_values=[]
	for i in range(len(individual_confirmed_values)):
		individual_active_values.append(individual_confirmed_values[i] - (individual_recovered_values[i]+individual_deceased_values[i]))

	a=0
	cumulative_active_values=[]
	for i in range(len(individual_active_values)):
		a+=individual_active_values[i]
		cumulative_active_values.append(a)

	plot_values = {"Active cases" : cumulative_active_values}
	plot_dates=dates_in_range
	data_frame=pd.DataFrame(plot_values,index=plot_dates)
	data_frame.plot(kind='area',stacked=False)
	plt.xlabel('Dates')
	plt.ylabel('Number of Active cases')
	plt.show()

def Q3(json_file_path, start_date, end_date):
	start_format=start_date.split("-",3)
	end_format=end_date.split("-",3)
	
	dd_start=start_format[2] #starting date
	dd_end=end_format[2]
	
	mm_start=" " # starting month
	mm_end=" " # ending month
	
	yr_start="20" #starting year
	yr_end="20" #ending year

	if(start_format[1]=="03"):
		mm_start="Mar"
	elif(start_format[1]=="04"):
		mm_start="Apr"
	elif(start_format[1]=="05"):
		mm_start="May"
	elif(start_format[1]=="06" ):
		mm_start="Jun"
	elif(start_format[1]=="07" ):
		mm_start="Jul"
	elif(start_format[1]=="08"):
		mm_start="Aug"
	elif(start_format[1]=="09"):
		mm_start="Sep"
	
	if(end_format[1]=="03"):
		mm_end="Mar"
	elif(end_format[1]=="04"):
		mm_end="Apr"
	elif(end_format[1]=="05"):
		mm_end="May"
	elif(end_format[1]=="06" ):
		mm_end="Jun"
	elif(end_format[1]=="07" ):
		mm_end="Jul"
	elif(end_format[1]=="08"):
		mm_end="Aug"
	elif(end_format[1]=="09"):
		mm_end="Sep"

	final_start_date=dd_start + "-" + mm_start + "-" + yr_start # starting date according to format in json
	final_end_date=dd_end + "-" + mm_end + "-" + yr_end  # ending date according to format in json

	with open(json_file_path) as df:
		dataf=js.load(df)
	all_dates=[]
	for i in dataf["states_daily"]:
		if(i["status"]=="Confirmed"):  # We can use any of "Confirmed","Deceased"  or "Recovered" to store dates
			all_dates.append(i["date"])

	start_index= all_dates.index(final_start_date) # Finding the index which is used later 
	end_index= all_dates.index(final_end_date)
	
	confirmed_arr=[]             # Storing each days confirmed count which is later used to iterate based on date
	recovered_arr=[]			# Storing each days recovered count which is later used to iterate based on date
	deceased_arr=[]				 #Storing each days deceased count which is later used to iterate based on date

	for i in dataf["states_daily"]:       # Total cases(confirmed,deceased & recovered) for the state Delhi are stored in the variable "dl"
		if(i["status"]=="Confirmed"):
			confirmed_arr.append(int(i["dl"]))
		elif(i["status"]=="Recovered"):
			recovered_arr.append(int(i["dl"]))
		elif(i["status"]=="Deceased"):
			deceased_arr.append(int(i["dl"]))

	new_confirmed_arr=[]    # Holding count for the range of dates which are given as input.
	new_recovered_arr=[]	
	new_deceased_arr=[]
	new_dates=[]
	for i in range(start_index,end_index+1):
		new_confirmed_arr.append(confirmed_arr[i])
		new_recovered_arr.append(recovered_arr[i])
		new_deceased_arr.append(deceased_arr[i])
		new_dates.append(all_dates[i])

	#Since dates are not numeric, hence dates will be represented through integers
	# For eg. 14th March is represented as 1 , 15th March as 2 and so on.

	dates_for_regression = []
	date_num=0
	for i in range(len(new_dates)):
		date_num+=1
		dates_for_regression.append(date_num)
		#date_num+=1

	# Y-axis has cases(confirmed/recovered/deceased) and X-axis has dates/days
	# Linear regression line is given by :  y=mx + c [ m= slope and c= intercept]
	mean_confirmed_values= sum(new_confirmed_arr)/len(new_confirmed_arr)  # Y-axis
	mean_dates_values = sum(dates_for_regression)/len(dates_for_regression) # X-axis

	confirmed_slope = 0
	up_slope_confirmed=0
	down_slope_confirmed=0
	for i in range(len(new_confirmed_arr)):
		up_slope_confirmed+=((new_confirmed_arr[i] - mean_confirmed_values)*(dates_for_regression[i]- mean_dates_values))
		down_slope_confirmed+=(dates_for_regression[i]-mean_dates_values)*(dates_for_regression[i]-mean_dates_values)

	confirmed_slope = up_slope_confirmed/down_slope_confirmed
	confirmed_intercept = mean_confirmed_values - (confirmed_slope)*(mean_dates_values)

	#print(confirmed_slope)
	#print(confirmed_intercept)

	mean_recovered_values= sum(new_recovered_arr)/len(new_recovered_arr)  # Y-axis
	

	recovered_slope = 0
	up_slope_recovered=0
	down_slope_recovered=0
	for i in range(len(new_recovered_arr)):
		up_slope_recovered+=((new_recovered_arr[i] - mean_recovered_values)*(dates_for_regression[i]- mean_dates_values))
		down_slope_recovered+=(dates_for_regression[i]-mean_dates_values)*(dates_for_regression[i]-mean_dates_values)

	recovered_slope = up_slope_recovered/down_slope_recovered
	recovered_intercept = mean_recovered_values - (recovered_slope)*(mean_dates_values)

	#print(recovered_slope)
	#print(recovered_intercept)

	mean_deceased_values= sum(new_deceased_arr)/len(new_deceased_arr)

	deceased_slope = 0
	up_slope_deceased=0
	down_slope_deceased=0
	for i in range(len(new_deceased_arr)):
		up_slope_deceased+=((new_deceased_arr[i] - mean_deceased_values)*(dates_for_regression[i]- mean_dates_values))
		down_slope_deceased+=(dates_for_regression[i]-mean_dates_values)*(dates_for_regression[i]-mean_dates_values)

	deceased_slope = up_slope_deceased/down_slope_deceased
	deceased_intercept = mean_deceased_values - (deceased_slope)*(mean_dates_values)

	#print(deceased_slope)
	#print(deceased_intercept)

	print(confirmed_intercept, confirmed_slope, recovered_intercept,recovered_slope, deceased_intercept, deceased_slope)



if __name__ == "__main__":
	print('Your Roll number' + ":" + " 2017040 ") 
	#Handling dates
	start_date = "2020-03-14"
	end_date = "2020-09-05"
	if(start_date<"2020-03-14" or end_date>"2020-09-05"):
		print("Please enter valid date between 2020-03-14 and 2020-09-05")
	# To run all of these functions, keep the json file in the same directory as of this python script
	else:
		Q1_1('states_daily.json', start_date, end_date) 
		Q1_2('states_daily.json',start_date,end_date)
		Q1_3('states_daily.json',start_date,end_date)
		Q1_4('states_daily.json',start_date,end_date)
		Q1_5('states_daily.json',start_date,end_date)
		Q1_6('states_daily.json',start_date,end_date)
		Q1_7('states_daily.json',start_date,end_date)
		Q2_1('states_daily.json',start_date,end_date)
		Q2_2('states_daily.json',start_date,end_date)
		Q2_3('states_daily.json',start_date,end_date)
		Q3('states_daily.json',start_date,end_date)