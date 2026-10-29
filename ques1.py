def transform(n: int) -> int:
    res = n
    val = number_transform(n)
    while val >= 10:
        res+=val
        val = number_transform(val)
    res+=val
    return res
    

def number_transform(n):
    digit=str(n)
    di = 0
    for i in range(len(digit)):
        if i%2==0:
            di+=int(digit[i])
        else:
            di-=int(digit[i])
    return abs(di)

print(transform(7283))