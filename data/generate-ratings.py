#!/usr/bin/env python3

import jinja2, json

tags = json.load(open("tags.json"))
data = json.load(open("flags.json"))
flags = list(data.values())
flags.sort(key=lambda a: a["score"])
flags.reverse()

tmpl = jinja2.Template(open("ratings.tmpl").read())
print(tmpl.render(flags=flags, tags=tags))
