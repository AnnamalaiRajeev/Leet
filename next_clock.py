from fab import profiler

@profiler
def next_clock(time):
    hash_map ={}
    for char in time:
        hash_map[char] = True
    time = time.split(":")
    _hours, _min = int(time[0]), int(time[1])

    while True:
        if _min == 59:
            if _hours == 23:
                _hours = 0
            else:
                _hours += 1
            _min = 0
        else:
            _min += 1

        if _hours < 10:
            _hours = '0' + str(_hours)
        if _min < 10:
            _min = '0' + str(_min)

        string = str(_hours) + ":" + str(_min)
        _true = True
        for char in string:
            if char not in hash_map:
                _hours, _min = int(string.split(":")[0]), int(string.split(":")[1])
                _true = False
                break

        if _true is False:
            continue

        elif _true is True:
            return str(_hours)+":"+str(_min)



# l=["00:00", "10:00", "11:11"]
# results = map(next_clock, l)
# print(results)
# print(list(results))