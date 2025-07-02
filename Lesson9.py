# while Loop, for loop(for counter in (x,range,step)
# Timer Clock App
# Time library
import time

# Create a integer variable for user input
alarm_time = int(input("Please enter the time(seconds): "))

# for loop with the user input that counts backward toward till the output display. Time decrement by one second
# with input mod by 60 seconds in a minute and then mod again for 60 minutes in an hour then also with the hour
for x in range(alarm_time, 0, -1):
    time.sleep(1)
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

# Print the string to on-screen display
print("It is time!")