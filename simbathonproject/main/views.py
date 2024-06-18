from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from .models import Varsity

def likes(request, varsity_id):
    varsity = get_object_or_404(Varsity, id=varsity_id)
    liked_varsitys = request.COOKIES.get('liked_varsitys', '')

    if str(varsity_id) in liked_varsitys.split(','):
        # 사용자가 이미 '좋아요'를 눌렀다면
        response = redirect('main:detail', varsity.id)
        return response
    else:
        # '좋아요'를 처음 누르는 경우
        varsity.like_count += 1
        varsity.save()
        response = redirect('main:detail', varsity.id)
        # 쿠키에 현재 포스트 ID 추가
        if liked_varsitys:
            liked_varsitys += ',' + str(varsity_id)
        else:
            liked_varsitys = str(varsity_id)
        response.set_cookie('liked_varsitys', liked_varsitys, max_age=31536000)  # 쿠키는 1년간 유효
        return response


# def likes(request, varsity_id):
#     varsity = get_object_or_404(Varsity, id=varsity_id)
#     if request.user in varsity.like.all():
#         varsity.like.remove(request.user)
#         varsity.like_count -= 1
#         varsity.save()

#     else:
#         varsity.like.add(request.user)
#         varsity.like_count += 1
#         varsity.save()
    
#     return redirect('main:detail', varsity.id)