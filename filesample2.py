import datetime
import csv

stat = 'ng'
try:
    with open("jsontest1", mode='r+') as fp:
        l = csv.reader(fp)
        list = next(l)
        pt = datetime.datetime.strptime(list[0], '%Y-%m-%d %H:%M:%S')
        nt = datetime.datetime.now()
        deltat = nt - pt
        list[0] = nt.strftime('%Y-%m-%d %H:%M:%S')
        if stat == "ok":
            list[1] = int(deltat.total_seconds() // 60)
            list[2] = 0
        else:
            list[1] = 0
            list[2] = int(deltat.total_seconds() // 60)
        fp.seek(0)
        w = csv.writer(fp)
        w.writerow(list)
        fp.truncate()

except FileNotFoundError:
    with open("jsontest1", mode="w") as f:
        t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        initial_list = [t, 0, 0]

        dataWriter = csv.writer(f)
        dataWriter.writerow(initial_list)
