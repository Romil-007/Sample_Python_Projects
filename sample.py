list = [int(x) for x in (input("Enter list values seprate by commas : ")).split(",")]

even_sum = 0
odd_sum = 0
another_var = 1
another_var2 = 3
for i in list:
    if(i%2 == 0):
        even_sum+=i
    else:
        odd_sum+=i

print(list,"\nEven Sum : " , even_sum,"\nOdd Sum : ",odd_sum)