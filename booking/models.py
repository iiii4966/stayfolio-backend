from django.db            import models
from account.models       import Accounts
from place.models         import Place

class Booking(models.Model):
    """
    :phone_number   : Required
    :special_request: Optional
    :booking_id     : User unique booking identifier
    :is_vacancy     : Room availability
    :check_in       : From when the booking is active
    :check_out      : Until when the booking is active
    :bill_total     : Total amount
    """
    account         = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    phone_number    = models.CharField(max_length=16, blank=False)
    special_request = models.CharField(max_length=512, blank=True)
    room            = models.ForeignKey(Place, on_delete = models.CASCADE, null=True) 
    is_vacancy      = models.NullBooleanField(default=True)
    check_in        = models.DateField(max_length=10)
    check_out       = models.DateField(max_length=10)
    bill_total      = models.DecimalField(max_digits = 9, decimal_places=1, null=False)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table='booking'
