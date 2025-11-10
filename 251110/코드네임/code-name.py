MAX_N = 5

codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))

class Agent():
    def __init__(self,name,score):
        self.name = name
        self.score = score

agents = []
for i in range(MAX_N):
    agents.append(Agent(codenames[i], scores[i]))


mn = agents[0].score
idx = 0

for i in range(len(agents)):
    if agents[i].score < mn:
        mn = agents[i].score
        idx = i


print(agents[idx].name,agents[idx].score)
    

