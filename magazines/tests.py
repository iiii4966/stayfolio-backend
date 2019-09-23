import json

from django.test import TestCase, Client
from .models     import Magazines, ContentType, Contents
from .views      import MagazinesView


class MagazinesViewTest(TestCase):
    def setUp(self):
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
                details              = "test_details"
                )

    def test_magazines_paging(self):
        c = Client()

        response = c.get("/magazines?offset=0&limit=5")
        print(response.json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
                response.json(), 
                {'items': [
                    {
                        'name_kr': 'test_identifier_kr', 
                        'title': 'test_title', 
                        'description': 'test_description', 
                        'main_image_url': 'https://www.google.com', 
                        'details': 'test_details'
                        }], 'total_count': 1})
