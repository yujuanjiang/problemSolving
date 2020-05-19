def solution(l):
    #print l
    if len(l) <= 1:
        return l

    l = sorted(l)
    sort_l = [x.split('.') for x in l]
    
    sort_l_num = []
    for i in sort_l:
        if len(i) == 1:
            sort_l_num.append(int(i[0])*10000)
        elif len(i) == 2:
            sort_l_num.append(int(i[0])*10000 + int(i[1])*100)
        elif len(i) == 3:
            sort_l_num.append(int(i[0])*10000 + int(i[1])*100 + int(i[2]))
        else:
            return 0
    
    sort_l_num = enumerate(sort_l_num)
    
    sort_l_num = sorted(sort_l_num, key=lambda x: x[1])
    print sort_l_num
    
    ret = []
    for idx, val in sort_l_num:
        ret.append(l[idx])
        
    return ret
 
solution(["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"])
