# Write Python3 code here
from django.shortcuts import render
import pandas as pd
import json

# Create your views here.
def Table(request):
	df = pd.read_csv("C:/Users/User/Desktop/internship_project/JanataWIFI/analytics_project/dashboard/templates/dataset/stock_market_data.csv")
	# df = pd.read_json("C:/Users/User/Desktop/internship_project/JanataWIFI/analytics_project/dashboard/templates/dataset/stock_market_data.json")
	# parsing the DataFrame in json format.
	json_records = df.reset_index().to_json(orient ='records')
	data = []
	data = json.loads(json_records)
	context = {'d': data}

	return render(request, 'table.html', context)
# def Table(request):
# 	response = requests.get('C:/Users/User/Desktop/internship_project/stock_market_data.json').json()
# 	return render(request, 'home.htm', {'response':response})