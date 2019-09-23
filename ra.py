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

new = [d for d in data if len(d) < 100]
print('共有', len(new), '筆留言長度小於100')

# 關鍵字搜尋
q = input('是否進行關鍵字搜尋？')
while True:
    if q == 'yes':
        key = input('請輸入欲搜尋之關鍵字： ')
        key_result = [d for d in data if key in d]
        print('總共有', len(key_result), '筆資料符合關鍵字', key)
        rq = input('是否再次搜尋？')
        while True:
            if rq == 'yes':
                break
            elif rq == 'no':
                q = 'no'
                break
            else:
                print('只能輸入yes或no')
                rq = input('請重新選擇是否再次搜尋？')
    elif q == 'no':
        break
    else:
        print('只能輸入yes或no')
        q = input('是否進行關鍵字搜尋？')