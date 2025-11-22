from django.contrib import admin
from .models import Employee, Department, Poste, Conge, Prime

@admin.register(Employee)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ('prenom', 'nom', 'departement', 'poste')
    search_fields = ('prenom', 'nom')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass

@admin.register(Poste)
class PosteAdmin(admin.ModelAdmin):
    pass

@admin.register(Conge)
class CongeAdmin(admin.ModelAdmin):
    list_display = ('employe', 'date_debut', 'date_fin', 'statut')
    list_filter = ('statut',)

@admin.register(Prime)
class PrimeAdmin(admin.ModelAdmin):
    list_display = ('employe', 'montant', 'motif', 'date_attribution')