import requests
#construct the url
base_url='https://www.autotrader.co.uk/car-search?search-target=usedcars&radius=&onesearchad=Used&onesearchad=Nearly%20New&onesearchad=New'
# queries
qlist= {
        'make':'&make=MAZDA',
        'model':'&model=+MX-5',
        'priceFrom':'&price-from=',
        'priceTo':'&price-to=',
        'year':'&year-from=',
        'mileage_max':'&maximum-mileage=',
        'fuel':'&fuel-type=',
        'engineSize':'&maximum-badge-engine-size=',
        'transmission':'&transmission=',
        'postecode':'&postcode=ec1n7ub'
    }
path=''
lenght=len(qlist)

for i in qlist.keys():
    path+=qlist[i]
print(path)

url = base_url+path
print(url)
r = requests.request('GET', url, verify=False)

print(r.text)
#add header
#headers={'x-auth-token': '6e217b67987548fab963f0aad73497ef'}

#make the http GET request
#r = requests.request('GET', url, headers=headers, verify=False)