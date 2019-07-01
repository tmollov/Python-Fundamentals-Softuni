import math as m

regions = dict()

while True:
    parts = [x for x in input().split(" ") if x]
    if parts[0] == "Aggregate":
        break
    region = parts[0]
    shell = int(parts[1])

    if regions.__contains__(region):
        if shell not in regions[region] :
            regions[region].append(shell)
    else:
        regions.__setitem__(region,[])
        regions[region].append(shell)

seperator = ", "
for region in regions:
    sumOfShells = sum(regions[region]) - (sum(regions[region]) // len(regions[region]))
    if len(regions[region]) == 1:
        print(f"{region} -> {seperator.join(str(item) for item in regions[region])} ({regions[region][0]})")
    else:
        print(f"{region} -> {seperator.join(str(item) for item in regions[region])} ({sumOfShells})")
    
    