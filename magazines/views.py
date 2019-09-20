from django.http import JsonResponse, HttpResponse
from django.views import View
from .models import Magazines, Contents
import json


class MagazinesView(View):
    
    def get(self, request):
        total_count = len(Magazines.objects.all())
        current_page = int(request.GET.get('page', '1'))
        per_page = 5

        return JsonResponse({'message': 'SUCCESS'}, status = 200)


class MagazineDetailView(View):
    
    def get(self, request, identifier):
        return JsonResponse({'message': "SUCCESS"}, status = 200)
