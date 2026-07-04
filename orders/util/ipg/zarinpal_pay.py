from django.http import HttpRequest
from zarinpal_utils.Config import Config
from zarinpal import ZarinPal

from orders.model.enumeration.payment_status import PaymentStatus
from orders.model.transaction import Transaction

config = Config(
    merchant_id="dc9394fa-c263-11e7-a5f9-000c295eb8fc",
    sandbox=True,
)


def payment_gateway(transaction: Transaction):
    try:
        zp = ZarinPal(config)
        payment = zp.payments.create({
            "amount":float(transaction.amount * 10),
            "description": f"Order #{transaction.order.pk}",
            "callback_url": "http://127.0.0.1:8000/verify/",
        })

        if payment['errors']:
            raise Exception(payment['errors'])

        authority = payment['data']['authority']
        transaction.authority = authority
        transaction.save()

        return f'{zp.get_base_url()}/pg/StartPay/{authority}'

    except Exception as e:
        print("Error on zarinpal payment: ", e)
        return None


def verify_payment(request: HttpRequest, transaction: Transaction):
    try:
        zp = ZarinPal(config)
        verif = zp.verifications.verify({
            'merchant_id': config.merchant_id,
            'amount': float(transaction.amount * 10),
            'authority': transaction.authority
        })

        if verif['errors']:
            raise Exception(verif['errors'])

        if verif['data']['code'] >= 100:
            transaction.ref_id = verif['data']['ref_id']
            transaction.code = verif['data']['code']
            transaction.message = verif['data']['message']
            transaction.card_hash = verif['data']['card_hash']
            transaction.card_pan = verif['data']['card_pan']
            transaction.status = PaymentStatus.PAID
            transaction.order.status = PaymentStatus.PAID
        else:
            transaction.status = PaymentStatus.FAILED
            transaction.order.status = PaymentStatus.FAILED

        transaction.save()
        transaction.order.save()

        return transaction

    except Exception as e:
        print("Error on zarinpal payment: ", e)
        return None
