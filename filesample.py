#!/usr/bin/env python3

import sys

#for k, v in enumerate(sys.argv):
#    print(k, v)

#f = open("jsontest", mode="r", encoding="utf-8")

# for k, v in enumerate(sys.argv):
#    print(f.read())
#    #f.write("test{k}:{v}\n".format(k=k,v=v))

# f.close()

with open("jsontest", mode='rb+') as fp:
    fp.seek(0)
    print(fp.tell())
    fp.seek(-10,2)
    print(fp.tell())
    # readlineはseek位置から改行までの１行を表示
    s = fp.readline()
    print(s)
