

def give_array(array):
    hash_map = {}
    for number in array:
        if hash_map.get(number, False):
            hash_map[number] += 1
        else:
            hash_map[number] = 1
    return max(hash_map, key=hash_map.get)

y = give_array([1,2,3,4,5,5,6])
print(y)



def yo():
    hashmap = {"1": [5, 6, 4], "2": [3, 4]}
    y = sorted(hashmap, key=lambda x: hashmap[x][1])
    print(y)
    print(max([5,3,4], [3,4]))

