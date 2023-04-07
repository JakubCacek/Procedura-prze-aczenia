#działa
# Lista = []
# list_num = 0
# trials = 13
# for i in range(trials):
#     list_num = list_num + 1
#     Lista.append(list_num)
    
# print(Lista)

import random

Lista_zadan = ["Num", "Let"]
Let_stim = ["a", "b", "c"]
Num_stim = [1,2,3,4,5]
trial = 0
trial_num = []
trial_leng = 10

for i in range(trial_leng):
    trial = trial + 1
    trial_num.append(trial)
    if trial == 1:
        task_type = random.choice(Lista_zadan)
        if task_type == "Let":
            print(random.choice(Let_stim))
        elif task_type == "Num":
            print(random.choice(Num_stim))
    else:
        rn = random.random()
        if rn >= 0.25:
            Lista_zadan[i] != task_type[i-1]
            task_type = Lista_zadan
                #save trial_type
            if task_type == "Let":
                print(random.choice(Let_stim))
            elif task_type == "Num":
                print(random.choice(Num_stim))
        elif rn < 0.25:
            Lista_zadan[i] == Lista_zadan[i-1]
            task_type = Lista_zadan
            if task_type == "Let":
                print(random.choice(Let_stim))
            elif task_type == "Num":
                print(random.choice(Num_stim))