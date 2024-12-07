#prints the previous number, current number and their sum
previousNum = 0
for i in range(1,6):
    
    sum = previousNum + i
    print("the previous num is", previousNum, "the current number is", i, "their sum is", sum)
    previousNum = i