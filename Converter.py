#Паттерн адаптер. Создать адаптер между несовместимыми данными
import csv
import json
import sys
#Класс конвертера, преобразовывает csv в JSON
class Converter():
    #На вход функции подается два пути, первый к существующему csv файлу, второй к создаваемму json файлу
    def ConvertCsvToJSON(self, path_csv, path_JSON):
        data = {}
        with open(path_csv, encoding='utf-8') as csvf:
            csvReader = csv.DictReader(csvf)

            for rows in csvReader:
                key = rows[""]
                data[key] = rows
        
        with open(path_JSON, 'w', encoding="utf-8") as jsonf:
            jsonf.write(json.dumps(data))
if len(sys.argv) > 2:
    Converter().ConvertCsvToJSON(sys.argv[1],sys.argv[2])