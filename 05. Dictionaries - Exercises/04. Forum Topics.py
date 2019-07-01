def GetClearList(array) :
    return list(dict.fromkeys(array))

def GetOutputTags(tags):
    arr = list()
    for tag in tags:
        arr.append("#" + tag)
    return arr

def IsTopicContainsTags(tags,topicTags):
    count = 0
    for tag in topicTags:
        if tag in tags:
            count += 1
    if count == len(tags):
        return True
    else:
        return False

forum = dict()

targetTags = ""
while True:
    string = input().split(" -> ")
    if string[0] == "filter":
        targetTags = input().split(", ")
        break

    topic = string[0]
    tags = string[1].split(", ")
    
    if forum.__contains__(topic):
        forum[topic] += tags 
        forum[topic] = GetClearList(forum[topic])
    else :
        forum.__setitem__(topic,tags)
        forum[topic] = GetClearList(forum[topic])

seperator = ', '
for topic in forum:
    if IsTopicContainsTags(targetTags,forum[topic]):
        print(f"{topic} | {seperator.join(GetOutputTags(forum[topic]))}")