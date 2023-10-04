#flow control week 3

# current = 8
# end = 88
# while current < end:
#     print(current)
#     current = current + 2

# for a in range(2,100,2):
#     print(a)
    
#a function is a predefined algorithm: someone else has already written a series of statements to solve a certain problem

n = input("put a number here")
#my input will be 10
currentoddNumber = 1
#oddCount is an iterating variable
for oddCount in range(int(n)):
    print(currentoddNumber)
    #this is updating the current odd number
    currentoddNumber = currentoddNumber + 2