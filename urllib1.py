import urllib3, json

http = urllib3.PoolManager()
end_point = "http://api.openweathermap.org/data/2.5/weather" 
appid = "2bc3e79bb974a007818864813f53fd35"
urls = [end_point+"?q=Nairobi&units=metric&appid="+appid, end_point+"?q=Lagos&units=metric&appid="+appid, end_point+"?q=London&units=metric&appid="+appid]
print 
print ("City".ljust(16)), 
print ("Temp".ljust(16)), 
print ("Description".ljust(16))
print("-"*60)
for x in urls:
    result = http.request("GET", x)
    data = json.loads(result.data)
    print (data['name'].ljust(16)),
    print (str(data['main']['temp']).ljust(16)),
    print (str(data['weather'][0]['description']).ljust(16))
    print 
    
    
#https://api.openweathermap.org/data/2.5/weather?
#http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=b1b15e88fa797225412429c1c50c122a1
#http://api.openweathermap.org/data/2.5/weather?id=2172797&appid=2bc3e79bb974a007818864813f53fd35