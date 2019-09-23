data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 100000 == 0:
            print(len(data))

sum_len = 0
for d in data:
    sum_len += len(d)

print('檔案讀取結束，總共有', len(data), '筆資料')
print('平均每筆資料長度為', sum_len / len(data))

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('共有', len(new), '筆留言長度小於100')