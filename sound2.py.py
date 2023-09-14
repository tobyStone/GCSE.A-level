import winsound


def sound():
 
    frequency = 370
    duration = 670
    number = 40
    for i in range (number):
        winsound.Beep(frequency, duration)
        frequency = frequency + 50
        print("should be beeping")

sound()