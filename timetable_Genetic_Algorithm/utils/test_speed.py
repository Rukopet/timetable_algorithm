import time

start_time = time.time()

test = {1: None, 3: None}
for _ in range(1000000):
    # sum(map(None.__eq__, test.values()))
    list(test.values()).count(None)
print("--- %s seconds ---" % (time.time() - start_time))

