from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from Employes.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(template_name='Employes/login.html'), name='login'),
    path('home/', home, name='home'),
    path('employees/', include('Employes.urls')),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]