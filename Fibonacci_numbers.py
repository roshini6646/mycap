n = int(input("enter the maximum length of the series:"))
enter the maximum length of the series:10
previous_num = 0
next_num = 1
sum = 0
count = 1
print("Fibonacci series: ", end = " ")
Fibonacci series: 
while (count <= n):
    print(sum, end = " ")
    count +=1
    previous_num = next_num
    next_num = sum
    sum = previous_num + next_num
0 1 1 2 3 5 8 13 21 34 
