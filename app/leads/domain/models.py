from dataclasses import dataclass

from leads.models import DjangoLead


@dataclass
class Lead:
    uuid: str

    @staticmethod
    def from_django(django_lead: DjangoLead):
        return Lead(
            uuid=django_lead.uuid
        )

    def to_django(self):
        return DjangoLead(
            uuid=self.uuid
        )

    def to_dict(self):
        return {
            "uuid": self.uuid
        }
