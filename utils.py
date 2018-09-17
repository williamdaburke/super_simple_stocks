from __future__ import division
import datetime

def minutes_ago(mins): return datetime.datetime.now() - datetime.timedelta(minutes=mins)

def wavg(group, avg_name, weight_name):
    d = group[avg_name]
    w = group[weight_name]
    try:
        result = (d * w).sum() / w.sum()
    except ZeroDivisionError:
        result = d.mean()
    return round(result,3)

geomean = lambda a: round(a.prod()**(1.0/len(a)),3)

cap = lambda x: x.lower().capitalize()