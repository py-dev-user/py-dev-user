from django.core.mail import send_mail
from django.utils.html import strip_tags

from datetime import datetime
from os.path import splitext

from accounts.models import Sender


def get_timestamp_path(instance, filename):
    return '{datetime_mark}{extension}'.format(
        datetime_mark=datetime.now().strftime('%Y%m%d%H%M%S'),
        extension=splitext(filename)[1]
    )


def send(subject, body, email):
    sender = Sender.objects.filter(name='sender').values('email')
    if len(sender) == 0:
        return

    send_mail(
        from_email=sender[0]['email'],
        subject=subject,
        message=strip_tags(body),
        html_message=body,
        recipient_list=email,
        fail_silently=False
    )
