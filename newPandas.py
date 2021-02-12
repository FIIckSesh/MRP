import numpy as np
import pandas as pd
import sys
from PyQt5 import QtWidgets
import worker
import re
from accessify import protected
import csv

column_names = ['Name', 'Surename', 'Patronomyc']
items = [['Sesh','Real','Kent']]
newDF = pd.DataFrame(items,columns=column_names)

newDF.to_csv(r'workers.csv')

newDF.to_csv(r'clients.csv')

#FILENAME = "workers.csv"

#with open(FILENAME, "a", newline="") as file:
#    newdata = ["Михайлов", "Игорь", "Отчество"]
#    writer = csv.writer(file)
#    writer.writerow(newdata)
