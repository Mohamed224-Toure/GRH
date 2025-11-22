from django.urls import path
from . import views

app_name = 'Employes'
urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('employee/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('employee/new/', views.employee_create, name='employee_create'),
    path('employee/<int:pk>/edit/', views.employee_update, name='employee_update'),
    path('employee/<int:pk>/delete/', views.employee_delete, name='employee_delete'),
    path('conges/', views.conge_list, name='conge_list'),
    path('conges/nouveau/', views.conge_new, name='conge_new'),
    path('primes/', views.prime_list, name='prime_list'),
    path('primes/nouvelle/', views.prime_new, name='prime_new'),
]