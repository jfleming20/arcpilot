from abc import ABC, abstractmethod
from typing import Optional

from payment_methods.domain.models import PaymentMethod
from payment_methods.models import DjangoPaymentMethod


class PaymentMethodRepository(ABC):
    @abstractmethod
    def save(self, payment_method: PaymentMethod) -> None:
        pass

    @abstractmethod
    def get(self, payment_method_uuid: str) -> Optional[PaymentMethod]:
        pass

    @abstractmethod
    def update(self, payment_method: PaymentMethod) -> None:
        pass

class DjangoPaymentMethodRepository(PaymentMethodRepository):
    def save(self, payment_method: PaymentMethod) -> None:
        payment_method.to_django().save()

    def get(self, payment_method_uuid: str) -> Optional[PaymentMethod]:
        try:
            django_payment_method = DjangoPaymentMethod.objects.get(uuid=payment_method_uuid)
        except DjangoPaymentMethod.DoesNotExist:
            return None
        return PaymentMethod.from_django(django_payment_method)

    def update(self, payment_method: PaymentMethod) -> None:
        django_payment_method = payment_method.to_django()
        django_payment_method.save()

payment_method_repository = DjangoPaymentMethodRepository()
