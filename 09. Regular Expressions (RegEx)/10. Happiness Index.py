import re

happyReg = r"([:;]\s*[\)D*\]}])|([(*c[]\s*[;:])"
sadReg = r"([:;]\s*[([{c]|[]})D]\s*[:;])"

happinesIndex = 0

senc = input()
happyMatches = re.findall(happyReg,senc)