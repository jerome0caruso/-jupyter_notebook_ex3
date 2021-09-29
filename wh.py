# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i if non of the above conditions are true.
 
def fizzBuzzFn(n):
    myList = []
    for i in range(1, n +1):
        if i % 3 == 0 and i % 5 == 0:
            myList.append("FizzBuzz")
        elif i % 3 == 0:
            myList.append("Fizz")
        elif i % 5 == 0:
           myList.append("Buzz") 
        else:
            myList.append(str(i))           
    return(myList)
# Input: n = 3
# Output: ["1","2","Fizz"]

print(fizzBuzzFn(3))

# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
print(fizzBuzzFn(5))

# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
print(fizzBuzzFn(15))