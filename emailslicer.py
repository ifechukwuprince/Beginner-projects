#! python3

# == My third beginner project ==

'''
    This is a program that slice Email eg ifecogltd@gmail.com 
    returns:
    username = ifecogltd
    hostname = gmail.com
    Version 0.0.1
'''


def email_slicer():
    u_mail = input('Enter Email: ')
    if '@' in u_mail:
        username = u_mail[:u_mail.index('@')]
        hostname = u_mail[u_mail.index('@')+1:]
        print('Username: {0}\nHostname: {1}'.format(username, hostname))
    else:
        print('Your Email is not Valid!')




if __name__ == '__main__':
    email_slicer()