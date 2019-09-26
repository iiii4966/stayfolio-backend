import json
import bcrypt
import jwt

from django.test   import TestCase
from django.test   import Client

from we_r_bnb.settings import SECRET_KEY
from .models           import PickComment
from place.models      import Place, Style, Target, Amenity, Tourspot, Feature
from pick.models       import Pick, PickImage
from account.models    import Accounts
from account.utils     import login_required
from test_fixtures     import _gen_fixture_data, get_today

class CommentTest(TestCase):
    encrypted_pw = bcrypt.hashpw(bytes('1234','utf-8'), bcrypt.gensalt()).decode('UTF-8')

    def setUp(self):
        place      = _gen_fixture_data()['place']
        tags       = _gen_fixture_data()['place_tag']
        pick       = _gen_fixture_data()['pick']
        image_urls = _gen_fixture_data()['image_urls']

        new_user = Accounts.objects.create(
            email    = '1234',
            name     = '1234',
            password = self.encrypted_pw,
        )

        new_place = Place.objects.create(
            name          = place['name'],
            full_address  = place['full_address'],
            zipcode       = place['zipcode'],
            street        = place['street'],
            county        = place['county'],
            city          = place['city'],
            province      = place['province'],
            country       = place['country'],
            longitude     = place['longitude'],
            latitude      = place['latitude'],
            website       = place['website'],
            facebook      = place['facebook'],
            instagram     = place['instagram'],
            phone         = place['phone'],
            price_min     = place['price_min'],
            price_max     = place['price_max'],
            persons_min   = place['persons_min'],
            persons_max   = place['persons_max'],
            room_capacity = place['room_capacity'],
            check_in      = place['check_in'],
            check_out     = place['check_out'],
            place_type    = place['place_type'],
        )
 
        new_styles    = [ ]
        new_targets   = [ ]
        new_amenities = [ ]
        new_tourspots = [ ]
        new_features  = [ ]

        for style, target, amenity, tourspot, feature in zip(tags['styles'], tags['targets'], tags['amenities'], tags['tourspots'], tags['features']):
            new_styles.append(Style.objects.create(styles=style))
            new_targets.append(Target.objects.create(targets=target))
            new_amenities.append(Amenity.objects.create(amenities=amenity))
            new_tourspots.append(Tourspot.objects.create(tourspots=tourspot))
            new_features.append(Feature.objects.create(features=feature))

        new_place.styles.add(*new_styles)
        new_place.targets.add(*new_targets)
        new_place.amenities.add(*new_amenities)
        new_place.tourspots.add(*new_tourspots)
        new_place.features.add(*new_features)

        new_pick = Pick.objects.create(
            identifier     = pick['identifier'],
            title          = pick['title'],
            subtitle       = pick['subtitle'],
            description    = pick['description'],
            main_image_url = pick['main_image_url'],
            place_info     = Place.objects.get(name = place['name'])
        )

        for image in image_urls:
            PickImage.objects.create(
                image_url = image,
                pick_name = new_pick,
            )

        test_comment = PickComment.objects.create(
            user     = new_user,
            pick     = new_pick,
            content  = '1234',
        )

    def test_post_comment(self):
        c = Client()
        test_user = {'email' : '1234', 'password' : '1234'}
        response = c.post('/account/login', json.dumps(test_user), content_type = 'application/json')
        access_token = response.json()['access_token']
        test_comment = {'content' : '1234'}
        response = c.post('/pick_comment/4', json.dumps(test_comment), content_type = 'application/json', HTTP_AUTHORIZATION=access_token)
        self.assertEqual(response.status_code, 200)

    def test_post_comment_fail(self):
        c = Client()
        test_user = {'email' : '1234', 'password' : '1234'}
        response = c.post('/account/login', json.dumps(test_user), content_type = 'application/json')
        access_token = response.json()['access_token']
        test_comment = {'content' : ''}
        response = c.post('/pick_comment/5', json.dumps(test_comment), content_type = 'application/json', HTTP_AUTHORIZATION=access_token)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),
                            {'message':'COMMENT_MISSING'} 
                        )

    def test_get_comment(self):
        c = Client()
        response = c.get('/pick_comment/3', content_type = 'application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(),
                                {
                                    'total_count' : 1,
                                    'data'        : [
                                     {
                                         'user_name'  : '1234',
                                         'user_email' : '1234',
                                         'pick_id'    : 3,
                                         'pick_title' : '잠시 쉬어가도 좋은 우도의 하루',
                                         'comment_id' : 3,
                                         'content'    : '1234',
                                    }
                                ]
                            }
                        )

    def test_update_comment(self):
        c = Client()
        test_user = {'email' : '1234', 'password' : '1234'}
        response = c.post('/account/login', json.dumps(test_user), content_type = 'application/json')
        access_token = response.json()['access_token']
        test_comment = {'content' : '5678'}
        respnse = c.post('/pick_comment/2/2/editing', json.dumps(test_comment), content_type = 'application/json', HTTP_AUTHORIZATION=access_token)
        self.assertEqual(response.status_code, 200)

    def test_delete_comment(self):
        c = Client()
        test_user = {'email' : '1234', 'password' : '1234'}
        response = c.post('/account/login', json.dumps(test_user), content_type = 'application/json')
        access_token = response.json()['access_token']
        respnse = c.delete('/pick_comment/2/2/editing', content_type = 'application/json', HTTP_AUTHORIZATION=access_token)
        self.assertEqual(response.status_code, 200)

    def test_delete_comment_fail(self):
        c = Client()
        test_user = {'email' : '1234', 'password' : '1234'}
        response = c.post('/account/login', json.dumps(test_user), content_type = 'application/json')
        access_token = response.json()['access_token']
        response = c.delete('/pick_comment/2/100/editing', content_type = 'application/json', HTTP_AUTHORIZATION=access_token)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(),
                            {'message':'COMMENT_NOT_EXIST'}
                        )
