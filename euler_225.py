# Enter your code here. Read input from STDIN. Print output to STDOUT

T_list = list(map(int,input().split()))
k = T_list.pop()
orig = T_list

divisor = 1

while k > 0:
    divisor += 2
    while 'True':
        hold = sum(T_list) % divisor
        if (hold == 0):
            T_list = orig
            break
        T_list = T_list[1:]
        T_list.append(hold)
        if (T_list == orig):
            k -= 1
            break

print (divisor)
