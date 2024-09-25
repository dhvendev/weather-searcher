import datetime


def give_png(time):
    time_now = datetime.datetime.fromtimestamp(int(time)).time()
    if datetime.time(0, 0) <= time_now <= datetime.time(3, 0):
        return '00-03.png'
    elif datetime.time(3, 0) <= time_now <= datetime.time(5, 0):
        return '03-05.png'
    elif datetime.time(5, 0) <= time_now <= datetime.time(7, 0):
        return '05-07.png'
    elif datetime.time(11, 0) <= time_now <= datetime.time(16, 0):
        return '11-16.png'
    elif datetime.time(16, 0) <= time_now <= datetime.time(19, 0):
        return '16-19.png'
    elif datetime.time(19, 0) <= time_now <= datetime.time(21, 0):
        return '19-21.png'
    elif datetime.time(21, 0) <= time_now <= datetime.time(0, 0):
        return '21-00.png'
    else:
        return '21-00.png'
