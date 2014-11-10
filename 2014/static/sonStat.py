import random

random.seed()
trials = 1000000
younger = 0
oneSon = 0
bothSon = 0

for i in range(trials):
    family = (random.randint(0,1), random.randint(0,1))
    if family == (1,1):
        bothSon += 1
    if family[1] == 1:
        younger += 1
    if 1 in family:
        oneSon += 1

print(bothSon/oneSon)
print(bothSon/younger)

