from lxml import html
import requests
import re

def scrub1(list):
    list = map(str, list)
    for i, elem in enumerate(list):
        list[i] = re.sub('\[\'', '', list[i])
    return list
## Can't figure out what character's to put inbetween re.sub for ['']
## Two separate functions for removing [''] not preferable but it works.
def scrub2(list):
    list = map(str, list)
    for i, elem in enumerate(list):
        list[i] = re.sub('\'\]', '', list[i])
    return list

def printAll(name, info, sites, directions, phone, lat, long):
    print('{}\n------------------\n{}\nWalk-up sites: {}\n{}\nPhone number: {}\nGPS Coordinates: {}, {}').format(name, info, sites, directions, phone, lat, long)

## Used just to visualize on mapcustomizer.com
def gps(lat, long, name):
    print('{}, {} {{{}}}').format(lat, long, name)

## Order of campsites is alphabetical
site_info = ['https://www.recreation.gov/camping/alvarado-campground/r/campgroundDetails.do?contractCode=NRSO&parkId=74119',
'https://www.recreation.gov/camping/baby-doe/r/campgroundDetails.do?contractCode=NRSO&parkId=70233',
'https://www.recreation.gov/camping/buffalo-campground/r/campgroundDetails.do?contractCode=NRSO&parkId=70052',
'https://www.recreation.gov/camping/burning-bear-campground/r/campgroundDetails.do?contractCode=NRSO&parkId=109084',
'https://www.recreation.gov/camping/cascade-colorado/r/campgroundDetails.do?contractCode=NRSO&parkId=70042',
'https://www.recreation.gov/camping/chalk-lake/r/campgroundDetails.do?contractCode=NRSO&parkId=70043',
'https://www.recreation.gov/camping/colorado-campground/r/campgroundDetails.do?contractCode=NRSO&parkId=70684',
'https://www.recreation.gov/camping/geneva-park-campground/r/campgroundDetails.do?contractCode=NRSO&parkId=74132',
'https://www.recreation.gov/camping/molly-brown/r/campgroundDetails.do?contractCode=NRSO&parkId=70297',
'https://www.recreation.gov/camping/lakeview-campground/r/campgroundDetails.do?contractCode=NRSO&parkId=70290',
'https://www.recreation.gov/camping/monarch-park/r/campgroundDetails.do?contractCode=NRSO&parkId=70695',
'https://www.recreation.gov/camping/mount-princeton/r/campgroundDetails.do?contractCode=NRSO&parkId=70045',
'https://www.recreation.gov/camping/ohaver-lake/r/campgroundDetails.do?contractCode=NRSO&parkId=70046',
'https://www.recreation.gov/camping/painted-rocks/r/campgroundDetails.do?contractCode=NRSO&parkId=70685',
'https://www.recreation.gov/camping/silver-dollar/r/campgroundDetails.do?contractCode=NRSO&parkId=70598',
'https://www.recreation.gov/camping/timberline-campground/r/campgroundDetails.do?contractCode=NRSO&parkId=73770',
'https://www.recreation.gov/camping/white-star/r/campgroundDetails.do?contractCode=NRSO&parkId=70791'
]

## Same order as above.
campsites = [25, 7, 10, 6, 7, 7, 33, 10, 4, 20, 16, 3, 14, 7, 3, 8, 3]
## Couldn't strip results off table-- likely not 'pure' html. Likely in json format?
## Failed code: xpath('//tr[@class = "2ndweek"]/td[@class = "status w sat"]/text()')
name = []
info = []
city = []
phone = []
latitude = []
longitude = []
directions = []

for site in site_info:
    source = requests.get(site)
    tree = html.fromstring(source.content)
    name.append(tree.xpath("//span[@id = 'cgroundName']/text()"))
    info.append(tree.xpath('//span[@itemprop = "description"]/text()'))
    city.append(tree.xpath("//span[@itemprop='addressLocality']/text()"))
    phone.append(tree.xpath("//span[@itemprop='telephone']/text()"))
    latitude.append(tree.xpath("//div[@itemprop = 'geo']/span[@itemprop = 'latitude']/text()"))
    longitude.append(tree.xpath("//div[@itemprop = 'geo']/span[@itemprop = 'longitude']/text()"))
    directions.append(tree.xpath("//div[@itemprop = 'geo']/text()[6]"))

## Mapping all list content to strings, so they can be manipulated
name = map(str, name)
info = map(str, info)
city = map(str, city)
phone = map(str, phone)
latitude = map(str, latitude)
longitude = map(str, longitude)
directions = map(str, directions)

## Scrubbing all contents of those ['']
name = scrub1(scrub2(name))
info = scrub1(scrub2(info)) ## Some of the descriptions have [""] and aren't scrubbed. Oh well
city = scrub1(scrub2(city))
phone = scrub1(scrub2(phone))
latitude = scrub1(scrub2(latitude))
longitude = scrub1(scrub2(longitude))
directions = scrub1(scrub2(directions))

## Cleaning up a couple of the sections
for i, elem in enumerate(name):
    name[i] = (elem.replace(', CO', '')).title()
for i, elem in enumerate(info):
    info[i] = elem.replace('"', '')
for i, elem in enumerate(city):
    city[i] = elem.capitalize()

## Basic algorithm to cycle through printing of all info for each campsite
i = 0
print("Campgrounds with ample walk-up campsites in the Pike and San Isabel National Forests\n_____________________________________________")
while (i < len(site_info)):
    print(i+1) ## Used for corresponing numbers on map
    printAll(name[i], info[i], campsites[i], directions[i], phone[i], latitude[i], longitude[i])
    print('\n')
    i = i + 1
