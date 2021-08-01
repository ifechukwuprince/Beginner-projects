#! python3

import sys, random
# Generates password


def password_g():
    print('''
    ---------------------------------------
    Password must be 8digits
    Must contain Capital letter atleast 1
    Must contain Number
    Must contain atleast special characters
    ---------------------------------------
    ''')

    user_p = input('Enter password: ')

    check, s_chr, alpha, capi, num  = ('!','@','#','$','%','^','&','*','(',')','_','+'),[],[],[],[]

    if user_p:
        for i in user_p:
            if i in check:
                s_chr.append(i)

        for t in user_p:
            if t.isalpha():
                alpha.append(t)
        
        for n in user_p:
            if n.isnumeric():
                num.append(n)

        for c in user_p:
            if c.isupper():
                capi.append(c)               
    else:
        print('Empty Field!')
        sys.exit()

   
    # Lets generate password for the user
    l = 'abcdefghijklmnopqrstuvwxyz','abcdefghijklmnopqrstuvwxyz'.upper(),'0123456789','!@#$%^&*()_+-'
    r_sa = []
    for i in l:
        r_sam = sorted(random.sample(i, 3))
        r_sa += r_sam
    
    r_ch = random.sample(r_sa, k = random.randrange(8, 12))
    r_ch = ''.join(r_ch)



    if s_chr == []:
        print('special chr missing\n-------------------\nsuggested Password : '+ r_ch)
    elif alpha == []:
        print('No alphabet\n-------------------\nsuggested Password : '+ r_ch)
    elif num == []:
        print('No number\n-------------------\nsuggested Password : '+ r_ch)
    elif capi == []:
        print('Capital letter Missing\n-------------------\nsuggested Password : '+ r_ch)
    elif (len(s_chr+alpha+num+capi) < 8):
        print('Not accurate\n-------------------\nsuggested Password : '+ r_ch)
    else:
        print('Accurate Password!')


    


        

        




if __name__ == '__main__':
    password_g()