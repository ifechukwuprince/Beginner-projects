#! python3

import random

''' 
    This is game of 'paper','book','character', you should be able to guess correctly what the unknown
    holds
'''



# attempt increase if score reaches 10
def game():

    trial = 4
    score = 0

    while trial != 1:
        gamelist = 'Paper','Character','Book'
        gamelist = random.choice(gamelist)
        
        print('You have '+ str(trial) +' attempt')
        print('Attempt will be increase once your score 10 :)')
        print('----------------------------------------------')
        ans = input('GUESS WHAT l HAVE: ').title()
        print('Checking Answer...')
        if ans != gamelist:
            print('You scored: ',score)
            trial -= 1
            if trial == 1: print('Game over')
        
        else:
            score += round(random.randint(1, 7))
            print('You scored: ', score)
            if score >= 10: 
                print('Trial increased')
                trial += 1
                score = 0
            
            









if __name__ == '__main__':
    game()