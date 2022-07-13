from django.shortcuts import render

# Create your views here.

def base(request):
    return render(request, 'base.html')

def index(request):
    return render(request, 'home.html')

def group(request):
    return render(request, 'groups.html')

def branch(request):
    return render(request, 'branch.html')

def ledger(request):
    return render(request, 'ledger.html')

def primary(request):
    return render(request, 'primarycost.html')

def costcat(request):
    return render(request, 'costcat.html')

def costcentr(request):
    return render(request, 'costcentr.html')

def voucher(request):
    return render(request, 'voucher.html')

def vouchpage(request):
    return render(request, 'vouchpage.html')


def load_employee_group(request):
    return render(request,'employee_group.html')


def load_employee(request):
    return render(request,'employee.html')

def load_unit_creation(request):
    return render(request,'unit_creation.html')

def load_attendance(request):
    return render(request,'attendance.html')

def load_payroll_voucher(request):
    return render(request,'payroll_voucher.html')

def load_bank_details(request):
    return render(request,'bank_details.html')

def load_attendance_1(request):
    return render(request,'attendance_1.html')

def load_attendance_2(request):
    return render(request,'attendance_2.html')
