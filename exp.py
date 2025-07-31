import datetime
def exp():
    print(int(datetime.datetime.today().strftime("%H")))

    x="2025-07-30 06:00"
    format = '%Y-%m-%d %H:%M'
    dt = datetime.datetime.strptime(x, format)
    print(int(dt.strftime("%H")))


if __name__=="__main__":
    exp()