import bcrypt
import datetime
import json
import jwt
import pdb
import smtplib

from account.utils      import login_required
from datetime           import timedelta
from email.mime.text    import MIMEText
from .models            import Accounts
from my_settings        import SECRET

from django.core.mail   import send_mail
from django.conf        import settings
from django.http        import HttpResponse, JsonResponse
from django.views       import View


class SignUpView(View):
    def post(self, request):
        data = json.loads(request.body)

        if Accounts.objects.filter(email=data['email']).exists():
            return JsonResponse({'message': 'EMAIL_ALREADY_EXISTS'}, status=400)

        if len(data['password']) == 0:
            return JsonResponse({'error': 'INPUT_PASSWORD'}, status=401)

        if len(data['email']) == 0:
            return JsonResponse({'error': 'INPUT_EMAIL'}, status=401)

        try:
            password = bytes(data['password'], 'UTF-8')
            hashed_pw = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())

            Accounts(
                email=data['email'],
                name=data['name'],
                password=hashed_pw.decode('UTF-8'),
            ).save()
            
            return JsonResponse({'message': 'SUCCESS'}, status=200)

        except KeyError:
            return JsonResponse({'error': 'MISSING_INPUT'}, status=401)


class LogInView(View):
    def post(self, request):
        data = json.loads(request.body)
       
        try:
            password = data['password']
            exist_account = Accounts.objects.get(email = data['email'])

            if bcrypt.checkpw(password.encode('UTF-8'), exist_account.password.encode('UTF-8')):
                payload = {'email':exist_account.email}
                encoded = jwt.encode(payload, SECRET['secret'], algorithm='HS256')

                return JsonResponse({'access_token': encoded.decode('UTF-8')}, status=200)
            
            else:
                return JsonResponse({'error': 'INVALID_PASSWORD'}, status=401)

        except Accounts.DoesNotExist:
            return JsonResponse({'error':'INVALID_EMAIL_ADDRESS'}, status=401)
