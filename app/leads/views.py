import json

from django import forms
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

from leads.domain.app import app
class LeadForm(forms.Form):
