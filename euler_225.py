# Enter your code here. Read input from STDIN. Print output to STDOUT

prompt = "This program will give you the Nth odd divisor of a sum of a list of numbers.  Please enter the first three numbers in the list, separated by a space, then enter N, which is the number of non-divisors you are looking for: "


T_list = list(map(int,input(prompt).split()))
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
