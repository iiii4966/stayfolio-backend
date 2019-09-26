from django.db      import models
from account.models import Accounts
from pick.models    import Pick

class PickComment(models.Model):
    user       = models.ForeignKey(Accounts, on_delete = models.CASCADE, null = False)
    pick       = models.ForeignKey(Pick, on_delete = models.CASCADE, null = False)
    is_deleted = models.BooleanField(default = False, null = True)
    content    = models.TextField(null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        db_table = 'pick_comments'
