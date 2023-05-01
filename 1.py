import numpy as np

n = 5 #количество экспонатов
w = 13 #вес, который может унести вор за рах
m = 2 #количестов заходов

exp_w = [3, 4, 5, 8, 9] #вес каждого экспоната
exp_p = [1, 6, 4, 7, 6] #стоимость каждого экспоната

ans = 0

def func(n, w): 
    a = np.zeros((n, w)) #создаем двумерный массив, куда будет записывать промежуточные результаты
    global exp_w
    global exp_p        
    for k in range(n):           
        for s in range(w): #Перебираем для каждого k все вместимости                           
            if s >= exp_w[k]: #Если текущий предмет вмещается в рюкзак                       
                a[k][s] = max(a[k - 1][s], a[k - 1][s - exp_w[k]] + exp_p[k]) #Выбираем класть его или нет 
            else:
                a[k][s] = a[k - 1][s] #Иначе, не кладем 
    
    ans = a[n-1][w-1]
    sum = a[n-1][w-1]
    j = w-1
    for i in range(n-1, 0, -1):
        '''
        идем от обратного и ищем какие экспонаты положили в рюкзак
        убираем эти экспонаты из списка и уменьшаем их количество
        далее снова вызываем эту функцию уже с новыми значениями 
        '''
        if sum == 0:
            break
        if a[i-1][j] != sum:
            sum -= exp_p[i]
            j -= exp_p[i]
            n -= 1
            exp_w.remove(exp_w[i])
            exp_p.remove(exp_p[i])

    return ans, n


for i in range(m):
    tek, n = func(n,w)
    ans += tek

print(ans)