def solution(users, emoticons):
    emodisc = [10 for i in range(len(emoticons)+1)]
    answer = [0, 0]
    
    while emodisc[-1] != 20 :
        pay = [0 for i in range(len(users))]
        plus = 0
        profit = 0

        for j in range(len(emoticons)):
            for i in range(len(users)) :
                if users[i][0] <= emodisc[j] :
                    pay[i] += emoticons[j] * (100-emodisc[j]) // 100
                    if pay[i] >= users[i][1] :
                        plus += 1
                        pay[i] = -7000000
        for i in pay :
            if i > 0 :
                profit += i
        
        if answer[0] < plus :
            answer[0] = plus
            answer[1] = profit
        elif answer[0] == plus and answer[1] < profit :
            answer[1] = profit
            
        emodisc[0] += 10
        
        for i in range(len(emodisc)) :
            if emodisc[i] > 40 :
                emodisc[i] = 10
                emodisc[i+1] += 10
        
    return answer