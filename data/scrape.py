from bs4 import BeautifulSoup
import json

fp = open("../ratings.html")
soup = BeautifulSoup(fp, "html.parser")

data = {}
for tr in soup.find_all("tr"):
    td = tr.td
    if not td or not td.a: continue
    if not td.a["href"].startswith("fotw"): continue
    grade = td.find(size="6")
    score = list(grade.children)[-1].string.strip()
    tags = sorted(img["src"][6:].split(".")[0] for img in td.table.find_all("img"))
    code = td.a["href"][5:7]
    data[code] = {
            "code": code,
            "name": td.h2.a.string,
            "grade": grade.b.string,
            "score": score,
            "tags": tags,
            "comment": (td.p.string if td.p else "")
            }

print(json.dumps(data))
