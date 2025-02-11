import json

from django import forms
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

from payment_methods.domain.app import app
from payment_methods.domain.command.select_payment_method import SelectPaymentMethodCommand

class PaymentMethodForm(forms.Form):
    payment_type = forms.CharField()
    payment_details = forms.CharField()
    payment_status = forms.CharField()
    payment_validation = forms.CharField()
@method_decorator(csrf_exempt, name="dispatch")
class SelectPaymentMethodView(View):

    @staticmethod
    def put(_, payment_method_uuid):
        query = GetPaymentMethod(payment_method_uuid)
        result = app.execute_query(query)
        if not result:
            return JsonResponse(
                {"error": "PaymentMethod not found"},
                status=404
            )

        command = SelectPaymentMethodCommand(payment_method_uuid)
        app.execute_command(command)

        return JsonResponse(
            {"message": "PaymentMethod closed successfully!", "payment_method_uuid": command.payment_method_uuid},
            status=200
        )
