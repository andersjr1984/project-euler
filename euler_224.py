def branch_1 (x,y,z,N):
    a = x - 2*y + 2*z
    b = 2*x - y + 2*z
    c = 2*x - 2*y + 3*z
    count = 0
    if (a+b+c <= N):
        count += branch_1(a,b,c,N)
        count += branch_2(a,b,c,N)
        count += branch_3(a,b,c,N)
        #have to ensure we are only counting items where a>b
        if (a<=b):
            count +=1
    return count

def branch_2(x,y,z,N):
    a = x+2*y+2*z
    b = 2*x+y+2*z
    c = 2*x+2*y+3*z
    count = 0
    if (a+b+c <= N):
        count += branch_1(a,b,c,N)
        count += branch_2(a,b,c,N)
        count += branch_3(a,b,c,N)
        if (a<=b):
            count += 1
    return count

def branch_3 (x,y,z,N):
    a = -x+2*y+2*z
    b = -2*x+y+2*z
    c = -2*x+2*y+3*z
    count=0
    if (a+b+c <= N):
        count += branch_1(a,b,c,N)
        count += branch_2(a,b,c,N)
        count += branch_3(a,b,c,N)
        if (a<=b):
            count += 1
    return count


for t in range(int(input())):
    N = int(input())
    print (1+branch_1(2,2,3,N) + branch_2(2,2,3,N) + branch_3(2,2,3,N))
