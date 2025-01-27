from abc import ABC, abstractmethod
from typing import Optional

from claims.domain.models import Claim
from claims.models import DjangoClaim


class ClaimRepository(ABC):
    @abstractmethod
    def save(self, claim: Claim) -> None:
        pass

    @abstractmethod
    def get(self, claim_uuid: str) -> Optional[Claim]:
        pass

    @abstractmethod
    def update(self, claim: Claim) -> None:
        pass

class DjangoClaimRepository(ClaimRepository):
    def save(self, claim: Claim) -> None:
        claim.to_django().save()

    def get(self, claim_uuid: str) -> Optional[Claim]:
        try:
            django_claim = DjangoClaim.objects.get(uuid=claim_uuid)
        except DjangoClaim.DoesNotExist:
            return None
        return Claim.from_django(django_claim)

    def update(self, claim: Claim) -> None:
        django_claim = claim.to_django()
        django_claim.save()

claim_repository = DjangoClaimRepository()
