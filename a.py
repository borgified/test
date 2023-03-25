#!/usr/bin/env python

import json

i = open("ab-results-README.md-filtered.json","r")
o = open("ab-results-output.md","w")
data = json.loads(f.read())

heading="""| Line | Status | Link |
| ---- | ------ | ---- |"""

o.write(heading)
for i in data:
  o.write("|",i['loc'],"|",i['status'],"|",i['link'],"|")

f.close()
