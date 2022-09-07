import csv
import json

from pathlib import Path

data = []
candidates = {}
vices = {}

home = Path.home()

json_path = Path(home, "Documents", "eleicoes-2022", "eleicoes-2022-data", "assets", "BRASIL.json")

with open(json_path, 'r') as f:
  assets = json.load(f)

# print(assets.keys())

csv_path = Path(home, "Documents", "eleicoes-2022", "eleicoes-2022-data", "data", "BRASIL.csv")

with open(csv_path, newline='', encoding='latin1') as f:
    reader = csv.DictReader(f, delimiter=';')

    for row in reader:
        sg_uf = row["SG_UF"]
        cd_cargo = str(row["CD_CARGO"])
        nr_candidato = str(row["NR_CANDIDATO"])
        sq_candidato = row["SQ_CANDIDATO"]

        candidate = row

        candidate["BS_CANDIDATO"] = assets.get(sq_candidato)
        candidate["BS_CANDIDATO"] = assets.get(sq_candidato)

        img_path = Path(home, "Documents", "eleicoes-2022", "eleicoes-2022-data", "imgs", "candidates", "{0}".format(sg_uf), "F{0}{1}_div.jpg".format(sg_uf, sq_candidato))
        
        if img_path.exists():
            candidate["IM_CANDIDATO"] = "https://raw.githubusercontent.com/alexsilva96dev/eleicoes-2022-data/main/imgs/candidates/{0}/F{0}{1}_div.jpg".format(sg_uf, sq_candidato)
        else:
            candidate["IM_CANDIDATO"] = "https://raw.githubusercontent.com/alexsilva96dev/eleicoes-2022-data/main/imgs/candidates/{0}/F{0}{1}_div.jpeg".format(sg_uf, sq_candidato)

        if sg_uf in vices:
            if cd_cargo in ["2", "4", "9", "10"]:
                if cd_cargo in vices[sg_uf]:
                    vices[sg_uf][cd_cargo][nr_candidato] = candidate
                else:
                    vices[sg_uf][cd_cargo] = { nr_candidato: candidate }
            else:
               data.append(candidate) 
        else:
            if cd_cargo in ["2", "4", "9", "10"]:
                vices[sg_uf] = { cd_cargo: { nr_candidato: candidate } }
            else:
                data.append(candidate)

# print(vices["BR"]["2"]["13"])
# print(vices["PA"]["10"].keys())

# json_path = Path(home, "Documents", "eleicoes-2022", "eleicoes-2022-data", "data", "BRASIL.json")

# with open(json_path, 'w') as json_file:
#   json.dump(data, json_file)