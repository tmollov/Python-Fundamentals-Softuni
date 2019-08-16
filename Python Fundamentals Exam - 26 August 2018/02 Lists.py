while True:
    line = list(filter(lambda x: x != "",input().lstrip().split(" ")))
    if line[0] == "stop":
        exit()
    line = list(map(int,line))
    uniques = set(line)
    if len(uniques) == len(line):
        line = sorted(list(map(lambda x: x if x%2 == 1 else x+2,line)))
        print(f"Unique list: {','.join(list(map(str,line)))}")
        print(f"Output: {(sum(line) / len(line)):.2f}")
    else:
        line = sorted(list(map(lambda x: x if x%2 == 0 else x+3,line)))
        print(f"Non-unique list: {':'.join(list(map(str,line)))}")
        print(f"Output: {(sum(line) / len(line)):.2f}")