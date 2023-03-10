def division(dividend, divisor):
    if divisor == 0 and dividend == 0:
        print("Indeterminate")
        return
    if divisor == 0:
        print("Undefined")
        return
    s = 0
    e = abs(dividend)
    ans = 0
    while s <= e:
        m = s + (e-s)//2
        if abs(divisor*m) == abs(dividend):
            ans = m
            break
        elif abs(divisor*m) > abs(dividend):
            e = m-1
        else:
            ans = m
            s = m+1
    if dividend*divisor < 0:
        ans *= -1
    print(ans)

division(20,0)