from django.db import transaction
from django_outbox_pattern.payloads import Payload

from carts.domain.command.create_cart import CreateCartCommand
from carts.domain.app import app


def callback(payload: Payload):
    with transaction.atomic():
        command = CreateCartCommand(
            total_amount=payload.body.get("total_amount")
        )
        app.execute_command(command)
        payload.ack()
        payload.saved = True
        print("Cart created successfully!")
