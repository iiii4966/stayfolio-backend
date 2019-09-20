from django.urls import path, include

urlpatterns = [
        path('place', include('place.urls')),
        path('magazines', include('magazines.urls'))
]
