import json

from django import forms
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

from claims.domain.app import app
from claims.domain.command.close_claim import CloseClaimCommand

from claims.domain.command.assign_claim_to_adjuster import AssignClaimToAdjusterCommand

class ClaimForm(forms.Form):
    claim_id = forms.CharField()
    claim_status = forms.CharField()
    claimant_name = forms.CharField()
    claim_amount = forms.CharField()
    claim_date = forms.CharField()
    claim_closure_date = forms.CharField()
    claim_documents = forms.CharField()
@method_decorator(csrf_exempt, name="dispatch")
class CloseClaimView(View):

    @staticmethod
    def put(_, claim_uuid):
        query = GetClaim(claim_uuid)
        result = app.execute_query(query)
        if not result:
            return JsonResponse(
                {"error": "Claim not found"},
                status=404
            )

        command = CloseClaimCommand(claim_uuid)
        app.execute_command(command)

        return JsonResponse(
            {"message": "Claim closed successfully!", "claim_uuid": command.claim_uuid},
            status=200
        )
@method_decorator(csrf_exempt, name="dispatch")
class AssignClaimToAdjusterView(View):

    @staticmethod
    def put(_, claim_uuid):
        query = GetClaim(claim_uuid)
        result = app.execute_query(query)
        if not result:
            return JsonResponse(
                {"error": "Claim not found"},
                status=404
            )

        command = AssignClaimToAdjusterCommand(claim_uuid)
        app.execute_command(command)

        return JsonResponse(
            {"message": "Claim closed successfully!", "claim_uuid": command.claim_uuid},
            status=200
        )
