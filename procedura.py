import random


Lista_zadan = ["Num", "Let"] # 2 rodzaje zadań, między którymi badani mają się przełączać
Let_stim = ["a", "b", "c"] #Zadanie z liter
Num_stim = [1,2,3,4,5] #zadanie z liczb 
trial = 0 #numer trialu
trial_num = [] #lista do zapisu numeru trialu
task_hist = [] #poprzedni trial
trial_leng = 10 #testowa liczba triali

for i in range(trial_leng):
    trial = trial + 1
    trial_num.append(trial)
    if trial == 1:
        task_type = random.choice(Lista_zadan)
        task_hist.append(task_type) #zapis poprzedniego trialu
        if task_type == "Let":
            print(random.choice(Let_stim))
        elif task_type == "Num":
            print(random.choice(Num_stim))
    else:
        rn = random.random()
        if rn >= 0.25:
            Lista_zadan[i] != task_hist[i-1]
            task_type = Lista_zadan
            task_hist.append(task_type)
                #save trial_type
            if task_type == "Let":
                print(random.choice(Let_stim))
            elif task_type == "Num":
                print(random.choice(Num_stim))
        elif rn < 0.25:
            Lista_zadan[i] == task_hist[i-1]
            task_type = Lista_zadan
            task_hist.append(task_type)
            if task_type == "Let":
                print(random.choice(Let_stim))
            elif task_type == "Num":
                print(random.choice(Num_stim))
