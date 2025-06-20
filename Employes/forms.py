from django import forms
from .models import Employee, Department, Poste

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['prenom', 'nom', 'email', 'date_embauche', 'salaire', 'departement', 'poste', 'sexe', 'est_actif']
        widgets = {
            'date_embauche': forms.DateInput(attrs={'type': 'date'}),
            'sexe': forms.Select(),
            'departement': forms.Select(),
            'poste': forms.Select(),
        }