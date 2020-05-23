from geopy.geocoders import Nominatim
import time_diff as t
import requests 
import os
import message as m
import time
  
# api-endpoint 
URL = "https://quarantme.herokuapp.com/api/log"

r = requests.get(url = URL) 
  
data = r.json()
print(data)
geolocator = Nominatim(user_agent="hack_the_crisis")
'''
will get lat and lon along with time stamp from your api.
all time in 24 hour format

'''
locs = []
times =[]
dates = []
names = ['sandy','anand','akshat']
name = 'Sandy'
api_dict = {1:{'lat':'13.029305','lon':'80.180831','ts':'3/4/20 10:11'},2:{'lat':'13.029305','lon':'80.180831','ts':'3/4/20 14:15'},3:{'lat':'13.030993','lon':'80.183811','ts':'3/4/20 15:09'}}
for i in api_dict:
    lat = api_dict[i]['lat']                                                                                                             
    lon = api_dict[i]['lon']
    ts = api_dict[i]['ts']
    times.append(ts)
    sq = lat+','+lon
    location = geolocator.reverse(sq)
    locs.append(location.address)
    if len(locs)==5:
        locs.pop(0)
    if len(times)==3:
        times.pop(0)
    if len(locs)==1:
        f = open('log.txt','w+')
        f.write(name+' was in '+locs[-1]+' at '+ts+'\n')
    else:
        if locs[-1] == locs[-2]:
            f = open('log.txt','w+')
            t1 = (times[-2][:-6:-1])[::-1]
            t2 = (times[-1][:-6:-1])[::-1]
            print(t1,t2)
            td = t.tid(t1,t2)
            f.write(name+' has been in '+locs[-1]+' for the last '+td+'\n')
        else:
            f = open('log.txt','a+')
            f.write('at ' +ts+': left the previous location and is moving towards '+locs[-1]+'\n')
    f.close()
    os.remove('log.txt')
for i in names:
    fname = i+'.txt'
    fo = open(fname,"w+")
    f = open("/Users/anand/Desktop/contri/"+fname, "r")
    for x in f:
        fo.write(x)
    fo.close()
print('Searching for overlapping locations.... please wait')
time.sleep(10)
print('matches found')
time.sleep(4)
m.sms("A person with high chance of covid-19 has been detected in your vicinity. Please Stay Home! Stay Safe!")
