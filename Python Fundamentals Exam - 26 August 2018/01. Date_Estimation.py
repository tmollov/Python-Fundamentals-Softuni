import datetime

date = list(map(int,input().split('-')))

date1 = datetime.datetime(2018,8,26)
date2 = datetime.datetime(date[0],date[1],date[2])

res = date1 - date2
if res.days == 0:
    print("Today date")
elif res.days > 0:
    print("Passed")
else:
    print(f"{(res.days*-1)+1} days left")