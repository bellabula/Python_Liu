# 產生一個隨機整數1~100(不要印出來)
# 讓使用著重複輸入數字去猜
# 猜對的話 印出 "終於猜對了！"
# 猜錯的話 要告訴他 比答案大還是小

import random
start = input('請決定隨機數字範圍開始值: ')
end = input('請決定隨機數字範圍結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
    rn = input('請猜一個數字: ')
    rn = int(rn)
    count += 1 # count = count + 1
    print('這是你猜的第', count, '次')
    if rn == r:
        print('猜對了！')
        break
    elif rn < r:
        print('你的數字比答案小')
    else:
        print('你的數字比答案大')