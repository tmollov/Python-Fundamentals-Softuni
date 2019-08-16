import math

while True:
    state = input()
    if state == "collapse":
        break
    fiction = input()
    
    length = math.ceil(len(fiction)/2)
    for i in range(length):
        state = state.replace(fiction,"")
        fiction = fiction[1:-1]
    if state == "":
        print("(void)")
    else:
        print(state.strip())