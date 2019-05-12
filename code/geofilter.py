import json
from shapely.geometry import shape, Point

# load GeoJSON file containing sectors
with open('madrid.json') as f:
    js = json.load(f)
# construct point based on lon/lat returned by geocoder
point = Point(-3.695526123046875, 40.4166327886885)


# check each polygon to see if it contains the point
def point_in_polygon(js, point):
    for feature in js['features']:
        polygon = shape(feature['geometry'])
        if polygon.contains(point):
            return True
        else:
            return False

if(point_in_polygon(js, point)):
    print('Point is contained in area')