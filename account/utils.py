import json
import jwt

from django.http            import JsonResponse
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist

from .models                import Accounts
from we_r_bnb.settings      import SECRET_KEY

def login_required(view_func):
    def wrap(self, request, *a, **k):
        access_token = request.headers.get('Authorization', None)

        if access_token:
            try:
                decoded         = jwt.decode(access_token, SECRET_KEY, algorithm='HS256')
                email           = decoded['email']
                request.account = Accounts.objects.get(email=email)
            except jwt.DecodeError: 
                return JsonResponse({'error': 'INVALID_TOKEN'}, status=401)
            except Accounts.DoesNotExist:
                return JsonResponse({'error':'INVALID_EMAIL_ADDRESS'}, status=401)
            return view_func(self, request, *a, **k)

        else:
            raise PermissionDenied('LOGIN_REQUIRED')

    return wrap

