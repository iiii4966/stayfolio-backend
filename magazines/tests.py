import json

from django.test      import TestCase, Client
from magazines.models import Magazines, ContentType, Contents
from place.models     import Place, Style, Target, Amenity, Tourspot, Feature
from .views           import MagazinesView


class MagazinesViewTest(TestCase):
    styles    = ['styles1', 'style2', 'style3']
    targets   = ['target1', 'target2', 'target3']
    amenities = ['amenity1', 'amenity2', 'amenity3']
    tourspots = ['tourspot1', 'tourspot2', 'tourspot3']
    features  = ['feature1','feature2','feature3']

    def setUp(self):
        new_styles    = []
        new_targets   = []
        new_amenities = []
        new_tourspots = []
        new_features  = []

        for style, target, amenity, tourspot, feature in zip(self.styles, self.targets, self.amenities, self.tourspots, self.features):
            new_styles.append(Style.objects.create(styles = style))
            new_targets.append(Target.objects.create(targets = target))
            new_amenities.append(Amenity.objects.create(amenities = amenity))
            new_tourspots.append(Tourspot.objects.create(tourspots = tourspot))
            new_features.append(Feature.objects.create(features = feature))

        place = Place.objects.create(
                id = 1,
                name = "test_identifier_kr",
                full_address = "test_full_address",
                zipcode = "11111",
                street = "test_street",
                county = "test_county",
                city = "test_city",
                province = "test_province",
                country = "test_country",
                longitude = "111.11",
                latitude = "111.11",
                website = "https://www.google.com",
                facebook = "https://www.google.com",
                instagram = "https://www.google.com",
                phone = "010-0000-0000",
                price_min = "10000.0",
                price_max = "10000.0",
                persons_min = "1",
                persons_max = "2",
                is_vacancy = "1",
                room_capacity = "1",
                check_in = "16:00",
                check_out = "11:00",
                )

        place.styles.add(*new_styles)
        place.targets.add(*new_targets)
        place.amenities.add(*new_amenities)
        place.tourspots.add(*new_tourspots)
        place.features.add(*new_features)

        magazine = Magazines.objects.create(
                id                   = 1,
                title                = "test_title",
                title_image_url      = "https://www.google.com",
                title_text_image_url = "https://www.google.com",
                identifier           = "test_identifier",
                identifier_kr        = "test_identifier_kr",
                description          = "test_description",
                intro                = "test_intro",
                main_image_url       = "https://www.google.com",
                logo_url             = "https://www.google.com",
                details              = "test_details",
                place                = place
                )

        content_type = ContentType.objects.create(
                id =1,
                c_type = "WHY"
                )

        content = Contents.objects.create(
                id = 1,
                content_type = content_type,
                header = ['This', 'is', 'test', 'header.'],
                description = ['This', 'is', 'test', 'description.'],
                image_url = "https://www.google.com",
                magazine = magazine
                )

    def test_magazines_paging(self):
        c = Client()

        response = c.get("/magazines?offset=0&limit=5")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
                response.json(),
                {'items': [
                    {
                        'identifier': 'test_identifier',
                        'identifier_kr': 'test_identifier_kr',
                        'title': 'test_title',
                        'description': 'test_description',
                        'main_image_url': 'https://www.google.com',
                        'details': 'test_details'
                        }
                    ], 'total_count': 1})
    def test_magazine_detail(self):
        c = Client()

        response = c.get("/magazines/test_identifier")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
                response.json(),
                {'MAGAZINE':
                    {
                        'title': 'test_title',
                        'tile_image_url': 'https://www.google.com',
                        'title_text_image_url': 'https://www.google.com',
                        'identifier': 'test_identifier',
                        'identifier_kr': 'test_identifier_kr',
                        'intro': 'test_intro',
                        'main_image_url': 'https://www.google.com',
                        'footer_image_url': None,
                        'link_btn_title': None,
                        'link_btn_url': None,
                        'logo_url': 'https://www.google.com',
                        'details': 'test_details',
                        'contents': [
                            {
                                'content_type': 'WHY',
                                'header': ['This', 'is', 'test', 'header.'],
                                'description': ['This', 'is', 'test', 'description.'],
                                'image_url': 'https://www.google.com'
                                }
                            ],
                        'place': {
                            'identifier': 'test_identifier_kr',
                            'full_address': 'test_full_address',
                            'zipcode': '11111',
                            'street': 'test_street',
                            'county': 'test_county',
                            'city': 'test_city',
                            'province': 'test_province',
                            'country': 'test_country',
                            'longitude': '111.11',
                            'website': 'https://www.google.com',
                            'facebook': 'https://www.google.com',
                            'instagram': 'https://www.google.com',
                            'phone': '010-0000-0000',
                            'price_min': '10000.0',
                            'price_max': '10000.0',
                            'is_vacancy': True,
                            'room_capacity': 1,
                            'check_in': '16:00',
                            'check_out': '11:00',
                            'styles': ['style2', 'style3', 'styles1'],
                            'targets': ['target1', 'target2', 'target3'],
                            'amenities': ['amenity1', 'amenity2', 'amenity3'],
                            'tourspots': ['tourspot1', 'tourspot2', 'tourspot3'],
                            'features': ['feature1', 'feature2', 'feature3']
                            }
                        }
                    }

                )
