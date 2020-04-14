import random


k=random.randint(0,101)
chances=1
while(chances <= 10):
    n=int(input('Please enter a number :'))
    print(str(k)+'\n')
    if(n == k):
        print('Yes.you won!')
        break
    elif(n < 0):
        print('Please enter greater than 0!')
    elif(n > 100):
        print('Number must be under 10')
    elif(n > 50 and k < 50):
        print('Please try a number below 50')
    elif(n > 30 and k < 30):
        print('Please enter a number below 30')
    elif(n > 70 and k < 70):
        print('Please enter a number below 70')
    print('Sorry.Not correct!' + '\n')
    chances=chances+1
    
    



