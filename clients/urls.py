from django.urls import path
from . import views

urlpatterns = [
    path("clients/", views.ClientListCreateView.as_view()),
    path("clients/<str:cpf>/", views.ClientRetrieveUpdateDestroyView().as_view())
]
