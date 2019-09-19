import ast
import urllib.request as req
import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "we_r_bnb.settings")
import django
django.setup()
from magazines.models import Magazines, Contents, ContentType


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
    contents = res_json['contents']

    for content in contents:
        description = []

        if content['content_type'] == 'why' or content['content_type'] == 'location':
            description_dict = ast.literal_eval(content['description'])
            headers = description_dict['header'].split("\n")
            image_url = ''
            
            if description_dict.get('picture', '') == '':
                image_url = ''
            else:
                image_url = url_pre + description_dict['picture']

            for t in description_dict['text']:
                t = t.split("/n/n")

                for text in t:
                    description.append(text)
    
            content_data = Contents(
                    content_type = ContentType.objects.get(c_type=content['content_type']),
                    header = headers,
                    description = description,
                    image_url = image_url,
                    magazine = Magazines.objects.get(identifier=res_json['identifier'])
                    )
            content_data.save()

        elif content['content_type'] == 'people':
            description_dict = ast.literal_eval(content['description'])
            headers = description_dict['header'].split("\n")
            image_url = url_pre + description_dict['footer_img_url']

            for t in description_dict['text']:
                t = t.split("/n/n")

                for text in t:
                    description.append(text)
    
            content_data = Contents(
                    content_type = ContentType.objects.get(c_type=content['content_type']),
                    header = headers,
                    description = description,
                    image_url = image_url,
                    magazine = Magazines.objects.get(identifier=res_json['identifier'])
                    )
            content_data.save()
