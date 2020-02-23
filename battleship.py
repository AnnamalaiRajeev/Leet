def next_clock(clock):
    time = clock.split(":")
    hours,min = int(time[0], time[1])
    x = 0
    while x< 5: # define true later on
        if min == 59:
            if hours == 23:
                hours = 00
            else:
                hours += 1

        else:
            min += 1
        x += 1






clock = "17:35"