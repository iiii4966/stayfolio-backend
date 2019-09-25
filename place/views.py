import json

from django.http  import JsonResponse
from django.views import View

from .models import Place, Style, Target, Amenity, Tourspot, Feature

class PlaceView(View):
    def get(self, request):
        offset      = int(request.GET.get('offset', 0))
        limit       = int(request.GET.get('limit', 12))
        places      = Place.objects.all()
        total_count = places.count()
        result      = Place.get_place_info(self,offset,limit)

        return JsonResponse(result, safe = False, status = 200)
