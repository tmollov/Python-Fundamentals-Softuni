class Exercise:
    def __init__(self,topic,courseName, judgeLink,problems):
        self.topic = topic
        self.courseName = courseName
        self.judgeLink = judgeLink
        self.problems = problems
    
    def Print(self):
        print(f"Exercises: {self.topic}")
        print(f"Problems for exercises and homework for the \"{self.courseName}\" course @ SoftUni.")
        print(f"Check your solutions here: {self.judgeLink}")
        for i in range(len(self.problems)):
            print(f"{i+1}. {self.problems[i]}")

exercises = []

while True:
    data = input()
    if data == "go go go":
        break
    data = data.split(" -> ")
    topic = data[0]
    courseName = data[1]
    link = data[2]
    problems = data[3].split(", ")
    ex = Exercise(topic,courseName,link,problems)
    exercises.append(ex)

for ex in exercises:
    ex.Print()