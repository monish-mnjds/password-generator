import random
for i in range(1):
    s="1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    passlen=16
    p="".join(random.sample(s,passlen))
    print(p)
