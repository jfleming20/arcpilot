from uuid import uuid4

from payment_methods.domain.repositories import payment_method_repository

from outbox.domain.command.create_published import CreatePublishedCommand
from outbox.domain.app import app


class SelectPaymentMethodCommand:
    def __init__(self, payment_type: str, user_id: uuid.UUID):
        self.uuid = str(uuid4())
        self.payment_type = payment_type


        self.user_id = user_id


def select_payment_method_command_handler(command: SelectPaymentMethodCommand) -> str:
    payment_method = payment_method_repository.get(command.payment_method_uuid)
    # payment_method.closed = True
    payment_method_repository.update(payment_method)

    payment_method_selected_command = CreatePublishedCommand(
        destination="/topic/payment_method",
        body={"payment_method_uuid": payment_method.uuid}
    )

    payment_method_selection_failed_command = CreatePublishedCommand(
        destination="/topic/payment_method",
        body={"payment_method_uuid": payment_method.uuid}
    )

    app.execute_command(payment_method_selected_command)

    app.execute_command(payment_method_selection_failed_command)

    return payment_method.uuid
