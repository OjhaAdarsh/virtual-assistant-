num = int(input("Please provide the number to calculate it's factorial "))    
print("you entered the number = ",num)
factorial = 1       
if num == 0:    
   print("The factorial of given number is = 1")    
else:    
    for i in range(1,num + 1):    
       factorial = factorial*i    
    print("Factorial of given number is",factorial)    