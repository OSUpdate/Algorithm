import datetime

def solution(lines):
    answer = 0
    sDate , sTime, sT = lines[0].split()
    print(sDate+" "+sTime)
    first = datetime.datetime.strptime(sDate+" "+sTime,"%Y-%m-%d %H:%M:%S.%f")
    for line in lines:
        d,s,t = line.split()
        data = datetime.datetime.strptime(d+" "+s,"%Y-%m-%d %H:%M:%S.%f")
        t = t[:-1]
        sec, mile = t.split('.')
        start = data- datetime.timedelta(seconds=int(sec),microseconds=int(mile))
        print(data.strftime("%Y-%m-%d %H:%M:%S.%f"), )
        print(s,t)
    return answer

solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
])