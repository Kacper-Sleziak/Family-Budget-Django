from django.urls import path

from .views.transaction import CreateTransaction

urlpatterns = [path("create_transaction/<int:budget_pk>", CreateTransaction.as_view())]
