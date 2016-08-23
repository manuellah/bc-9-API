import urllib3, json


def urllib3_test():
    http = urllib3.PoolManager()
    end_point = "http://api.openweathermap.org/data/2.5/weather" 
    appid = "2bc3e79bb974a007818864813f53fd35"
    urls = [end_point + "?q=Nairobi&units=metric&appid=" + appid, end_point + "?q=Lagos&units=metric&appid=" + appid, end_point + "?q=London&units=metric&appid=" + appid]
    my_format_list = ["\n City".ljust(16), "Temp".ljust(16), "Description".ljust(16), "\n" + "-" * 60]

    my_header = '{} {} {} {}'.format( "\n City".ljust(16), "Temp".ljust(16), "Description \n", "-" * 60)

    print my_header
    for x in urls:

        result = http.request("GET", x)
        data = json.loads(result.data)
        my_body = '{} {} {} {}'.format( data['name'].ljust(16), str(data['main']['temp']).ljust(16), str(data['weather'][0]['description']).ljust(16), "\n")
        
        print my_body
        

urllib3_test()
