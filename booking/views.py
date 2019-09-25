import json

from django.http      import JsonResponse
from django.shortcuts import render
from django.views     import View

from .models          import Booking
from place.models     import Place
from account.models   import Accounts
from account.utils    import login_required
from datetime         import date, datetime, timedelta
from decimal          import Decimal

class BookingView(View):
    def convert_date(self, day):
        props = day.split('-')
        return date(int(props[0]),int(props[1]),int(props[2]))
    
    def get(self, request):
        """
        :start : Check-in Date
        :end   : Check-out Date
        :price : Per day price
        :delta : How many days to stay
        :result: Total Billing
        """
        start       = request.GET.get('start', None)
        end         = request.GET.get('end', None)
        place       = request.GET.get('place', None)
        price       = Place.objects.get(pk = place).price_max 
        delta       = self.convert_date(start) - self.convert_date(end)
        result      = (abs(delta.days)-1) * price
       
        return JsonResponse({'total_price':result}, status=200)

    @login_required
    def post(self, request): 
        data = json.loads(request.body)
        Booking.objects.create(
            account         = request.account,
            phone_number    = data['phone_number'],
            special_request = data['special_request'],
            check_in        = data['check_in'],
            check_out       = data['check_out'],
            bill_total      = Decimal(data['bill_total'])
        )

        return JsonResponse({'message':'BOOKING_CONFIRMED'}, status=200)
