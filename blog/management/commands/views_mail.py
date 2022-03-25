from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
from blog.models import Blog
import datetime


class Command(BaseCommand):

    def handle(self, *args, **options):
        blog = Blog.objects.all()
        view = [blog_v.views for blog_v in blog]
        blog_view = sum(view)
        time = datetime.date.today()
        subject = 'PV結果'
        massege = '{0}は計{1}PVでした'.format(time, blog_view)
        from_mail = []
        recipient = [settings.EMAIL_HOST_USER]
        send_mail(subject, massege, from_mail, recipient)
        blog.update(views=0)
        self.stdout.write(self.style.SUCCESS('メッセージ Mail'))