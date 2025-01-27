from dataclasses import dataclass

from claims.models import DjangoClaim


@dataclass
class Claim:
    uuid: str
    claim_id: uuid.UUID
    claim_status: str
    claimant_name: str
    claim_amount: float
    claim_date: datetime.date
    claim_closure_date: datetime.date
    claim_documents: list[str]

    @staticmethod
    def from_django(django_claim: DjangoClaim):
        return Claim(
            uuid=django_claim.uuid,
            claim_id=django_claim.claim_id,
            claim_status=django_claim.claim_status,
            claimant_name=django_claim.claimant_name,
            claim_amount=django_claim.claim_amount,
            claim_date=django_claim.claim_date,
            claim_closure_date=django_claim.claim_closure_date,
            claim_documents=django_claim.claim_documents
        )

    def to_django(self):
        return DjangoClaim(
            uuid=self.uuid,
            claim_id=self.claim_id,
            claim_status=self.claim_status,
            claimant_name=self.claimant_name,
            claim_amount=self.claim_amount,
            claim_date=self.claim_date,
            claim_closure_date=self.claim_closure_date,
            claim_documents=self.claim_documents
        )

    def to_dict(self):
        return {
            "uuid": self.uuid,
            "claim_id": self.claim_id,
            "claim_status": self.claim_status,
            "claimant_name": self.claimant_name,
            "claim_amount": self.claim_amount,
            "claim_date": self.claim_date,
            "claim_closure_date": self.claim_closure_date,
            "claim_documents": self.claim_documents
        }
