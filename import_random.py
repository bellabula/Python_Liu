# 產生一個隨機整數1~100(不要印出來)
# 讓使用著重複輸入數字去猜
# 猜對的話 印出 "終於猜對了！"
# 猜錯的話 要告訴他 比答案大還是小

import random

r = random.randint(1, 100)
while True:
    rn = input('請猜一個數字: ')
    rn = int(rn)
    if rn == r:
        print('猜對了！')
        break
    elif rn < r:
        print('你的數字比答案小')
    else:
        print('你的數字比答案大')