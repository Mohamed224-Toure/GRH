from django.contrib import admin
from .models import Department, Poste, Employee

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')
    search_fields = ('nom',)

@admin.register(Poste)
class PosteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')
    search_fields = ('nom',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'email', 'departement', 'poste', 'sexe', 'salaire', 'est_actif')
    list_filter = ('departement', 'poste', 'sexe', 'est_actif')
    search_fields = ('prenom', 'nom', 'email')
    date_hierarchy = 'date_embauche'