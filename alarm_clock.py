import datetime
import time
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")

    sound_file = "assets/my_music.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)

    is_running = True
    
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        # print("Current Time: " + current_time, end='\r')

        if current_time == alarm_time:
            print("⏰ Wake Up!")

            pygame.mixer.music.play()
            time.sleep(30)
            pygame.mixer.music.stop()

            is_running=False

        time.sleep(1)


if __name__=="__main__":
    print("===== Alarm Clock (Terminal-Based) =====")
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)
