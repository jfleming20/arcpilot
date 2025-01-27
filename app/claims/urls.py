from django.urls import path

from claims import views

urlpatterns = [
    path("/<str:claim_uuid>/close-claim", views.CloseClaimView.as_view(), name="close_claim"),
    path("/<str:claim_uuid>/assign-claim-to-adjuster", views.AssignClaimToAdjusterView.as_view(), name="assign_claim_to_adjuster")
]
