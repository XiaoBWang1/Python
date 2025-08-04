""" time library
    import datetime
    datetime.date.today()
    datetime.time(_,_,_)
    datetime.datetime.now()
    now.strftime(%H:%M:%S %m-%d-%Y)
    datatime.datatime()
"""

# Alarm Sound Clock Application
import time
import datetime
import pygame

# Create a function for the alarm action with a formatted print display of the alarm time follow by a Bool for
# the on state of the alarm clock while adding a mp3 file with its absolute path.
def time_set(alarm):
    print(f"Alarm time set at: {alarm}")
    alarm_sound = "C:\\Users\\xbw24\\Desktop\\Python\\Effects\\Morning_Alarm.mp3"
    running = True

# While loop with Boolean that sets the current time in a formatted string that displays it
    while running:
        real_time = datetime.datetime.now().strftime("%H: %M: %S")
        print(real_time)
        if real_time == alarm:
            print("Wake up!")
            running = False
        time.sleep(1)

# Dunder main method consists of a user input for setting alarm time along with the time set method function and
# the alarm argument pass
if __name__ == "__main__":
    alarm = input("Set the time(HH:MM:SS): ")
    time_set(alarm)



