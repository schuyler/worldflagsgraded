#!/usr/bin/env python3

import jinja2, json, sys

if len(sys.argv) < 2:
    print("usage:", sys.argv[0], "[score|name]")
    sys.exit(-1)

key = sys.argv[1]
tags = json.load(open("tags.json"))
data = json.load(open("flags.json"))
flags = list(data.values())
flags.sort(key=lambda a: a[key])
flags.reverse()

tmpl = jinja2.Template(open("ratings.tmpl").read())
print(tmpl.render(flags=flags, tags=tags))
