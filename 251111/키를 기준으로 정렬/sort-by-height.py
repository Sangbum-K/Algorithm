n = int(input())

class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

people = [
    Person(name, int(height), int(weight))
    for name, height, weight in (input().split() for _ in range(n))
]

people.sort(key=lambda x: x.height)

for p in people:
    print(p.name, p.height, p.weight)
