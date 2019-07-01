word = input().split(" ")

l = -1
for i in range(int(len(word)/2)):
    swap = word[i] 
    word[i] = word[l]
    word[l] = swap
    l -= 1

print(" ".join(word))