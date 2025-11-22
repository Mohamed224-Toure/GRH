from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from Employes.forms import EmployeeForm
from .models import Employee
from .models import Conge
from .models import Prime
from django.contrib import messages   # ← Ligne CORRECTEfrom .forms import EmployeeForm

@login_required
def home(request):
    return render(request, 'Employes/home.html')

@login_required
def employee_list(request):
    employes = Employee.objects.all()
    return render(request, 'Employes/employes_list.html', {'employes': employes})

@login_required
def employee_detail(request, pk):
    employe = get_object_or_404(Employee, pk=pk)
    return render(request, 'Employes/employes_detail.html', {'employe': employe})

@login_required
def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Employes:employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'Employes/employes_form.html', {'form': form})

@login_required
def employee_update(request, pk):
    Employe = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=Employe)
        if form.is_valid():
            form.save()
            return redirect('Employes:employee_list')
    else:
        form = EmployeeForm(instance=Employe)
    return render(request, 'Employes/employes_form.html', {'form': form})

@login_required
def employee_delete(request, pk):
    employe = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employe.delete()
        return redirect('Employes:employee_list')
    return render(request, 'Employes/employes_delete.html', {'employe': employe})

# === Vues Congés ===
@login_required
def conge_list(request):
    conges = Conge.objects.all().order_by('-date_demande')
    return render(request, 'Employes/conge_list.html', {'conges': conges})

@login_required
def conge_new(request):
    if request.method == 'POST':
        employe_id = request.POST['employe']
        employe = Employee.objects.get(id=employe_id)
        Conge.objects.create(
            employe=employe,
            date_debut=request.POST['date_debut'],
            date_fin=request.POST['date_fin'],
            motif=request.POST['motif']
        )
        messages.success(request, "Demande de congé envoyée !")
        return redirect('Employes:conge_list')
    employes = Employee.objects.all()
    return render(request, 'Employes/conge_form.html', {'employes': employes})

# === Vues Primes ===
@login_required
def prime_list(request):
    primes = Prime.objects.all().order_by('-date_attribution')
    return render(request, 'Employes/prime_list.html', {'primes': primes})

@login_required
def prime_new(request):
    if request.method == 'POST':
        employe_id = request.POST['employe']
        employe = Employee.objects.get(id=employe_id)
        Prime.objects.create(
            employe=employe,
            montant=request.POST['montant'],
            motif=request.POST['motif']
        )
        messages.success(request, "Prime attribuée avec succès !")
        return redirect('Employes:prime_list')
    employes = Employee.objects.all()
    return render(request, 'Employes/prime_form.html', {'employes': employes})