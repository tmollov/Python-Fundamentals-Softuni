nums = list(map(int,input().split(" ")))

def Add(line):
    global nums
    line = line.split(",")
    if len(line) > 1:
        nums += list(map(int,line))
    elif len(line) == 1:
        nums.append(int(line[0]))
                    
def Contains(num):
    print(num in nums)

def MultiplyList(count):
    global nums
    nums = nums * count
    
def MultiplyNum(target,count):
    global nums
    nums = list(map(lambda x:x*count if x == target else x ,nums))

while True:
    line = input()
    if line == "END":
        break

    comm = line.split(" ")
    if comm[0] == "multiply" and comm[1] == "list":
        MultiplyList(int(comm[2]))
    elif comm[0] == "multiply":
        MultiplyNum(int(comm[1]),int(comm[2]))
    elif comm[0] == "contains":
        Contains(int(comm[1]))
    elif comm[0] == "add":
        Add(comm[1])
    
for num in sorted(nums):
    print(num, end=" ")