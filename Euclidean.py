m = int(input())

def gcd(a, b):
    result = a*b
    while True:
        c = b % a
        if c == 0:
            print(result//a)
            break
        b = a
        a = c

for i in range(m):
    a,b = map(int, input().split())
    gcd(a,b)



