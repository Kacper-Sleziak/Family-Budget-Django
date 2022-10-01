from functools import partial

from rest_framework import generics, mixins, views
from utils.permissions import ListCreatorPermission

from ..serializers.budget import DefaultBudgetSerializer
