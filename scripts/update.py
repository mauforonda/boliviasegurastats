#!/usr/bin/env python3

import requests
from datetime import datetime, timedelta
import csv

ayer = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
hoy = datetime.today().strftime('%Y-%m-%d')
url = "https://juliael.carto.com/api/v1/viz/c70fa175-3e6a-4955-8088-89048c6e6886?show_stats=true"
helper = 'scripts/helper.csv'
output = 'vistas.csv'
with open(helper, 'r') as f:
  lag = int(list(csv.reader(f))[-1][1])

data = requests.get(url).json()
vistas = data['stats'][ayer] + data['stats'][hoy] - lag
with open(output, 'a') as f:
  f.write("\n{a},{v}".format(a=ayer, v=int(vistas)))
with open(helper, 'a') as f:
  f.write("\n{a},{v}".format(a=hoy, v=int(data['stats'][hoy])))

