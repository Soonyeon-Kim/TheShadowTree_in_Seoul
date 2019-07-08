from datetime import date, timedelta


def date_cal(start_date, end_date):
    d1 = date(int(start_date.split('-')[0]),int(start_date.split('-')[1]),int(start_date.split('-')[2]))
    d2 = date(int(end_date.split('-')[0]),int(end_date.split('-')[1]),int(end_date.split('-')[2]))

    delta = d2 - d1

    datelist = []
    for i in range(delta.days + 1):
        a = str(d1+timedelta(days=i))
        a = a.replace('-','.')
        
        datelist.append(a)
    return datelist

