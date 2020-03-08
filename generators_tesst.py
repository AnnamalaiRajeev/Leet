

def gen_1():
    for i in range(100):
        yield


def gen_2():
    yield from gen_1()


if __name__ == "__main__":
    y = gen_2()
    for element in gen_2():
        print(element)


