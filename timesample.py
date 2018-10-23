import datetime, time
import csv

t1 = datetime.datetime.now()
print(type(t1))
print(t1)

time.sleep(2)
t2 = datetime.datetime.now()
print(type(t2))
print(t2)

t = t2 - t1
print(type(t))
print(type(t.seconds))
print(t.seconds // 60)

with open("jsontest", encoding='utf-8', mode="r") as f:
    csvline = [i for i in csv.reader(f)]
    print(type(csvline))

print(next(iter(csvline)))
print("start")
for r in csvline:
    print(type(r))
    print(r)

t3 = datetime.datetime.strptime('2018-10-21 19:57:41.479196', '%Y-%m-%d %H:%M:%S.%f')
print(type(t3))
print(t3)
with open("timetest", encoding='utf-8', mode="w") as f:
    f.write(t3.strftime('%Y-%m-%d %H:%M:%S.%f'))
t4 = t1 - t3
print(type(t4))
print(t4)
print(t4.total_seconds()//60)
print(t4.seconds // 60)
