from celery import shared_task
from mail_templated import send_mail

@shared_task
def notify_order_saved(order_pk, promocode):
    # from time import sleep
    # sleep(3)

    send_mail(
        "email/order-updated.html",
        {
            "order_pk" : order_pk,
            "order_promocode": promocode,
        },
        "admin@shopsales.com",
        ["manager@shopsales.com"],
        fail_silently=False,
    )