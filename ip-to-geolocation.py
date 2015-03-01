#Tutorial : http://www.idiotinside.com/2015/02/05/find-geolocation-of-an-ip-address-using-php-and-python/

import urllib2
import json

def getIPAddress(api_key,ip_address):
    api_endpoint = "http://api.ipinfodb.com/v3/ip-city/?key=" +api_key+"&ip="+ip_address+"&format=json"
        try:
            api_response = urllib2.urlopen(api_endpoint)
                try:
                    return json.loads(api_response.read())
                except (ValueError, KeyError, TypeError):
                    return "JSON format error"

    except IOError, e:
        if hasattr(e, 'code'):
            return e.code
                elif hasattr(e, 'reason'):
                    return e.reason

api_key = "YOUR_API_KEY"
ip_address = "IP_ADDRESS"

data = getIPAddress(api_key,ip_address)
#print data
if data['statusCode'] == "OK":
    print "IP: "+ ip_address
        print "API Status:"+ data['statusCode']
        print "Country:"+ data['countryName']
        print "Region:"+ data['regionName']
        print "City:"+ data['cityName']
        print "Latitude:"+ data['latitude']
        print "Longitude:"+ data['longitude']
else:
    print data['statusCode']
        print data['statusMessage']
