import pandas as pd
import numpy as np
import os
import itertools 

 
def get_pairs(numbers): 
    pairs = list(itertools.combinations(numbers, 2))
    return pairs


Participants = ['Godwin Divine','Kudsy','Chigozirim Precious Aviara','Merelam','Favour Uche Asiro','Tochukwu Kingsley Smith','John C Aneke','Chioma Emeakama','Okechukwu Marvellous','Valentine','Jonathan Asogbon','Kingsley']
n = int(len(Participants) / 2)
Stages = []
for i in range(len(Participants) - 1):
    t = Participants[:1] + Participants[-i:] + Participants[1:-i] if i else Participants
    Stages.append(list(zip(t[:n], reversed(t[n:]))))


Pairings = []
for step in Stages:
    for pair in step:
        Pairings.append("{} is praying with {}".format(pair[0], pair[1]))

round1,round2,round3,round4,round5,round6,round7,round8,round9,round10,round11 = [],[],[],[],[],[],[],[],[],[],[]
days = [round1,round2,round3,round4,round5,round6,round7,round8,round9,round10,round11]
for i in range(len(days)):
            days[i] = Pairings[(i*6):((i*6)+6)]


round1,round2,round3,round4,round5,round6,round7,round8,round9,round10,round11 = days[0],days[1],days[2],days[3],days[4],days[5],days[6],days[7],days[8],days[9],days[10]
Rounds = [round1,round2,round3,round4,round5,round6,round7,round8,round9,round10,round11]

for i in range(len(Rounds)):
    print(Rounds[i])