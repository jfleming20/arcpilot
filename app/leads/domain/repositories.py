from abc import ABC, abstractmethod
from typing import Optional

from leads.domain.models import Lead
from leads.models import DjangoLead


class LeadRepository(ABC):
    @abstractmethod
    def save(self, lead: Lead) -> None:
        pass

    @abstractmethod
    def get(self, lead_uuid: str) -> Optional[Lead]:
        pass

    @abstractmethod
    def update(self, lead: Lead) -> None:
        pass

class DjangoLeadRepository(LeadRepository):
    def save(self, lead: Lead) -> None:
        lead.to_django().save()

    def get(self, lead_uuid: str) -> Optional[Lead]:
        try:
            django_lead = DjangoLead.objects.get(uuid=lead_uuid)
        except DjangoLead.DoesNotExist:
            return None
        return Lead.from_django(django_lead)

    def update(self, lead: Lead) -> None:
        django_lead = lead.to_django()
        django_lead.save()

lead_repository = DjangoLeadRepository()
