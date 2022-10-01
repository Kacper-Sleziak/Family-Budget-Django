from django.urls import path
from rest_framework.routers import DefaultRouter

from .views.budget import BudgetViewSet
from .views.list import ListViewSet
from .views.transaction import CreateTransaction

router = DefaultRouter()
router.register(r"lists", ListViewSet, basename="user")

urlpatterns = [
    path("create_transaction/<int:budget_pk>", CreateTransaction.as_view()),
    path("budgetViewSet", BudgetViewSet.as_view({"get": "list"})),
]

urlpatterns += router.urls
