import numpy as np
import pandas as pd
#Перезаполнение базы данных

import re
from accessify import protected
import csv

#Рабочие
column_worker = ['Name', 'Surename', 'Patronomyc']
items_worker = [['Sesh','Real','Kent']]
newDF = pd.DataFrame(items_worker,columns=column_worker)
newDF.to_csv(r'workers.csv')
#Клиенты
column_clients = ['Name', 'Surename', 'Patronomyc', 'Street', 'House', 'Number']
items_clients = [['Sesh','Real','Kent','Puskina','Kolotuskina','+75673565676']]
newDF = pd.DataFrame(items_clients,columns=column_clients)
newDF.to_csv(r'clients.csv')
#Продукты
column_products = ['Name', 'Price', 'Producer', 'Measurment']
items_products = [['Pivo','228','PivoPetrsu','Литр']]
newDF = pd.DataFrame(items_products,columns=column_products)
newDF.to_csv(r'products.csv')
#Поставщик
column_couriers = ['Name', 'Surename', 'Patronomyc', 'Carriage size']
items_couriers = [['Sesh','Real','Kent', '50']]
newDF = pd.DataFrame(items_couriers,columns=column_couriers)
newDF.to_csv(r'couriers.csv')

#Доставки
shipment = ['Courier', 'The date', 'Product', 'Count', 'Client', 'Address']
items_worker = [['Никита Алексеенко Алексеевич','27.10.2000','Соль', '100000', 'Никита Алексеенко Алексеевич', 'Puskina Kolotuskina']]
newDF = pd.DataFrame(items_worker,columns=shipment)
newDF.to_csv(r'shipment.csv')
#Сделки
transaction = ['Seller', 'Client', 'The date', 'Product', 'Count', 'Price']
items_worker = [['Никита Алексеенко Алексеевич', 'Никита Алексеенко Алексеевич', '27.10.2000', 'Соль', '50', '100000']]
newDF = pd.DataFrame(items_worker,columns=transaction)
newDF.to_csv(r'transaction.csv')
#Склад
balance = ['Name','Producer','Amount','Measurment']
items_balance = [['Pivo', 'PivoPetrsu', '30', 'Литр']]
newDF = pd.DataFrame(items_balance, columns=balance)
newDF.to_csv(r'balance.csv')