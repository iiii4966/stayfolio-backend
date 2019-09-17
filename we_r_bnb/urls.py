from django.urls import path, include

urlpatterns = [
   path('magazines', include('magazines.urls'))
]
