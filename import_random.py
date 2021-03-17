# 產生一個隨機整數1~100(不要印出來)
# 讓使用著重複輸入數字去猜
# 猜對的話 印出 "終於猜對了！"
# 猜錯的話 要告訴他 比答案大還是小

import random

r = random.randint(1, 100)
r = str(r)
rn = input('請猜一個數字: ')

while True:
    if r == rn:
        print('終於猜對了！')
        break
    elif rn < r:
        print('你的數字比答案小')
    else:
        print('你的數字比答案大')
    rn = input("請猜一個數字")

