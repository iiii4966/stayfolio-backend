from bs4 import BeautifulSoup as bs
import urllib.request
import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','we_r_bnb.settings')
django.setup()

from place.models import Place, Style, Target, Amenity, Feature, Tourspot

#main_url = 'https://www.stayfolio.com/'
main_url = 'https://www.stayfolio.com/api/v1/picks/kairosjeju'
html = urllib.request.urlopen(main_url)
soup = bs(html, "html.parser")
raw_data = soup.text
json_dict = json.loads(raw_data)['place']
styles_dict = json_dict['styles']
target_dict = json_dict['targets']
amenities_dict = json_dict['amenities']
tourspots_dict = json_dict['tourspots']
features_dict = json_dict['features']

place_obj = Place.objects.create(
			     name          = json_dict['name_kr'],
			     full_address  = json_dict['address'],
			     zipcode       = json_dict['address_zipcode'],
			     street        = json_dict['address_detail_2'],
			     county        = json_dict['address_detail_1'],
			     city          = json_dict['address_city'],
			     province      = json_dict.get('city'),
			     country       = json_dict['country'],
			     longitude     = json_dict['longitude'],
			     latitude      = json_dict['latitude'],
			     website       = json_dict['website'],
			     facebook      = json_dict.get('facebook',''),
			     instagram     = json_dict.get('instagram',''),
			     phone         = json_dict['phone'],
			     price_min     = json_dict['price_min'],
			     price_max     = json_dict['price_max'],
			     persons_min   = json_dict['passenger_cnt_min'],
			     persons_max   = json_dict['passenger_cnt_max'],
			     room_capacity = json_dict['room_cnt'],
			     check_in      = json_dict['checkin_time'],
			     check_out     = json_dict['checkout_time'],
			)
#place_obj = Place.objects.get(name = json_dict['name_kr'])
for style in styles_dict:
	if Style.objects.filter(styles = style).exists():
		new_style = Style.objects.get(styles = style)
	else:
		new_style = Style.objects.create(styles = style)
	place_obj.styles.add(new_style)

for target in target_dict:
	if Target.objects.filter(targets = target).exists():
		new_target = Target.objects.get(targets = target)
	else:
		new_target = Target.objects.create(targets = target)
	place_obj.targets.add(new_target)

for amenity in amenities_dict:
	if Amenity.objects.filter(amenities = amenity).exists():
		new_amenity = Amenity.objects.get(amenities = amenity)
	else:
		new_amenity = Amenity.objects.create(amenities = amenity)
	place_obj.amenities.add(new_amenity)

for tourspot in tourspots_dict:
	if Tourspot.objects.filter(tourspots = tourspot).exists():
		new_tourspot = Tourspot.objects.get(tourspots = tourspot)
	else:
		new_tourspot = Tourspot.objects.create(tourspots = tourspot)
	place_obj.tourspots.add(new_tourspot)

for feature in features_dict:
	if Feature.objects.filter(features = feature).exists():
		new_feature = Feature.objects.get(features = feature)
	else:
		new_feature = Feature.objects.create(features = feature)
	place_obj.features.add(new_feature)
