def krug(r):
    s=3.14*r*r
    return s
def treugolnik(a,b,c):
    if (a+b>c and b+c>a and a+c>b):
        p=(a+b+c)/2
        s=(p*(p-a)*(p-b)*(p-c))**0.5
    return s
