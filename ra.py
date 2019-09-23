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

# 關鍵字搜尋
q = input('是否進行關鍵字搜尋？')
if q == 'yes':
    while True:
        x = input('請輸入欲查詢關鍵字')
        key = []
        for d in data:
            if x in d:
                key.append(d)
        print('總共有', len(key), '筆資料符合關鍵字', x)
        rq = input('是否換下個關鍵字？')
        if rq == 'no':
            break
        