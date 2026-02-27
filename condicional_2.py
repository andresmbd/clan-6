import datetime
rightnow = datetime.datetime.now()
day_of_week = rightnow.weekday()
hour_day = rightnow.hour

weekend = day_of_week > 5

print(f"Hey! It's {hour_day}:00")

if weekend:
    if hour_day < 10:
        print("go to sleep!! Its Weekend!!!")
    elif 10 <= hour_day <= 17:
        print("I recommend you to walk, wacth movies/serires,")

    else:
        print("go rest, you had a productive day")

else:
    if hour_day < 8:
        print("wake up, have your breakfast,do exersice so you get energy!!")
    elif 8 <= hour_day <= 17:
        print("Study/do your job")
    else:
        print("Go rest tomorrow is another day!")


