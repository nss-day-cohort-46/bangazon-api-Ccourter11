from django.urls import path
from .views import userfavorite_list, unpaidorders_list

urlpatterns = [
    path('reports/userfavorite', userfavorite_list),
    path('reports/unpaidorders', unpaidorders_list),
]