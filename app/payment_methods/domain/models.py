from dataclasses import dataclass

from payment_methods.models import DjangoPaymentMethod


@dataclass
class PaymentMethod:
    uuid: str
    payment_type: str
    payment_details: str
    payment_status: str
    payment_validation: bool

    @staticmethod
    def from_django(django_payment_method: DjangoPaymentMethod):
        return PaymentMethod(
            uuid=django_payment_method.uuid,
            payment_type=django_payment_method.payment_type,
            payment_details=django_payment_method.payment_details,
            payment_status=django_payment_method.payment_status,
            payment_validation=django_payment_method.payment_validation
        )

    def to_django(self):
        return DjangoPaymentMethod(
            uuid=self.uuid,
            payment_type=self.payment_type,
            payment_details=self.payment_details,
            payment_status=self.payment_status,
            payment_validation=self.payment_validation
        )

    def to_dict(self):
        return {
            "uuid": self.uuid,
            "payment_type": self.payment_type,
            "payment_details": self.payment_details,
            "payment_status": self.payment_status,
            "payment_validation": self.payment_validation
        }
