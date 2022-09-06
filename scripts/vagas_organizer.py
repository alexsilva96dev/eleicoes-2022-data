import csv
import json

from pathlib import Path

data = {}

home = Path.home()
csv_path = Path(home, "Documents", "eleicoes-2022", "eleicoes-2022-data", "vagas", "BRASIL.csv")
# print(csv_path)

with open(csv_path, newline='', encoding='latin1') as f:
    reader = csv.DictReader(f, delimiter=';')

    for row in reader:
        sg_uf = row["SG_UF"]
        cd_cargo = row["CD_CARGO"]
        qt_vagas = row["QT_VAGAS"]

        if sg_uf in data:
            data[sg_uf][cd_cargo] = qt_vagas
        else:
            data[sg_uf] = { cd_cargo: qt_vagas }

# print(data["PA"])

json_path = Path(home, "Documents", "eleicoes-2022", "eleicoes-2022-data", "vagas", "BRASIL.json")

with open(json_path, 'w') as json_file:
  json.dump(data, json_file)