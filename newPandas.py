import numpy as np
import pandas as pd
import sys
from PyQt5 import QtWidgets
import worker
import re
from accessify import protected
import csv

column_worker = ['Name', 'Surename', 'Patronomyc']
items_worker = [['Sesh','Real','Kent']]
newDF = pd.DataFrame(items_worker,columns=column_worker)
newDF.to_csv(r'workers.csv')

column_clients = ['Name', 'Surename', 'Patronomyc', 'Street', 'House', 'Number']
items_clients = [['Sesh','Real','Kent','Puskina','Kolotuskina','+75673565676']]
newDF = pd.DataFrame(items_clients,columns=column_clients)
newDF.to_csv(r'clients.csv')

column_products = ['Name', 'Price', 'Producer', 'Measurment']
items_products = [['Pivo','228','PivoPetrsu','10000']]
newDF = pd.DataFrame(items_products,columns=column_products)
newDF.to_csv(r'products.csv')

#FILENAME = "workers.csv"

#with open(FILENAME, "a", newline="") as file:
#    newdata = ["Михайлов", "Игорь", "Отчество"]
#    writer = csv.writer(file)
#    writer.writerow(newdata)
