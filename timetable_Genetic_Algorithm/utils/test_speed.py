import time

start_time = time.time()


def suuum(a, b): return a + b


test = {1: None, 3: None}
# for _ in range(1000000):
[suuum(i, i + 1) for i in range(10000000)]
# for i in range(10000000):
#     suuum(i, i + 1)
print("--- %s seconds ---" % (time.time() - start_time))
