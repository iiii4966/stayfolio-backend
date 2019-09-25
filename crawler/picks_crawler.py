from bs4 import BeautifulSoup as bs
import urllib.request
import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','we_r_bnb.settings')
django.setup()

from place.models import Place
from pick.models  import Pick, PickImage

#main_url = 'https://www.stayfolio.com/'
main_url = 'https://www.stayfolio.com/api/v1/picks/55th-street'
html = urllib.request.urlopen(main_url)
soup = bs(html, "html.parser")
raw_data = soup.text
json_dict = json.loads(raw_data)
new_place_title = json_dict['place']['name_kr']
new_identifier = json_dict['identifier']
new_title = json_dict['title']
new_subtitle = json_dict['subtitle']
new_description = json_dict['description']
new_main_image_url = json_dict['main_image_url']

new_images = [url['image']['large'] for url in json_dict['pictures']] 

#new_pick = Pick.objects.create(
#            identifier     = new_identifier,
#            title          = new_title,
#            place_info     = Place.objects.get(name = new_place_title),
#            subtitle       = new_subtitle,
#            description    = new_description,
#            main_image_url = new_main_image_url,
#           )

#print(new_pick)

for image in new_images:
   new_image = PickImage.objects.create(
        image_url = image,
        pick_name = Pick.objects.get(identifier = new_identifier),
    )
print(new_image.pick_name_id)
