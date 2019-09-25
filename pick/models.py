from django.db    import models
from place.models import Place, Room

class PickImage(models.Model):
    pick_name = models.ForeignKey('Pick', on_delete = models.SET_NULL, null = True)
    image_id  = models.AutoField(primary_key = True)
    image_url = models.URLField(max_length = 2500, null = False)
    
    class Meta:
        db_table = 'pick_images'

    def get_pick_images(pick_id):
        images = PickImage.objects.select_related('pick_name')
        return [image['image_url'] for image in images.filter(pick_name_id = pick_id).values()]

class Pick(models.Model):
    pick_id        = models.AutoField(primary_key = True)
    identifier     = models.CharField(max_length = 100, null  = False, unique = True)
    place_info     = models.ForeignKey(Place, on_delete = models.CASCADE, null = True)
    title          = models.CharField(max_length = 100, null  = False, unique = True)
    subtitle       = models.CharField(max_length = 100, null  = False)
    description    = models.TextField(null = False)
    main_image_url = models.URLField(max_length = 2500, null = False)
    created_at     = models.DateTimeField(auto_now_add = True)
    updated_at     = models.DateTimeField(auto_now = True)
    
    class Meta:
        db_table = 'picks'
     
    def get_place_info(place):
        place_info = Place.objects.get(pk = place.place_info_id)
        
        place = {
            'id'            : place_info.id,
            'name'          : place_info.name,
            'full_address'  : place_info.full_address,
            'zipcode'       : place_info.zipcode,
            'street'        : place_info.street,
            'county'        : place_info.county,
            'city'          : place_info.city,
            'province'      : place_info.province,
            'country'       : place_info.country,
            'longitude'     : place_info.longitude,
            'latitude'      : place_info.latitude,
            'website'       : place_info.website,
            'facebook'      : place_info.facebook,
            'instagram'     : place_info.instagram,
            'phone'         : place_info.phone,
            'price_min'     : place_info.price_min,
            'price_max'     : place_info.price_max,
            'persons_min'   : place_info.persons_min,
            'persons_max'   : place_info.persons_max,
            'room_capacity' : place_info.room_capacity,
            'check_in'      : place_info.check_in,
            'check_out'     : place_info.check_out,
            'place_type'    : place_info.place_type,
            'styles'        : [style['styles'] for style in place_info.styles.values('styles')],
            'targets'       : [target['targets'] for target in place_info.targets.values('targets')],
            'amenities'     : [amenity['amenities'] for amenity in place_info.amenities.values('amenities')],
            'tourspots'     : [tourspot['tourspots'] for tourspot in place_info.tourspots.values('tourspots')],
            'features'      : [feature['features'] for feature in place_info.features.values('features')],
            'room_info'     : Room.get_room_info(place_info) 
        }
        return place
