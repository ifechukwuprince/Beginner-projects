#! python3

import random

'''
    Animal quiz in the sense you need to specify the right answer from the question
'''


def quiz():
    questions = {
        'what animal has the tallest neck ?':'jirraf',
        'what animal is the strongest ?':'lion',
        'what animal eats grass ?':'goat',
        'what animal has colored skin ?':'leopard',
        'what animal has black skin ?':'dog',
        'what animal has shell ?':'snail',
        'what animal has biggest nose ?':'elephant',
        'what animal has human nature ?':'ape',
        'what animal has two leg ?':'fowl',
        'what animal has varities of colour ?':'tiger',
    }


    quiz_len = len(questions.keys())
    score = 0
    name = input('Enter your Name for the exam: ')

    while quiz_len != 0:
        # lets defend questions
        quiz_ = list(questions.keys())
        random.shuffle(quiz_)
        
        for i in range(len(quiz_)):
            correct_ans = questions[quiz_[i]]
            wrong_ans = list(questions.values())
            del wrong_ans[wrong_ans.index(correct_ans)]
            wrong_ans = random.sample(wrong_ans, k = 3)
            options = wrong_ans + [correct_ans]
            random.shuffle(options)
           
            print('Q_'+str(i+1)+' '+quiz_[i])
            for i in range(4):
                print('ABCD'[i].rjust(4)+'. '+options[i])
            ans = input('Answer: ')
            if ans == correct_ans:
                score += 1
                quiz_len -= 1; print('Number of questions remaining: ',quiz_len)
                if quiz_len == 0:
                    if score <= 4:
                        print(f'{name} you scored {score} \nGRADE: FAIL')
                    elif score in range(5, 8):
                        print(f'{name} you scored {score} \nGRADE: GOOD')
                    else:
                        print(f'{name} you scored {score} \nGRADE: EXCELLENT')
        
            elif ans != correct_ans:
                quiz_len -= 1; print('Number of questions remaining: ',quiz_len)
                if quiz_len == 0:
                    if score <= 4:
                        print(f'{name} you scored {score} \nGRADE: FAIL')
                    elif score in range(5, 8):
                        print(f'{name} you scored {score} \nGRADE: GOOD')
                    else:
                        print(f'{name} you scored {score} \nGRADE: EXCELLENT')
        

if __name__ == '__main__': 
    quiz()
