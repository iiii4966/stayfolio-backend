from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
import sys
import urllib.request
import json
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','we_r_bnb.settings')
django.setup()

from place.models  import Place, Room

#main_url = 'https://www.stayfolio.com/'
main_url = 'https://booking.stayfolio.com/places/soohwarim'

driver = wd.Chrome(executable_path='./chromedriver')
driver.get(main_url)

driver.implicitly_wait(10)
place_name = driver.find_element_by_css_selector('.left-title').text
room_title = driver.find_element_by_css_selector('.room-title').text
room_name = driver.find_element_by_css_selector('.room-name').text
room_description = driver.find_element_by_css_selector('.room-desc').text
room_info = driver.find_element_by_css_selector('.room-semi-info-wrapper').text

new_room = Room.objects.create(
    name = room_title,
    room_type = room_name,
    description = room_description,
    detail = room_info,
)
print(new_room)

place = Place.objects.get(name = place_name)
place.room_info = new_room
place.save()
print(place.name)

driver.close()
driver.quit()
sys.exit()

#raw_data = soup.text
#json_dict = json.loads(raw_data)
#new_place_title = json_dict['place']['name_kr']
#new_identifier = json_dict['identifier']
#new_title = json_dict['title']
#new_subtitle = json_dict['subtitle']
#new_description = json_dict['description']
#new_main_image_url = json_dict['main_image_url']
