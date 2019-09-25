import json
import math
import ast

from django.http      import JsonResponse, HttpResponse
from django.views     import View
from magazines.models import Magazines, Contents, ContentType
from place.models     import Place, Style, Target, Amenity, Tourspot, Feature


class MagazinesView(View):
    def get(self, request):
        total_count    = Magazines.objects.all().count()
        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('limit', 5))
        magazines_data = Magazines.objects.all()[offset:limit].values()

        response_data = [{
            'identifier'     : magazine_data['identifier'],
            'identifier_kr'  : magazine_data['identifier_kr'],
            'title'          : magazine_data['title'],
            'description'    : magazine_data['description'],
            'main_image_url' : magazine_data['main_image_url'],
            'details'        : magazine_data['details'],
            } for magazine_data in magazines_data]

        return JsonResponse({"items" : response_data, "total_count" : total_count}, safe=False, status=200)

class MagazineDetailView(View):
    def get(self, request, identifier):
        try:
            magazine_data = Magazines.objects.filter(identifier = identifier).values()[0]
        except Magazines.DoesNotExist:
            return JsonResponse({'MESSAGE': 'MAGAZINE_NOT_EXIST'}, status = 401)

        contents_in_magazine = Contents.objects.filter(magazine = magazine_data['id']).values()
        places_in_magazine = Place.objects.get(name = magazine_data['identifier_kr'])

        response_data = {
                'title'                : magazine_data['title'],
                'title_image_url'      : magazine_data['title_image_url'],
                'title_text_image_url' : magazine_data['title_text_image_url'],
                'identifier'           : magazine_data['identifier'],
                'identifier_kr'        : magazine_data['identifier_kr'],
                'intro'                : magazine_data['intro'],
                'main_image_url'       : magazine_data['main_image_url'],
                'footer_image_url'     : magazine_data['footer_image_url'],
                'link_btn_title'       : magazine_data['link_btn_title'],
                'link_btn_url'         : magazine_data['link_btn_url'],
                'logo_url'             : magazine_data['logo_url'],
                'details'              : magazine_data['details'],
                }

        contents_data = [{
            'content_type' : ContentType.objects.get(id = content['content_type_id']).c_type,
            'header'       : ast.literal_eval(content['header']),
            'description'  : ast.literal_eval(content['description']),
            'image_url'    : content['image_url']
            } for content in contents_in_magazine]

        place_data = {
            'identifier'    : places_in_magazine.name,
            'full_address'  : places_in_magazine.full_address,
            'zipcode'       : places_in_magazine.zipcode,
            'street'        : places_in_magazine.street,
            'county'        : places_in_magazine.county,
            'city'          : places_in_magazine.city,
            'province'      : places_in_magazine.province,
            'country'       : places_in_magazine.country,
            'longitude'     : places_in_magazine.longitude,
            'latitude'      : places_in_magazine.latitude,
            'website'       : places_in_magazine.website,
            'facebook'      : places_in_magazine.facebook,
            'instagram'     : places_in_magazine.instagram,
            'phone'         : places_in_magazine.phone,
            'price_min'     : places_in_magazine.price_min,
            'price_max'     : places_in_magazine.price_max,
            'is_vacancy'    : places_in_magazine.is_vacancy,
            'room_capacity' : places_in_magazine.room_capacity,
            'check_in'      : places_in_magazine.check_in,
            'check_out'     : places_in_magazine.check_out,
            'styles'        : [style[1] for style in Style.objects.values_list().filter(
                place__name = places_in_magazine.name)],
            'targets'       : [target[1] for target in Target.objects.values_list().filter(
                place__name = places_in_magazine.name)],
            'amenities'     : [amenity[1] for amenity in Amenity.objects.values_list().filter(
                place__name = places_in_magazine.name)],
            'tourspots'     : [tourspot[1] for tourspot in Tourspot.objects.values_list().filter(
                place__name = places_in_magazine.name)],
            'features'      : [feature[1] for feature in Feature.objects.values_list().filter(
                place__name = places_in_magazine.name)]
            }

        response_data['contents'] = contents_data
        response_data['place']    = place_data

        return JsonResponse({"MAGAZINE" : response_data}, status=200)
