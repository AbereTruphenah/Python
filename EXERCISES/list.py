def alice_wins(nums):
    single_digits=[]
    double_digits=[]
    for num in nums:
        if 0<=num<10:
            single_digits.append(num)
        elif 10<=num<100:
            double_digits.append(num)
    
    alice_single=sum(single_digits)
    alice_double=sum(double_digits)
    bob_single=sum(single_digits)
    bob_double=sum(double_digits)
    
    alice_wins_singles=alice_single>bob_double
    alice_wins_doubles=alice_double>bob_single
    
    return alice_wins_singles or alice_wins_doubles

nums=[1,2,3,4,10]

print(alice_wins(nums))
            



