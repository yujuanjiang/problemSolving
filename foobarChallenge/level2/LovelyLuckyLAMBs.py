def solution(x):

    if x < 2:
        return 0
    
    tmp = [1, 1]
    i = 0
    while sum(tmp) <= x: 
        i += 1
        tmp.append(tmp[i] + tmp[i-1])  
    minimum = i + 1
    
    tmp = [1]
    i = 0
    while sum(tmp) <= x:
        i += 1
        tmp.append(2*tmp[i-1])
    maximum = i
    print abs(minimum - maximum)
    return abs(minimum - maximum)
 
solution(143)
