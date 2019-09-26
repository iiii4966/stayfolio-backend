from django.urls import path, include

urlpatterns = [
    path('place', include('place.urls')),
    path('pick', include('pick.urls')),
    path('magazines', include('magazines.urls')),
    path('account', include('account.urls')),
]
