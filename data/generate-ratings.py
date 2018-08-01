#!/usr/bin/env python3

import jinja2, json, sys, os.path

if len(sys.argv) < 2:
    print("usage:", sys.argv[0], "[score|name]")
    sys.exit(-1)

key = sys.argv[1]
path = sys.argv[2] if len(sys.argv) > 2 else ""
base = os.path.dirname(sys.argv[0]) or "."

tags = json.load(open(base + "/tags.json"))
data = json.load(open(base + "/flags.json"))
flags = list(data.values())
flags.sort(key=lambda a: a[key])
if key == "score": flags.reverse()

tmpl = jinja2.Template(open("ratings.tmpl").read())
print(tmpl.render(flags=flags, tags=tags, path=path))
