normalArr = input().split(" ")
elementToRotate = normalArr.pop()
normalArr.insert(0,elementToRotate)
print(" ".join(str(s) for s in normalArr))