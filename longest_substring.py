
s = "abcabcbb"

# make hash map store the variables with count
# count = len(hash_map)Q
# if hash_map(
print(list(set("ykkj")))
print(len("abababc"))


def get_string(s):
    hashmap = {}
    for i in range(0, len(s)):
        for j in range(i+1, len(s)+1):
            sub_string = s[i:j]
            if len(set(sub_string)) == len(sub_string):
                if hashmap.get(sub_string, False):
                    hashmap[sub_string] += 1
                else:
                    hashmap[sub_string] = 1

    print(hashmap)
    key = max(hashmap, key= lambda x: len(x))

    return key


y = get_string("abcabdeabcdabcabc")
print(y)

