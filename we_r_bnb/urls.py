from django.urls import path, include

urlpatterns = [
    path('place', include('place.urls')),
    path('pick', include('pick.urls')),
    path('pick_comment',include('pick_comment.urls')),
    path('magazines', include('magazines.urls')),
    path('account', include('account.urls')),
    path('booking', include('booking.urls')),
]
