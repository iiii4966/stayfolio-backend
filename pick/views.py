import json

from django.http  import JsonResponse
from django.views import View

from .models import PickImage, Pick, Place

class PickListView(View):
    def get(self, request):
        offset      = int(request.GET.get('offset', 0))
        limit       = int(request.GET.get('limit', 12))
        picks       = Pick.objects.all()
        total_count = picks.count()

        result     = [{
            'pick_id'        : pick.pick_id,
            'identifier'     : pick.identifier,
            'title'          : pick.title,
            'subtitle'       : pick.subtitle,
            'description'    : pick.description,
            'main_image_url' : pick.main_image_url,
            'images'         : PickImage.get_pick_images(pick.pick_id),
            'place_info_id'  : pick.place_info_id,
            'place_info'     : Pick.get_place_info(pick),
        } for pick in picks[offset:limit]]
        
        return JsonResponse({'total_count':total_count, 'result' : result}, safe = False, status = 200)

class PickView(View):
    def get(self, request, pick_id):
        pick = Pick.objects.get(pick_id = pick_id)
        
        result = {
            'pick_id'        : pick_id,
            'identifier'     : pick.identifier,
            'title'          : pick.title,
            'subtitle'       : pick.subtitle,
            'description'    : pick.description,
            'main_image_url' : pick.main_image_url,
            'images'         : PickImage.get_pick_images(pick_id),
            'place_info_id'  : pick.place_info_id,
            'place_info'     : Pick.get_place_info(pick),
        }
        
        return JsonResponse(result, safe = False, status = 200)
