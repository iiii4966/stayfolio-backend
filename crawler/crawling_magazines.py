import urllib.request as req
import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "we_r_bnb.settings")
import django
django.setup()

from magazines.models import Magazines, Contents
from place.models     import Place


url_list = []
url_api_pre = 'https://www.stayfolio.com/api/v1/magazines/'
url_details = ['stay-sodo', 'sohsul53', 'jocheonmasil', 'stay-beyond', 'hotel-cappuccino', 'Alveolus-Mangwon', 'aroundfollie_magazine', 'owall-hotel', 'ikkoinstay', 'bengdi-1967', 'gagopa-home', 'jocheondaek', 'gurume', 'baguni-hostel-Suncheon', 'pyeongdae-panorama', 'ihwaruae', 'blindwhale', 'chang-shin-creativehouse', 'zeroplace', 'soohwarim']
url_stayfolio = 'https://www.stayfolio.com'

for url_detail in url_details:
    url = url_api_pre + url_detail
    url_list.append(url)

for url in url_list:
    res = req.urlopen(url).read().decode('utf-8')
    res_json = json.loads(res)
    place = res_json['place']
    place_name = place['name_kr']
    Magazines(
        title                = res_json['title'],
        title_image_url      = url_stayfolio + res_json['title_image_url'],
        title_text_image_url = url_stayfolio + res_json['title_text_image_url'],
        identifier           = res_json['identifier'],
        identifier_kr        = res_json['place']['name_kr'],
        description          = res_json['description'],
        intro                = res_json['intro'],
        main_image_url       = url_stayfolio + res_json['main_image_url'],
        footer_image_url     = url_stayfolio + res_json['footer_image_url'],
        link_btn_title       = res_json['link_btn_title'],
        link_btn_url         = res_json['link_btn_url'],
        logo_url             = url_stayfolio + res_json['logo_url'],
        details              = place['place_type_to_s'] + ' | ' + place['city'] + '/' + place['neighborhood'],
        place                = Place.objects.get(name = place['name_kr'])
    ).save()
