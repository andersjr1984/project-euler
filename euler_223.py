def branch_1 (x,y,z,N):
    a = x - 2*y + 2*z
    b = 2*x - y + 2*z
    c = 2*x - 2*y + 3*z
    count = 0
    if (a+b+c <= N):
        #print (str(x) + ' ' + str(y) + ' ' + str(z))
        #print (str(a) + ' ' + str(b) + ' ' + str(c) + ' 1')
        count += branch_1(a,b,c,N)
        count += branch_2(a,b,c,N)
        count += branch_3(a,b,c,N)
        count += 1
    return count

def branch_2(x,y,z,N):
    a = x+2*y+2*z
    b = 2*x+y+2*z
    c = 2*x+2*y+3*z
    count = 0
    if (a+b+c <= N):
        #print (str(x) + ' ' + str(y) + ' ' + str(z))
        #print (str(a) + ' ' + str(b) + ' ' + str(c) + ' 2')
        count += branch_1(a,b,c,N)
        count += branch_2(a,b,c,N)
        if (a != b):
            count += branch_3(a,b,c,N)
        count += 1
    return count

def branch_3 (x,y,z,N):
    a = -x+2*y+2*z
    b = -2*x+y+2*z
    c = -2*x+2*y+3*z
    count = 0
    if (a+b+c <= N):
        #print (str(x) + ' ' + str(y) + ' ' + str(z))
        #print (str(a) + ' ' + str(b) + ' ' + str(c) + ' 3')
        count += branch_1(a,b,c,N)
        count += branch_2(a,b,c,N)
        count += branch_3(a,b,c,N)
        count += 1
    return count

for t in range(int(input())):
    N = int(input())
    br_1_test = int(N/12)+1
    count = int((N-1)/2)
    while br_1_test > 0:
        count += branch_2(1,br_1_test,br_1_test,N)
        if br_1_test != 1:
            count += branch_3(1,br_1_test,br_1_test,N)
        br_1_test -= 1
    print (count)
