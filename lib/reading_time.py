import math
def reading_time(text, speed=200):
    words = text.split()
    time = math.ceil(len(words) / speed)
    statement = f"{time} mins"
    if time == 1:
        statement = statement.replace("s","")


    return statement