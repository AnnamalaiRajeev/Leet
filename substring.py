
s = "abcabcbb"

# make hash map store the variables with count
# count = len(hash_map)Q
# if hash_map(
print(list(set("ykkj")))
print(len("abababc"))


def get_string(s, minlength, maxlength, maxunique):
    hashmap = {}
    for i in range(0, len(s)):
        for j in range(i+1, len(s)+1):
            sub_string = s[i:j]
            if maxlength >= len(sub_string) >= minlength:
                if len(set(sub_string)) == len(sub_string):
                    if len(sub_string) <= maxunique:
                        if hashmap.get(sub_string, False):
                            hashmap[sub_string] += 1
                        else:
                            hashmap[sub_string] = 1

    print(hashmap)
    key = max(hashmap, key=hashmap.get)

    return hashmap[key]


y = get_string("abcabdeabcdabcabc",2,4,26)
print(y)

