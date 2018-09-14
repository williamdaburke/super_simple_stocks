from __future__ import division


def div_yield(symbol,price):
    return self.dividend / float(price)

def p_e_ratio(symbol,price):
    return float(float(price) / self.dividend)

def wavg(group, avg_name, weight_name):
    d = group[avg_name]
    w = group[weight_name]
    try:
        return (d * w).sum() / w.sum()
    except ZeroDivisionError:
        return d.mean()

    