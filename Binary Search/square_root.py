def sqrt(num):
    precision = int(input("Enter precision: "))
    s = 0
    e = num-1
    ans = 0
    while s <= e:
        m = s + (e-s)//2
        if m*m == num:
            ans = m
            break
        elif m*m < num:
            ans = m
            s = m+1
        else:
            e = m-1

    step = 0.1
    for i in range(precision):
        j = ans
        while j*j <= num:
            ans = j
            j += step
        step /= 10

    return round(ans,precision)

print(sqrt(10))
