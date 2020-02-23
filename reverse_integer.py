# x belongs to [-2^31, 2^31 - 1]
def multiple(a,b):
    sum_array = [] # store the sum for each unit place multiplication
    for i,value in enumerate(reversed(b)):
        if i > 0:
            number_of_trailing_zeroes = i*10
        for 




