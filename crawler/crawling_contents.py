import ast
import urllib.request as req
import json
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "we_r_bnb.settings")
import django
django.setup()

from magazines.models import Magazines, Contents, ContentType


def make_description_list(prev_list):
    result = []
    step_one_list = []

    for prev_el in prev_list:
        prev_el = prev_el.split(' ')
        while '' in prev_el:
            prev_el.remove('')
        prev_el = ' '.join(prev_el)
        step_one_list.append(prev_el)

    step_two_list = []
    for one in step_one_list:

        if "\n " in one:
            two = one.replace("\n ", "\n")
            step_two_list.append(two)
        else:
            step_two_list.append(one)


    for two in step_two_list:

        if " \n\n" in two:
            two = two.split(" \n\n")

            for result_val in two:
                result.append(result_val)
        else:
            result.append(two)
            result.append('')
            result.append('')

    return result

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
    contents = res_json['contents']

    for content in contents:

        if content['content_type'] == 'why' or content['content_type'] == 'location':
            description_dict = ast.literal_eval(content['description'])
            headers = description_dict['header'].split("\n")
            image_url = ''

            if description_dict.get('picture', '') == '':
                image_url = ''
            else:
                image_url = url_stayfolio + description_dict['picture']

            description = make_description_list(description_dict['text'])

            Contents(
                content_type = ContentType.objects.get(c_type = content['content_type']),
                header       = headers,
                description  = description,
                image_url    = image_url,
                magazine     = Magazines.objects.get(identifier = res_json['identifier'])
            ).save()

        elif content['content_type'] == 'people':
            description_dict = ast.literal_eval(content['description'])
            headers = description_dict['header'].split("\n")
            image_url = url_stayfolio + description_dict['footer_img_url']

            description = make_description_list(description_dict['text'])

            Contents(
                content_type = ContentType.objects.get(c_type=content['content_type']),
                header      = headers,
                description = description,
                image_url   = image_url,
                magazine    = Magazines.objects.get(identifier = res_json['identifier'])
            ).save()
