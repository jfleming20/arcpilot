from django.urls import path

from payment_methods import views

urlpatterns = [
    path("/<str:payment_method_uuid>/select-payment-method", views.SelectPaymentMethodView.as_view(), name="select_payment_method")
]
