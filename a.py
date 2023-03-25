#!/usr/bin/env python

import json

i = open("ab-results-README.md-filtered.json","r")
o = open("./pr/ab-results-output.md","w")
data = json.loads(i.read())

heading="""| Line | Status | Link |
| ---- | ------ | ---- |
"""

o.write(heading)
for i in data:
  o.write("| {} | {} | {} |\n".format(i['loc'],i['status'],i['link']))
