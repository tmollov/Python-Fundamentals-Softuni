while True:
    word = input()
    if word == "end":
        break
    
    core = len(word) - 2
    nilapdromesSize = 1
    coreAmplifier = 1
    nilapdrome = None
    while True:
        nilap1 = word[0:nilapdromesSize]
        nilap2 = word[core+coreAmplifier:len(word)]
        
        if nilap1 == nilap2:
            nilapdrome  = f"{word[nilapdromesSize:core+coreAmplifier]}{nilap1}{word[nilapdromesSize:core+coreAmplifier]}"
        
        core -= 2
        coreAmplifier += 1
        nilapdromesSize += 1
        if core < 1:
            break
    if nilapdrome != None:
        print(nilapdrome)