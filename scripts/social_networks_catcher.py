import csv
import json

import os
from pathlib import Path

# import glob

# data = []
social_networks = {}
# vices = {}

states = []

home = Path.home()

dir_path = Path(home, "Documents", "eleicoes-2022", "eleicoes-2022-data", "data")

files = os.listdir(dir_path)

for file in files:
    if ".json" in file:
        states.append(file.split(".")[0])

# print(states)

for state in states:
    json_path = Path(home, "Documents", "eleicoes-2022", "eleicoes-2022-data", "data", "{0}.json".format(state))

    with open(json_path, 'r') as f:
        data = json.load(f)

        print(state)
        # print(data.keys())
        print()

        for cd_cargo in data.keys():
            for candidate in data[cd_cargo]:
                sq_candidato = candidate["SQ_CANDIDATO"]

                social_networks[sq_candidato] = candidate["RS_CANDIDATO"]

                if cd_cargo in ["1", "3"]:
                    vice_candidato = candidate["VC_CANDIDATO"]
                    sq_vice_candidato = vice_candidato["SQ_CANDIDATO"]

                    social_networks[sq_vice_candidato] = vice_candidato["RS_CANDIDATO"]
                elif cd_cargo in ["5"]:
                    st1_candidato = candidate["ST1_CANDIDATO"]
                    st2_candidato = candidate["ST2_CANDIDATO"]

                    if st1_candidato:
                        sq_st1_candidato = st1_candidato["SQ_CANDIDATO"]
                        
                        social_networks[sq_st1_candidato] = st1_candidato["RS_CANDIDATO"]
                    
                    if st2_candidato:
                        sq_st2_candidato = st2_candidato["SQ_CANDIDATO"]

                        social_networks[sq_st2_candidato] = st2_candidato["RS_CANDIDATO"]

# print(len(social_networks.keys()))

json_path2 = Path(home, "Documents", "eleicoes-2022", "eleicoes-2022-data", "redes-sociais", "BRASIL.json")

with open(json_path2, 'w') as json_file:
  json.dump(social_networks, json_file)

networks = {}

for sq_candidato in social_networks.keys():
    # print(social_networks[sq_candidato])

    if social_networks[sq_candidato]:
        for network in social_networks[sq_candidato].keys():
            if network in networks:
                networks[network] = networks[network] + [social_networks[sq_candidato][network]]
            else: 
                networks[network] = [social_networks[sq_candidato][network]]

# print(networks.keys())

for network in networks.keys():
    file_path = Path(home, "Documents", "eleicoes-2022", "eleicoes-2022-data", "redes-sociais", "{0}.txt".format(network))

    with open(file_path, 'w', encoding='utf-8') as f:
        for item in networks[network]:
            f.write("{0}\n".format(item))
            # f.write("This file\n\n")
            # f.write("contains three lines\n")

# csv_path = Path(home, "Documents", "eleicoes-2022", "eleicoes-2022-data", "data", "BRASIL.csv")

# with open(csv_path, newline='', encoding='latin1') as f:
#     reader = csv.DictReader(f, delimiter=';')

#     for row in reader:
#         sg_uf = row["SG_UF"]
#         cd_cargo = str(row["CD_CARGO"])
#         nr_candidato = str(row["NR_CANDIDATO"])
#         sq_candidato = row["SQ_CANDIDATO"]

#         candidate = row

#         candidate["BS_CANDIDATO"] = assets.get(sq_candidato)
#         candidate["BS_CANDIDATO"] = assets.get(sq_candidato)

#         img_path = Path(home, "Documents", "eleicoes-2022", "eleicoes-2022-data", "imgs", "candidates", "{0}".format(sg_uf), "F{0}{1}_div.jpg".format(sg_uf, sq_candidato))
        
#         if img_path.exists():
#             candidate["IM_CANDIDATO"] = "https://raw.githubusercontent.com/alexsilva96dev/eleicoes-2022-data/main/imgs/candidates/{0}/F{0}{1}_div.jpg".format(sg_uf, sq_candidato)
#         else:
#             candidate["IM_CANDIDATO"] = "https://raw.githubusercontent.com/alexsilva96dev/eleicoes-2022-data/main/imgs/candidates/{0}/F{0}{1}_div.jpeg".format(sg_uf, sq_candidato)

#         if sg_uf in vices:
#             if cd_cargo in ["2", "4", "9", "10"]:
#                 if cd_cargo in vices[sg_uf]:
#                     vices[sg_uf][cd_cargo][nr_candidato] = candidate
#                 else:
#                     vices[sg_uf][cd_cargo] = { nr_candidato: candidate }
#             else:
#                data.append(candidate) 
#         else:
#             if cd_cargo in ["2", "4", "9", "10"]:
#                 vices[sg_uf] = { cd_cargo: { nr_candidato: candidate } }
#             else:
#                 data.append(candidate)

# print(vices["BR"]["2"]["13"])
# print(vices["PA"]["10"].keys())

# json_path = Path(home, "Documents", "eleicoes-2022", "eleicoes-2022-data", "data", "BRASIL.json")

# with open(json_path, 'w') as json_file:
#   json.dump(data, json_file)