from django.urls import path

from .views.budget import BudgetViewSet
from .views.transaction import CreateTransaction

urlpatterns = [
    path("create_transaction/<int:budget_pk>", CreateTransaction.as_view()),
    path("budgetViewSet", BudgetViewSet.as_view({"get": "list"})),
]
