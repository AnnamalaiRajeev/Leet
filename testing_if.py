w = 'python'
import time
w_iterator = iter(w)
next(  w_iterator)
start = time.time()
print(time.time())
print(time.time()-start, type(time.time()))