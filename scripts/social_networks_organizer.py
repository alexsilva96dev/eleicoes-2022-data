import csv
import json

import os
from pathlib import Path

# import glob

# data = []
# vices = {}

states = []

home = Path.home()

dir_path = Path(home, "Documents", "eleicoes-2022", "eleicoes-2022-data", "redes-sociais")

files = os.listdir(dir_path)

for file in files:
    if ".csv" in file:
        if file.split(".")[0] != "BRASIL":
            states.append(file.split(".")[0])

# print(states)

for state in states:
    social_networks = {}

    csv_path = Path(home, "Documents", "eleicoes-2022", "eleicoes-2022-data", "redes-sociais", "{0}.csv".format(state))

    with open(csv_path, newline='', encoding='latin1') as f:
        reader = csv.DictReader(f, delimiter=';')

        for row in reader:
            sq_candidato = row["SQ_CANDIDATO"] 
            ds_url = row["DS_URL"]  

            if sq_candidato in social_networks:
                if "flickr.com" in ds_url.lower():
                    social_networks[sq_candidato]["flickr"] = ds_url
                elif "gettr.com" in ds_url.lower():
                    social_networks[sq_candidato]["gettr"] = ds_url
                elif "linkedin" in ds_url.lower():
                    social_networks[sq_candidato]["linkedin"] = ds_url
                elif "linkedln" in ds_url.lower():
                    social_networks[sq_candidato]["linkedin"] = ds_url
                elif "linktr" in ds_url.lower():
                    social_networks[sq_candidato]["linktr"] = ds_url
                elif "pinterest.com" in ds_url.lower():
                    social_networks[sq_candidato]["pinterest"] = ds_url
                elif "spotify.com" in ds_url.lower():
                    social_networks[sq_candidato]["spotify"] = ds_url
                elif "t.me" in ds_url.lower():
                    social_networks[sq_candidato]["telegram"] = ds_url
                elif "telegram" in ds_url.lower():
                    social_networks[sq_candidato]["telegram"] = ds_url
                elif "twitter" in ds_url.lower():
                    social_networks[sq_candidato]["twitter"] = ds_url
                elif "twiiter" in ds_url.lower():
                    social_networks[sq_candidato]["twitter"] = ds_url
                elif "twiter" in ds_url.lower():
                    social_networks[sq_candidato]["twitter"] = ds_url
                elif "whatsapp" in ds_url.lower():
                    social_networks[sq_candidato]["whatsapp"] = ds_url
                elif "wa.me" in ds_url.lower():
                    social_networks[sq_candidato]["whatsapp"] = ds_url
                elif "contate.me" in ds_url.lower():
                    social_networks[sq_candidato]["whatsapp"] = ds_url
                elif "zapdodudu" in ds_url.lower():
                    social_networks[sq_candidato]["whatsapp"] = ds_url
                elif "tiktok" in ds_url.lower():
                    social_networks[sq_candidato]["tiktok"] = ds_url
                elif "wikipedia" in ds_url.lower():
                    social_networks[sq_candidato]["wikipedia"] = ds_url
                elif "youtube" in ds_url.lower():
                    social_networks[sq_candidato]["youtube"] = ds_url
                elif "youtu.be" in ds_url.lower():
                    social_networks[sq_candidato]["youtube"] = ds_url
                elif "youtubr" in ds_url.lower():
                    social_networks[sq_candidato]["youtube"] = ds_url
                elif "kwai" in ds_url.lower():
                    social_networks[sq_candidato]["kwai"] = ds_url
                elif "kw.ai" in ds_url.lower():
                    social_networks[sq_candidato]["kwai"] = ds_url
                elif "instagram" in ds_url.lower():
                    social_networks[sq_candidato]["instagram"] = ds_url
                elif "instagran" in ds_url.lower():
                    social_networks[sq_candidato]["instagram"] = ds_url
                elif "instargam" in ds_url.lower():
                    social_networks[sq_candidato]["instagram"] = ds_url
                elif "instragram" in ds_url.lower():
                    social_networks[sq_candidato]["instagram"] = ds_url
                elif "intagram" in ds_url.lower():
                    social_networks[sq_candidato]["instagram"] = ds_url
                elif "instragran" in ds_url.lower():
                    social_networks[sq_candidato]["instagram"] = ds_url
                elif "instagra" in ds_url.lower():
                    social_networks[sq_candidato]["instagram"] = ds_url
                elif "instaram" in ds_url.lower():
                    social_networks[sq_candidato]["instagram"] = ds_url
                elif "instaqram" in ds_url.lower():
                    social_networks[sq_candidato]["instagram"] = ds_url
                elif "instragamm" in ds_url.lower():
                    social_networks[sq_candidato]["instagram"] = ds_url
                elif "instagam" in ds_url.lower():
                    social_networks[sq_candidato]["instagram"] = ds_url
                elif "instrangram" in ds_url.lower():
                    social_networks[sq_candidato]["instagram"] = ds_url
                elif "facebook" in ds_url.lower():
                    social_networks[sq_candidato]["facebook"] = ds_url
                elif "fb.com" in ds_url.lower():
                    social_networks[sq_candidato]["facebook"] = ds_url
                elif "fecebook" in ds_url.lower():
                    social_networks[sq_candidato]["facebook"] = ds_url
                else:
                    social_networks[sq_candidato]["site"] = ds_url
            else:
                if "flickr.com" in ds_url.lower():
                    social_networks[sq_candidato] = { "flickr": ds_url }
                elif "gettr.com" in ds_url.lower():
                    social_networks[sq_candidato] = { "gettr": ds_url }
                elif "linkedin" in ds_url.lower():
                    social_networks[sq_candidato] = { "linkedin": ds_url }
                elif "linkedln" in ds_url.lower():
                    social_networks[sq_candidato] = { "linkedin": ds_url }
                elif "linktr" in ds_url.lower():
                    social_networks[sq_candidato] = { "linktr": ds_url }
                elif "pinterest.com" in ds_url.lower():
                    social_networks[sq_candidato] = { "pinterest": ds_url }
                elif "spotify.com" in ds_url.lower():
                    social_networks[sq_candidato] = { "spotify": ds_url }
                elif "t.me" in ds_url.lower():
                    social_networks[sq_candidato] = { "telegram": ds_url }
                elif "telegram" in ds_url.lower():
                    social_networks[sq_candidato] = { "telegram": ds_url }
                elif "twitter" in ds_url.lower():
                    social_networks[sq_candidato] = { "twitter": ds_url }
                elif "twiiter" in ds_url.lower():
                    social_networks[sq_candidato] = { "twitter": ds_url }
                elif "twiter" in ds_url.lower():
                    social_networks[sq_candidato] = { "twitter": ds_url }
                elif "whatsapp" in ds_url.lower():
                    social_networks[sq_candidato] = { "whatsapp": ds_url }
                elif "wa.me" in ds_url.lower():
                    social_networks[sq_candidato] = { "whatsapp": ds_url }
                elif "contate.me" in ds_url.lower():
                    social_networks[sq_candidato] = { "whatsapp": ds_url }
                elif "zapdodudu" in ds_url.lower():
                    social_networks[sq_candidato] = { "whatsapp": ds_url }
                elif "tiktok" in ds_url.lower():
                    social_networks[sq_candidato] = { "tiktok": ds_url }
                elif "wikipedia" in ds_url.lower():
                    social_networks[sq_candidato] = { "wikipedia": ds_url }
                elif "youtube" in ds_url.lower():
                    social_networks[sq_candidato] = { "youtube": ds_url }
                elif "youtu.be" in ds_url.lower():
                    social_networks[sq_candidato] = { "youtube": ds_url }
                elif "youtubr" in ds_url.lower():
                    social_networks[sq_candidato] = { "youtube": ds_url }
                elif "kwai" in ds_url.lower():
                    social_networks[sq_candidato] = { "kwai": ds_url }
                elif "kw.ai" in ds_url.lower():
                    social_networks[sq_candidato] = { "kwai": ds_url }
                elif "instagram" in ds_url.lower():
                    social_networks[sq_candidato] = { "instagram": ds_url }
                elif "instagran" in ds_url.lower():
                    social_networks[sq_candidato] = { "instagram": ds_url }
                elif "instargam" in ds_url.lower():
                    social_networks[sq_candidato] = { "instagram": ds_url }
                elif "instragram" in ds_url.lower():
                    social_networks[sq_candidato] = { "instagram": ds_url }
                elif "intagram" in ds_url.lower():
                    social_networks[sq_candidato] = { "instagram": ds_url }
                elif "instragran" in ds_url.lower():
                    social_networks[sq_candidato] = { "instagram": ds_url }
                elif "instagra" in ds_url.lower():
                    social_networks[sq_candidato] = { "instagram": ds_url }
                elif "instaram" in ds_url.lower():
                    social_networks[sq_candidato] = { "instagram": ds_url }
                elif "instaqram" in ds_url.lower():
                    social_networks[sq_candidato] = { "instagram": ds_url }
                elif "instragamm" in ds_url.lower():
                    social_networks[sq_candidato] = { "instagram": ds_url }
                elif "instagam" in ds_url.lower():
                    social_networks[sq_candidato] = { "instagram": ds_url }
                elif "instrangram" in ds_url.lower():
                    social_networks[sq_candidato] = { "instagram": ds_url }
                elif "facebook" in ds_url.lower():
                    social_networks[sq_candidato] = { "facebook": ds_url }
                elif "fb.com" in ds_url.lower():
                    social_networks[sq_candidato] = { "facebook": ds_url }
                elif "fecebook" in ds_url.lower():
                    social_networks[sq_candidato] = { "facebook": ds_url }
                else:
                    social_networks[sq_candidato] = { "site": ds_url }

        json_path = Path(home, "Documents", "eleicoes-2022", "eleicoes-2022-data", "redes-sociais", "{0}.json".format(state))

        with open(json_path, 'w') as json_file:
            json.dump(social_networks, json_file)  

        print(len(social_networks.keys()))