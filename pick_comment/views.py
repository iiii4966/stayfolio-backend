import json

from django.http  import JsonResponse, HttpResponse
from django.views import View

from .models        import PickComment
from account.models import Accounts
from pick.models    import Pick
from account.utils  import login_required

class PickCommentView(View):
    def get(self, request, pick_id):
        offset = int(request.GET.get('offset', 0))
        limit  = int(request.GET.get('limit', 10))

        comment_data = PickComment.objects.select_related('pick').filter(pick = pick_id, is_deleted = False).values()
        total_count  = comment_data.count()
        
        data = [{
            'user_name'    : Accounts.objects.get(id = comment['user_id']).name,
            'user_email'   : Accounts.objects.get(id = comment['user_id']).email,
            'pick_id'      : comment['pick_id'],
            'pick_title'   : Pick.objects.get(pick_id = comment['pick_id']).title,
            'comment_id'   : comment['id'],
            'content'      : comment['content'],
            } for comment in comment_data.order_by('created_at').reverse()[offset:limit]]

        return JsonResponse({'total_count' : total_count, 'data' : data}, safe = False, status = 200)

    @login_required
    def post(self, request, pick_id):
        data = json.loads(request.body)
        
        try:
            login_user = request.user
            pick_data = Pick.objects.get(pick_id = pick_id)
        except Pick.DoesNotExist:
            return JsonResponse({'message':'NO_PICK_IN_DB'}, status = 404)

        if 'content' not in data or len(data['content']) == 0:
            return JsonResponse({'message':'COMMENT_MISSING'}, status = 400)

        PickComment.objects.create(
            user    = login_user, 
            pick    = pick_data,
            content = data['content'],
        )
        
        return HttpResponse(status = 200)

class CommentEditingView(View):
    @login_required
    def post(self, request, pick_id, comment_id):
        data = json.loads(request.body)
        
        try:
            user_comment = PickComment.objects.get(id = comment_id, pick_id = pick_id , user = request.user)

            if 'content' not in data or len(data['content']) == 0:
                return JsonResponse({'message':'COMMENT_MISSING'}, status = 400)
            
            user_comment.content = data['content']
            user_comment.save()

            return HttpResponse(status = 200)
        except PickComment.DoesNotExist:
            return JsonResponse({'message':'COMMENT_NOT_EXIST'}, status = 401)

    @login_required
    def delete(self, request, pick_id, comment_id):
        try:
            user_comment = PickComment.objects.get(id = comment_id, user = request.user)
            user_comment.is_deleted = True
            user_comment.save()

            return HttpResponse(status = 200)
        except PickComment.DoesNotExist:
            return JsonResponse({'message':'COMMENT_NOT_EXIST'}, status = 401)
