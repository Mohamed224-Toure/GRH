from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import EmployeeForm

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
    employe = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employe)
        if form.is_valid():
            form.save()
            return redirect('Employes:employee_list')
    else:
        form = EmployeeForm(instance=employe)
    return render(request, 'Employes/employes_form.html', {'form': form})

@login_required
def employee_delete(request, pk):
    employe = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employe.delete()
        return redirect('Employes:employee_list')
    return render(request, 'Employes/employes_delete.html', {'employe': employe})