from django.shortcuts import render, get_object_or_404
from .models import Blog

from django.conf import settings 
import datetime  
from django.core.mail import send_mail  

# Create your views here.
""" 一覧表示"""
def index(request):
    time = datetime.datetime.now()
    blog = Blog.objects.order_by('-id')

    value = [value.views for value in blog]
    value_sum = sum(value)

    if value_sum == 10:
        subject = 'Djangoアプリから通知'
        massege = '{}PV達成しました!'.format(value_sum)
        from_mail = []
        recipient = [settings.EMAIL_HOST_USER]
        send_mail(subject, massege, from_mail, recipient)

    return render(request, 'blog/index.html', {'blog': blog, 'time': time  })

""" 記事詳細"""
def detail(request, blog_id):
    # 観覧数を + 1　する。
    blog = get_object_or_404(Blog, id=blog_id)
    blog.views += 1  
    blog.save() 
    return render(request, 'blog/detail.html', {'blog': blog })
