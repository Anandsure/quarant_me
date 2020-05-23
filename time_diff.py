#2:15 10:11
def tid(t1,t2):
    h1 = int((t1[-4::-1])[::-1])
    h2 = int((t2[-4::-1])[::-1])
    m1 = int((t1[-1:-3:-1])[::-1])
    m2 = int((t2[-1:-3:-1])[::-1])
    #print(t1,t2)
    if h2 < h1:
        hours = 24+(h2-h1)
    else:
        hours = h2 - h1
    if m2 >= m1:
        mins = m2 - m1
    else:
        mins = 60+(m2-m1)
        hours-=1
    #print('Time diff is: ',hours,' hours and ',mins,' mins')
    tot = hours*60 + mins
    return str(tot)+' mins'

if __name__ == '__main__':
    y = tid('10:15','2:00')
    print(y)
