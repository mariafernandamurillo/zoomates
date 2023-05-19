from django.urls import path
from accounts import views

urlpatterns = [
    path("signup/", views.SignmUpView.as_view(), name="signup"),
]