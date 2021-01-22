# Function for nth Fibonacci number 
def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==0: 
        return 0
    # Second Fibonacci number is 1 
    elif n==1: 
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2) 
# Driver Program 
num= int(input("Enter Number: "))
n1,n2 = 0,1    
print("Fibonacci numbers are: ",n1,n2,end=" ")
for i in range(2,num):
    n3 = n1 + n2
    print(n3,end=" ")
    n1 = n2
    n2 = n3

print("\nsum:",Fibonacci(num)) 