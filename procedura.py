#działa
# Lista = []
# list_num = 0
# trials = 13
# for i in range(trials):
#     list_num = list_num + 1
#     Lista.append(list_num)
    
# print(Lista)

import random

Lista_zadan = ["Num", "Let"] # 2 rodzaje zadań, między którymi badani mają się przełączać
Let_stim = ["a", "b", "c"] #Zadanie z liter
Num_stim = [1,2,3,4,5] #zadanie z liczb 
trial = 0 #numer trialu
trial_num = [] #lista do zapisu numeru trialu
trial_leng = 10 #testowa liczba triali

for i in range(trial_leng):
    trial = trial + 1
    trial_num.append(trial)
    if trial == 1: #w pierwszym trialu badany losouje jedno z zadań
        task_type = random.choice(Lista_zadan)
        if task_type == "Let":
            print(random.choice(Let_stim))
        elif task_type == "Num":
            print(random.choice(Num_stim))
    else:
        rn = random.random() # po pierwszym trialu losowany jest numer. Jeśli jest on mniejszy lub równy 0.25, to powinno wyświetlić im się inne zadanie
        if rn >= 0.25:
            Lista_zadan[i] != task_type[i-1] #wydawało mi się, że przełączenia można zrobić tak, ale pokazuje IndexError: list index out of range
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
