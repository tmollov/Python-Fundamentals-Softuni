class Chat:
    def __init__(self, sender,receiver,content):
        self.sender = sender
        self.receiver = receiver
        self.content = content

users = []
chats = []
while True:
    info = input().split(" ")
    if len(info) == 1: 
        break

    if len(info) == 2:
        users.append(info[1])
    
    if len(info) > 2:
        sender = info[0]
        receiver = info[2]
        content = info[3]
        if sender in users and receiver in users:
            chats.append(Chat(sender,receiver,content))

target = input().split(" ")
sms1 = list(filter(lambda x: x.sender == target[0] and x.receiver == target[1],chats))
sms2 = list(filter(lambda x: x.sender == target[1] and x.receiver == target[0],chats))

conversation = list(zip(sms1 + [None] * (len(sms2) - len(sms1)), sms2 + [None] * (len(sms1) - len(sms2))))

if conversation.__len__() == 0:
    print("No messages")
    exit()

for ch in conversation:
    if ch[0] != None:
        print(f"{ch[0].sender}: {ch[0].content}")
    
    if ch[1] != None:
        print(f"{ch[1].content} :{ch[1].sender}")