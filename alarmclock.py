#! python3

from datetime import datetime


# My Second beginner project
# To make it more advanced i will introduce re module in version 0.0.2
'''
    This is a program that sets alarm and plays sounds once it time
    Version 0.0.1
'''

def alarm_clock():
    print('Enter Alarm Clock[HH:MM:AM|PM] \n')
    ui = input('TIME: ')
    alarm_hour = ui[:2]
    if alarm_hour.startswith('0'):
        alarm_hour = ui[1]


    alarm_min = ui[3:5]
    if alarm_min.startswith('0'):
        alarm_min = ui[4]


    alarm_period = ui[6:]


    #=== I need to write a code that compares the two time ====
    stop = False
    
    while stop == False:

        current_time = datetime.now()
        c_hour = current_time.hour
        c_min = current_time.minute
        c_period = current_time.strftime('%p')


        if (alarm_hour, alarm_min, alarm_period.upper()) == (str(c_hour), str(c_min), str(c_period)):
            print('Time Reached')
            stop = not(False)

            


        



if __name__ == '__main__':
    alarm_clock()