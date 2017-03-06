import time

def test():
    x = time.time()%30
    if x < 15: return ""
    else: return "Time is %s" % x
