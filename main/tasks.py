from django.conf import settings

from celery import shared_task
from celery.schedules import crontab

from py_dev_user.utilities import send
from py_dev_user.celery import app

from .models import Subscriber
from .models import ItemReports


def report():
    html_table = """
<h3>Здравствуйте {user_name},</h3>

<p>Появился товар, который может Вас заинтересовать:</p>
    
<table>
    <tr>
        <th>Title</th>
        <th>Description</th>
        <th>Price</th>
        <th>Details</th>
    </tr>
    {contents}
</table>
    """

    html_content = """
<tr>
    <td>{title}</td>
    <td>{description}</td>
    <td>{price} {currency}</td>
    <td>{link}</td>
<tr>
    """

    if settings.ALLOWED_HOSTS:
        host = 'http://' + settings.ALLOWED_HOSTS[0]
    else:
        host = 'http://localhost:8000'

    subscribers = Subscriber.objects.all()
    records = ItemReports.objects.filter(is_send=False)

    if len(records) == 0:
        return

    content = list()

    for record in records:
        content.append(html_content.format(
                title=record.item.short_name,
                description=record.item.description,
                price=record.item.price,
                currency=record.item.currency,
                link='{host}/main/item/{item_id}/'.format(
                    host=host,
                    item_id=record.item.id
                )
            )
        )

        record.is_send = True
        record.save()

    contents = '\n'.join(row for row in content)

    for subscriber in subscribers:
        message = html_table.format(
            user_name=subscriber.user.last_name + ', ' + subscriber.user.first_name,
            contents=contents
        )

        send('Новые поступления.', message, [subscriber.user.email, ])


@shared_task
def one():
    print('one')


@shared_task
def two():
    print('two')


@shared_task
def three():
    print('three')


app.conf.beat_schedule = {
    'task_one': {
        'task': 'main.tasks.one',
        'schedule': 2
    },
    'task_two': {
        'task': 'main.tasks.two',
        'schedule': 4
    },
    'task_three': {
        'task': 'main.tasks.three',
        'schedule': 6
    }
}
