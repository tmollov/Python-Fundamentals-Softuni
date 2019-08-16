import re

regex = r"<a.+<\/a>"

while True:
    tags = input()
    if tags == "end":
        break

    matches = re.findall(regex,tags)
    if len(matches) == 0:
        print(tags)
        continue
    for match in matches:
        res = re.sub(r'<\s*a\s*',"[URL ",match)
        res = re.sub(r"<\s*\/\s*a\s*>","[/URL]",res)
        res = res.replace(">","]")
        outp = re.sub(match,res,tags)
        print(outp)