from django.urls import path
from .views import userfavorite_list, unpaidorders_list, completedorders_list, inexpensiveproduct_list, expensiveproduct_list

urlpatterns = [
    path('reports/userfavorite', userfavorite_list),
    path('reports/unpaidorders', unpaidorders_list),
    path('reports/completedorders', completedorders_list),
    path('reports/inexpensiveproducts', inexpensiveproduct_list),
    path('reports/expensiveproducts', expensiveproduct_list),
]