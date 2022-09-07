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

json_path2 = Path(home, "Documents", "eleicoes-2022", "eleicoes-2022-data", "redes-sociais", "BRASIL2.json")

with open(json_path2, 'r') as f:
  social_networks = json.load(f)

# print(assets.keys())

csv_path = Path(home, "Documents", "eleicoes-2022", "eleicoes-2022-data", "data", "BRASIL.csv")

with open(csv_path, newline='', encoding='latin1') as f:
    reader = csv.DictReader(f, delimiter=';')

    for row in reader:
        sg_uf = row["SG_UF"]
        cd_cargo = str(row["CD_CARGO"])
        nr_candidato = str(row["NR_CANDIDATO"])
        sq_candidato = row["SQ_CANDIDATO"]
        ds_situacao_candidato = row["DS_SITUACAO_CANDIDATURA"]

        if ds_situacao_candidato != "INAPTO":
            candidate = row

            candidate["RS_CANDIDATO"] = social_networks.get(sq_candidato)
            candidate["BS_CANDIDATO"] = assets.get(sq_candidato)

            img_path = Path(home, "Documents", "eleicoes-2022", "eleicoes-2022-data", "imgs", "candidates", "{0}".format(sg_uf), "F{0}{1}_div.jpg".format(sg_uf, sq_candidato))
            
            if img_path.exists():
                candidate["IM_CANDIDATO"] = "https://raw.githubusercontent.com/alexsilva96dev/eleicoes-2022-data/main/imgs/candidates/{0}/F{0}{1}_div.jpg".format(sg_uf, sq_candidato)
            else:
                candidate["IM_CANDIDATO"] = "https://raw.githubusercontent.com/alexsilva96dev/eleicoes-2022-data/main/imgs/candidates/{0}/F{0}{1}_div.jpeg".format(sg_uf, sq_candidato)

            proposal_path = Path(home, "Documents", "eleicoes-2022", "eleicoes-2022-data", "proposals", "{0}".format(sg_uf), "2022{0}{1}.pdf".format(sg_uf, sq_candidato))
            
            if proposal_path.exists():
                candidate["PT_CANDIDATO"] = "https://eleicoes-2022-api.herokuapp.com/proposals/{0}/2022{0}{1}.pdf".format(sg_uf, sq_candidato)
                # print(candidate["PT_CANDIDATO"])

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
        # else:
        #     print(ds_situacao_candidato)
        #     print(sg_uf)
        #     print(row["DS_CARGO"])
        #     print(row["NM_CANDIDATO"])
        #     print()

# print(vices["BR"]["2"]["13"])
# print(vices["PA"]["10"].keys())

# print(len(data))

for row in data:
    sg_uf = row["SG_UF"]
    cd_cargo = str(row["CD_CARGO"])
    nr_candidato = str(row["NR_CANDIDATO"])
    sq_candidato = row["SQ_CANDIDATO"]
    # ds_situacao_candidato = row["DS_SITUACAO_CANDIDATURA"]

    candidate = row

    if cd_cargo == "1":
        candidate["VC_CANDIDATO"] = vices[sg_uf]["2"].get(nr_candidato)
    elif cd_cargo == "3":
        candidate["VC_CANDIDATO"] = vices[sg_uf]["4"].get(nr_candidato)
        
        # if candidate["VC_CANDIDATO"] == None:
        #     print(sg_uf)
        #     print(sq_candidato)
            # print(candidate["VC_CANDIDATO"]["DS_CARGO"])
            # print(candidate["VC_CANDIDATO"]["NM_CANDIDATO"])
        
            # print()
    elif cd_cargo == "5":
        candidate["ST1_CANDIDATO"] = vices[sg_uf]["9"].get(nr_candidato)
        candidate["ST2_CANDIDATO"] = vices[sg_uf]["10"].get(nr_candidato)

        # if candidate["ST1_CANDIDATO"] == None:
        #     print(sg_uf)
        #     print(sq_candidato)
        #     print("1 SUPLENTE")
        #     print()

        # if candidate["ST2_CANDIDATO"] == None:
        #     print(sg_uf)
        #     print(sq_candidato)
        #     print("2 SUPLENTE")
        #     print()

    if sg_uf in candidates:
        if cd_cargo in candidates[sg_uf]:
            candidates[sg_uf][cd_cargo] = candidates[sg_uf][cd_cargo] + [candidate]
        else:
            candidates[sg_uf][cd_cargo] = [candidate]
    else:
        candidates[sg_uf] = { cd_cargo: [candidate] }

print(len(candidates["PA"]["3"]))

json_path3 = Path(home, "Documents", "eleicoes-2022", "eleicoes-2022-data", "data2", "BRASIL.json")

with open(json_path3, 'w') as json_file:
  json.dump(candidates, json_file)

for state in candidates.keys():
    json_path4 = Path(home, "Documents", "eleicoes-2022", "eleicoes-2022-data", "data2", "{0}2.json".format(state))

    with open(json_path4, 'w') as json_file:
        json.dump(candidates[state], json_file)