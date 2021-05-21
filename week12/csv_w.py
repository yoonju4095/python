import csv

with open('output.csv','w',encoding='utf-8',newline='')as f:
    wr = csv.writer(f)
    wr.writerow(["홍길동", "010-2233-4444", "대전시 유성구"])
    wr.writerow(["이순신", "010-5555-3443", "서울시 영등포구"])
    wr.writerow(["박찬호", "010-5656-7676", "서울시 영등포구"])

f = open('output.csv','r',encoding='utf-8')
lines = csv.reader(f)

f.close()