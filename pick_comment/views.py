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

        comment_data = PickComment.objects.select_related('pick', 'user').filter(pick = pick_id, is_deleted = False)
        total_count  = comment_data.count()
        
        data = [{
            'user_name'    : user.name,
            'user_email'   : user.email,
            'pick_id'      : comment['pick_id'],
            'pick_title'   : pick.title,
            'comment_id'   : comment['id'],
            'content'      : comment['content'],
            } for comment in comment_data.order_by('-created_at')[offset:limit]]

        return JsonResponse({'total_count' : total_count, 'data' : data})

@login_required
    def post(self, request, pick_id):
        data = json.loads(request.body)

         if 'content' not in data or len(data['content']) == 0:
            return JsonResponse({'ERROR':'COMMENT_MISSING'}, status = 400)
        
        try:
            pick_data = Pick.objects.get(pick_id = pick_id)

            PickComment.objects.create(
                user    = login_user, 
                pick    = pick_data,
                content = data['content'],
            )
        
            return HttpResponse(status = 200)
        except Pick.DoesNotExist:
            return JsonResponse({'ERROR':'NOT_FOUND'}, status = 404)
       
class CommentEditingView(View):
    @login_required
    def post(self, request, pick_id, comment_id):
        data = json.loads(request.body)
       
        if 'content' not in data or len(data['content']) == 0:
            return JsonResponse({'ERROR':'COMMENT_MISSING'}, status = 400)

        try:
            user_comment = PickComment.objects.get(id = comment_id, user = request.user)                       
            user_comment.content = data['content']
            user_comment.save()

            return HttpResponse(status = 200)
        except PickComment.DoesNotExist:
            return JsonResponse({'ERROR':'COMMENT_NOT_EXIST'}, status = 401)

    @login_required
    def delete(self, request, pick_id, comment_id):
        try:
            user_comment = PickComment.objects.get(id = comment_id, user = request.user)
            user_comment.is_deleted = True
            user_comment.save()

            return HttpResponse(status = 200)
        except PickComment.DoesNotExist:
            return JsonResponse({'ERROR':'COMMENT_NOT_EXIST'}, status = 401)
