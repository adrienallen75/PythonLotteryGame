
import random 

class Lottery:
    
    def generate(self):
        x1 = random.randint(0,10)
        x2 = random.randint(0,10)
        x3 = random.randint(0,10)   
        x4 = random.randint(0,10)
        x5 = random.randint(0,10)
        
        lottery_nums = []
        
        user_list = []
        
        for i in range(0,5):
            x = random.randint(1,10)
            lottery_nums.append(x)
        
        print("enter five numbers through 1-10 for a chance to win the lottery!:")
        
        
        for i in range(0,5):
            i = int(input())
            user_list.append(i)
        
        print("the winning lottery numbers are:")
        print(lottery_nums)
        
        print("the numbers you've entered are")
        print(user_list)
        
        if user_list == lottery_nums:
            print("you've won the lotterry")
        else:
            print("you've lost the lottery try again!")
            


l = Lottery()

l1 = l.generate()
