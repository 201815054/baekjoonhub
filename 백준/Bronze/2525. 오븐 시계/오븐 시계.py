current_h,current_m = map(int,input().split())
requisite_m = int(input())

tmp = current_m+requisite_m
if tmp>59:
    h = int(tmp/60)
    m = tmp%60
    if current_h+h>24:
        h = (current_h+h)-24
    elif current_h+h ==24:
        h = 0
    else:
        h = current_h+h
    print(f"{h} {m}")
else:
    print(f"{current_h} {tmp}")
    
    
    