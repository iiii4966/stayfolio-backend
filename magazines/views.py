import json
import math

from django.http      import JsonResponse, HttpResponse
from django.views     import View
from magazines.models import Magazines, Contents, ContentType

class MagazinesView(View):
    def get(self, request):
        total_count    = Magazines.objects.all().count()
        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('limit', 5))
        magazines_data = Magazines.objects.all()[offset:limit].values()

        response_data = [{
            'name_kr'        : magazine_data['identifier_kr'],
            'title'          : magazine_data['title'],
            'description'    : magazine_data['description'],
            'main_image_url' : magazine_data['main_image_url'],
            'details'        : magazine_data['details'],
            } for magazine_data in magazines_data]

        return JsonResponse({
            "items" : response_data, 
            "total_count" : total_count
            }, safe=False, status=200)
