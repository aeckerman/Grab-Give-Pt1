import urllib
from xml.etree.ElementTree import parse

doc = parse('rt22.xml')

for bus in doc.findall('bus'):
	direction = bus.findtext('d')
	lat = float(bus.findtext('lat'))
	lon = float(bus.findtext('lon'))
	busid = bus.findtext('id')

def dataT():
	print ("Direction:\n%s" % (direction))
	print ("Latitude:\n%s" % (lat))
	print ("Longitude:\n%s" % (lon))
	print ("Bus ID:\n%s" % (busid))

dataT()