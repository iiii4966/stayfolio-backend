import urllib.request as req
import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "we_r_bnb.settings")
import django
django.setup()
from magazines.models import Magazines, Contents


url_list = []
url_api_pre = 'https://www.stayfolio.com/api/v1/magazines/'
url_details = ['stay-sodo', 'fusion-resort-cam-ranh', 'sohsul53', 'fusion-suites-sai-gon', 'jocheonmasil', 'stay-beyond', 'fusion-resort-phu-quoc', 'hotel-cappuccino', 'Alveolus-Mangwon', 'aroundfollie_magazine', 'owall-hotel', 'nagwonjang', 'ikkoinstay', 'bengdi-1967', 'gagopa-home', 'jocheondaek', 'gurume', 'baguni-hostel-Suncheon', 'hosidam', 'hotel-sohsul', 'mungzip', 'pyeongdae-panorama', 'nookseoul', 'ihwaruae', 'b-ahn', 'goi', 'blindwhale', 'chang-shin-creativehouse', 'Casadelaya', 'framehouse', 'tori-x-kaareklint', 'hotel-shinshin', 'kyung-sung', 'small-house-big-door', 'jun-hanok-guest', 'ma-maison', 'zeroplace', 'onsaka-no-ie', 'Gomsk', 'soohwarim']
url_pre = 'https://www.stayfolio.com'

for url_detail in url_details:
    url = url_api_pre + url_detail
    url_list.append(url)

for url in url_list:
    res = req.urlopen(url).read().decode('utf-8')
    res_json = json.loads(res)
    magazine = Magazines(
                    title = res_json['title'],
                    title_image_url = url_pre + res_json['title_image_url'],
                    title_text_image_url = url_pre + res_json['title_text_image_url'],
                    identifier = res_json['identifier'],
                    description = res_json['description'],
                    intro = res_json['intro'],
                    main_image_url = url_pre + res_json['main_image_url'],
                    footer_image_url = url_pre + res_json['footer_image_url'],
                    link_btn_title = res_json['link_btn_title'],
                    link_btn_url = res_json['link_btn_url'],
                    logo_url = url_pre + res_json['logo_url'],
                    )
    magazine.save()
