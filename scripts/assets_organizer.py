import csv
import json

from pathlib import Path

data = {}

home = Path.home()
csv_path = Path(home, "Documents", "eleicoes-2022", "eleicoes-2022-data", "assets", "BRASIL.csv")
# print(csv_path)

with open(csv_path, newline='', encoding='latin1') as f:
    reader = csv.DictReader(f, delimiter=';')

    for row in reader:
        sq_candidato = row["SQ_CANDIDATO"]

        if sq_candidato in data:
            data[sq_candidato] = data[sq_candidato] + [row]
        else:
            data[sq_candidato] = [row]

# print(data["280001618036"][-1])

json_path = Path(home, "Documents", "eleicoes-2022", "eleicoes-2022-data", "assets", "BRASIL.json")

with open(json_path, 'w') as json_file:
  json.dump(data, json_file)