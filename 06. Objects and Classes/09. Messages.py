class Message:
    def __init__(self,content,sender):
        self.content = content
        self.sender = sender

class User:
    def __init__(self,username):
        self.username = username
        self.messages = []

users = dict()

while True:
    info = input().split(" ")
    if len(info) == 1: 
        break

    if len(info) == 2:
        username = info[1]
        users.__setitem__(username,User(username))
    
    if len(info) > 2:
        sender = info[0]
        receiver = info[2]
        content = info[3]

        # Check if both users exists
        if users.__contains__(sender) and users.__contains__(receiver):
            sms = Message(content,sender)
            users[receiver].messages.append(sms)

chat = input().split(" ")
messagesOfSecond = list(filter(lambda x:x.sender == chat[1],users[chat[0]].messages))
messagesOfFirst = list(filter(lambda x:x.sender == chat[0],users[chat[1]].messages))
conversation = list(zip(messagesOfFirst + [None] * (len(messagesOfSecond) - len(messagesOfFirst)), messagesOfSecond + [None] * (len(messagesOfFirst) - len(messagesOfSecond))))

if conversation.__len__() == 0:
    print("No messages")
    exit()

for ch in conversation:
    if ch[0] != None:
        print(f"{ch[0].sender}: {ch[0].content}")
    
    if ch[1] != None:
        print(f"{ch[1].content} :{ch[1].sender}")