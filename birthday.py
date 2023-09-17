import random

def birth(n):
    count = 0
    for i in range(100):
        y = []
        for i in range(n):
            x = random.randint(1, 366)
            y.append(x)

        if len(y)!=len(set(y)):
            count+=1
    print(count/100)
n=int(input("请输入房间人数："))
birth(n)
