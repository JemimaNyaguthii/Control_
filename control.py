# Write a function to check whether the numbers in the range of 50 are divisible by either 5,7,9
def comparisons():
    x=range(50)
    for i in x:
        if i%5==0:
            print(f"{i} is divisible by 5")
        elif i%7==0:
            print(f"{i} is divisible by 7")
        elif i%9==0:
            print(f"{i} is divisible by 9")
        else:
            print(f"{i} is not divisible by 5,7,9")   
#   Write a function in a range of 0,20 that prints numbers which are divisible by 3                   
def continue_statement():
    x=0
    while x<=20:
        x+=1 
        if x%3!=0:
            continue
        print(x) 

# Write a function that uses while, if and continue statements to print all the even numbers between 0 and 50.
def even_numb():
    x=0
    while x<=50:
        x+=1
        if x%2!=0:
            continue
        print(x)

# Write a function that takes a list of integers as input and prints the sum of all the even numbers in the list 
def sum_even(nums):
    sum = 0
    for i in nums:
        if i % 2 == 0:
            sum += i
    print(sum)
sum_even(([1,2,3,4,5,6,7,8,9,10]))
