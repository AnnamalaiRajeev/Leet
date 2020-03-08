cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity = 20


def max_duffel_bag_value(cake_tuples, capacity):
    price_per_pound = {}
    for cake in cake_tuples:
        price_per_pound[cake] = cake[1]/cake[0]
    cake_tuples.sort(key=lambda x : price_per_pound[x], reverse=True) #nlogn
    i = 0
    bag_weight = 0
    empty_space = capacity
    while empty_space >= 0 and i <= len(cake_tuples)-1:  # iterate from 0 elemen n-1 # O(n)
        if cake_tuples[i][0] > empty_space:
            i += 1
            continue
        if cake_tuples[i][0] <= empty_space:
             wieght_added = (empty_space // cake_tuples[i][0]) * cake_tuples[i][0]
             bag_weight += wieght_added
             print(cake_tuples[i], (empty_space // cake_tuples[i][0]))
             empty_space = empty_space - wieght_added
        i+= 1


















max_duffel_bag_value(cake_tuples,capacity)