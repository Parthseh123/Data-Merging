from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import csv

file1 = './home_project/scraped_Data_of_bright_stars.csv'
file2 = './home_project/dwarf_stars.csv'

dataset_1 = []
dataset_2 = []

with open(file1,'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_1.append(row) # itterating through each row and adding data to the dataset_1 list (bright_stars.csv)

with open(file2,'r',encoding='utf8') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_2.append(row) # itterating through each row and adding data to the dataset_2 list (dwarf_stars.csv)

headers_1 = dataset_1[0]
headers_2 = dataset_2[0]
planet_data_1 = dataset_1[1:]
planet_data_2 = dataset_2[1:]

headers = headers_1 + headers_2

planet_data = []

for s in planet_data_1:
    planet_data.append(s)
for p in planet_data_2:
    planet_data.append(p)

with open("./home_project/total_stars_after_merging.csv",'w',encoding='utf8') as t:
    csvwriter = csv.writer(t)
    csvwriter.writerow(headers)   
    csvwriter.writerows(planet_data)
    
df = pd.read_csv('./home_project/total_stars_after_merging.csv')
df.tail(8)