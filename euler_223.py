#this problem utilizes the pythagorean triple matrix to produce a count of triangles with perimeters less than the given input.
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
        #when a == b, branch_3 breaks down and starts to rapidly decrease till b=1 and that causes problems.  Branch 2 is the only branch a==b.
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

prompt = "Give me a value for the max perimeter and I will give you the number of triangles that have a perimeter less than your input and meet the equation: a**2+b**2=c**2+1: "
N = int(input(prompt))

#the program only needs to go through N/12+1 iterations.
br_1_test = int(N/12)+1

#this provides a count of all the triangles with a=1.  If we use the matrix method, it will count both a=1 and b=1 triangles as the same.
count = int((N-1)/2)

#start at the top and work backwards
while br_1_test > 0:
    count += branch_2(1,br_1_test,br_1_test,N)
    if br_1_test != 1:
        count += branch_3(1,br_1_test,br_1_test,N)
    br_1_test -= 1
print (count)
