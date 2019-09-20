import json

from django.http  import JsonResponse
from django.views import View

from .models import Place, Style, Target, Amenity, Tourspot, Feature

class PlaceView(View):
    def get(self, request):
        offset = int(request.GET.get('offset', 0))
        limit = int(request.GET.get('limit', 12))
        result = [{
        	'id'              : place.id,
        	'name'            : place.name,
        	'full_address'    : place.full_address,
        	'zipcode'         : place.zipcode,
        	'street'          : place.street,
        	'county'          : place.county,
        	'city'            : place.city,
        	'province'        : place.province,
        	'country'         : place.country,
        	'longitude'       : place.longitude,
        	'latitude'        : place.latitude,
        	'website'         : place.website,
        	'facebook'        : place.facebook,
        	'instagram'       : place.instagram,
        	'phone'           : place.phone,
        	'price_min'       : place.price_min,
        	'price_max'       : place.price_max,
        	'room_capacity'   : place.room_capacity,
        	'check_in'        : place.check_in,
        	'check_out'       : place.check_out,
        	'styles'          : [style['styles'] for style in place.styles.values('styles')],
        	'targets'         : [target['targets'] for target in place.targets.values('targets')],
        	'amenities'       : [amenity['amenities'] for amenity in place.amenities.values('amenities')],
        	'tourspots'       : [tourspot['tourspots'] for tourspot in place.tourspots.values('tourspots')],
        	'features'        : [feature['features'] for feature in place.features.values('features')],
        	} for place in Place.objects.all()[offset:limit]]

        return JsonResponse(result, safe = False, status = 200)
