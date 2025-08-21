"""
    time library
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
# the on state of the alarm clock while adding a mp3 file with its absolute path
def time_set(alarm_time):
    print(f"Alarm time set at: {alarm_time}")
    alarm_sound = "C:\\Users\\xbw24\\Desktop\\Python\\Effects\\Morning_Alarm.mp3"
    running = True

# While loop with Boolean that sets the current time in a formatted string that displays it
# initialize the pygame package with the mixer then load the sound file and play it inside a while
# loop with the get busy Boolean function that plays the alarm sound for a while

    while running:
        real_time = datetime.datetime.now().strftime("%H: %M: %S")
        print(real_time)

        if alarm_time == real_time:
            print("Wake up!")

            pygame.mixer.init()
            pygame.mixer.music.load(alarm_sound)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy:
                time.sleep(1)
            running = False

        time.sleep(1)

# Dunder main method consists of a user input for setting alarm time along with the time set method function and
# the alarm argument pass
if __name__ == "__main__":
    alarm_time = input("Set the alarm time(HH:MM:SS): ")
    time_set(alarm_time)

