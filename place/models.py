from django.db import models

class Place(models.Model):
    name          = models.CharField(max_length = 100, null = False, unique = True)
    full_address  = models.CharField(max_length = 100, null = False)
    zipcode       = models.CharField(max_length = 10, null = False)
    street        = models.CharField(max_length = 100, null = False)
    county        = models.CharField(max_length = 20, null = False)
    city          = models.CharField(max_length = 10, null = False)
    province      = models.CharField(max_length = 20, null = False)
    country       = models.CharField(max_length = 20, null = False)
    longitude     = models.CharField(max_length = 100, null = False)
    latitude      = models.CharField(max_length = 100, null = False)
    website       = models.URLField(max_length = 2500, null = True)
    facebook      = models.URLField(max_length = 2500, null = True)
    instagram     = models.URLField(max_length = 2500, null = True)
    phone         = models.CharField(max_length = 100, null = True)
    price_min     = models.DecimalField(max_digits = 9, decimal_places = 1, null = False)
    price_max     = models.DecimalField(max_digits = 9, decimal_places = 1, null = False)
    persons_min   = models.PositiveSmallIntegerField(null = False)
    persons_max   = models.PositiveSmallIntegerField(null = False)
    is_vacancy    = models.BooleanField(default = True, null = True)
    room_capacity = models.PositiveSmallIntegerField(null = False)
    check_in      = models.CharField(max_length = 10, null = False)
    check_out     = models.CharField(max_length = 10, null = False)
    place_type    = models.CharField(max_length = 100, null = True)
    created_at    = models.DateTimeField(auto_now_add = True)
    updated_at    = models.DateTimeField(auto_now = True)
    styles        = models.ManyToManyField('Style', blank = True)
    targets       = models.ManyToManyField('Target', blank = True)
    amenities     = models.ManyToManyField('Amenity', blank = True)
    tourspots     = models.ManyToManyField('Tourspot', blank = True)
    features      = models.ManyToManyField('Feature', blank = True)

    class Meta:
        db_table = 'place'

    def get_place_info(self, offset, limit):
        places = Place.objects.all()
        total_count = places.count()
        
        result      = [{
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
        'place_type'      : place.place_type,
        'styles'          : [style['styles'] for style in place.styles.values('styles')],
        'targets'         : [target['targets'] for target in place.targets.values('targets')],
        'amenities'       : [amenity['amenities'] for amenity in place.amenities.values('amenities')],
        'tourspots'       : [tourspot['tourspots'] for tourspot in place.tourspots.values('tourspots')],
        'features'        : [feature['features'] for feature in place.features.values('features')],
        'room_info'       : Room.get_room_info(place),
        } for place in places[offset:limit]]

        return {'total_count' : total_count, 'result' : result}


class Style(models.Model):
    styles = models.CharField(max_length = 100, null = True, unique = True)

    class Meta:
        db_table = 'style'

class Target(models.Model):
    targets = models.CharField(max_length = 100, null = True, unique = True)
    
    class Meta:
        db_table = 'target'

class Amenity(models.Model):
    amenities = models.CharField(max_length = 100, null = True, unique = True)
    
    class Meta:
        db_table = 'amenity'

class Tourspot(models.Model):
    tourspots = models.CharField(max_length = 100, null = True, unique = True)
	
    class Meta:
        db_table = 'tourspot'

class Feature(models.Model):
    features = models.CharField(max_length = 100, null = True, unique = True)
    
    class Meta:
        db_table = 'feature'

class Room(models.Model):
    place_info  = models.ForeignKey('Place', on_delete = models.CASCADE, null = True)
    name        = models.CharField(max_length = 100, null = False)
    room_type   = models.CharField(max_length = 50, null = False)
    description = models.CharField(max_length = 500, null = False)
    detail      = models.CharField(max_length = 500, null = False)

    def get_room_info(place):
        if not Room.objects.filter(place_info = place.id).exists():
            return None
        room_info = Room.objects.get(place_info = place.id)
        result = {
            'place_info_id' : place.id,
            'id'            : room_info.id,
            'name'          : room_info.name,
            'room_type'     : room_info.room_type,
            'description'   : room_info.description,
            'detail'        : room_info.detail,
        }
        return result

    class Meta:
        db_table = 'rooms'
