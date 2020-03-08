import time

start = time.time()

while True:
    if time.time() - start >= float(2):
        break
    print('yo')
