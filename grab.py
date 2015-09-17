import urllib

u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
data = u.read()

dataFile = open('rt22.xml', 'wb')
dataFile.write(data)
dataFile.close()

