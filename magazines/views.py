from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import Magazines, Contents
import json


class MagazinesView(View):
    
    def get(self, request):
        return JsonResponse({'message': 'SUCCESS'}, status = 200)


class MagazineDetailView(View):
    
    def get(self, request, identifier):
        return JsonResponse({'message': "SUCCESS"}, status = 200)
