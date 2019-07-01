def Post(postName):
    socialMedia.__setitem__(postName,list([0,0]))

def Like(postName):
    socialMedia[postName][0] += 1

def Dislike(postName):
    socialMedia[postName][1] += 1

def Comment(postName,commentator,content):
    socialMedia[postName].append(f"*  {commentator}: {content}")

socialMedia = dict()

while True:
    command = input()
    if command == "drop the media":
        break
    
    parts = command.split(" ")
    if parts[0] == "post":
        Post(parts[1])
    elif parts[0] == "like": 
        Like(parts[1])
    elif parts[0] == "dislike": 
        Dislike(parts[1])
    elif parts[0] == "comment": 
        if len(parts) > 4:
            for i in range(4,len(parts)):
                parts[3] += " " + parts[i]
        Comment(parts[1], parts[2] ,parts[3])

for post in socialMedia:
    print(f"Post: {post} | Likes: {socialMedia[post][0]} | Dislikes: {socialMedia[post][1]}")
    print("Comments:")
    if len(socialMedia[post]) == 2:
        print("None")
    for i in range(2,len(socialMedia[post])):
        print(socialMedia[post][i])