import json

from django.test import Client
from django.test import TestCase

from .models import Place, Style, Target, Amenity, Tourspot, Feature
from .views  import PlaceView

class PlaceGetTest(TestCase):
    styles    = ['재생건축','아웃도어','빈티지']
    targets   = ['가족여행','커플여행','로컬투어']
    amenities = ['명상','스파','쾌적한 정원']
    tourspots = ['cafe','restaurant','shopping']
    features  = ['barbeque','open_air_bath','breakfast']
    
    def setUp(self):
        new_styles    = [ ]
        new_targets   = [ ]
        new_amenities = [ ]
        new_tourspots = [ ]
        new_features  = [ ]
        for style, target, amenity, tourspot, feature in zip(self.styles, self.targets, self.amenities, self.tourspots, self.features):
            new_styles.append(Style.objects.create(styles = style))
            new_targets.append(Target.objects.create(targets = target))
            new_amenities.append(Amenity.objects.create(amenities = amenity))
            new_tourspots.append(Tourspot.objects.create(tourspots = tourspot))
            new_features.append(Feature.objects.create(features = feature))
        
        new_place = Place.objects.create(
                                   name          = '돌채',
                                   full_address  = '제주특별자치도 제주시 우도면 우목길 60-3',
                                   zipcode       = '63365',
                                   street        = '60-3',
                                   county        = '제주시 우도면 우목길',
                                   city          = '제주시',
                                   province      = '제주도',
                                   country       = '한국',
                                   longitude     = '126.949035',
                                   latitude      = '33.508973',
                                   website       = 'bit.ly/2m0TwWo',
                                   facebook      = 'dolchae',
                                   instagram     = 'dolchae',
                                   phone         = '0504-0904-2346',
                                   price_min     = '150000.0',
                                   price_max     = '300000.0',
                                   persons_min   = 1,
                                   persons_max   = 5,
                                   room_capacity = 2,
                                   check_in      = '16:00',
                                   check_out     = '11:00',
                    )
        
        new_place.styles.add(*new_styles)
        new_place.targets.add(*new_targets)
        new_place.amenities.add(*new_amenities)
        new_place.tourspots.add(*new_tourspots)
        new_place.features.add(*new_features)
        
    def test_get_places(self):
        c = Client()

        response = c.get('/place', content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                         [
                             {
                                 'id'            : 1,
                                 'name'          : '돌채',
                                 'full_address'  : '제주특별자치도 제주시 우도면 우목길 60-3',
                                 'zipcode'       : '63365',
                                 'street'        : '60-3',
                                 'county'        : '제주시 우도면 우목길',
                                 'city'          : '제주시',
                                 'province'      : '제주도',
                                 'country'       : '한국',
                                 'longitude'     : '126.949035',
                                 'latitude'      : '33.508973',
                                 'website'       : 'bit.ly/2m0TwWo',
                                 'facebook'      : 'dolchae',
                                 'instagram'     : 'dolchae',
                                 'phone'         : '0504-0904-2346',
                                 'price_min'     : '150000.0',
                                 'price_max'     : '300000.0',
                                 'room_capacity' : 2,
                                 'check_in'      : '16:00',
                                 'check_out'     : '11:00',
                                 'styles'        : ['빈티지', '아웃도어', '재생건축'],
                                 'targets'       : ['가족여행','로컬투어','커플여행'],
                                 'amenities'     : ['명상','스파','쾌적한 정원'],
                                 'tourspots'     : ['cafe','restaurant','shopping'],
                                 'features'      : ['barbeque','breakfast','open_air_bath'],
                             }
                         ]
                        )
