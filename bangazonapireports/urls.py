from django.urls import path
from .views import userfavorite_list

urlpatterns = [
    path('reports/userfavorite', userfavorite_list),
]