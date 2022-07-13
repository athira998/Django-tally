from django.urls import path,include
from.import views


urlpatterns = [

    path('',views.base,name='base'),
    path('index',views.index,name='index'),
    path('group',views.group,name='group'),
    path('branch',views.branch,name='branch'),
    path('ledger',views.ledger,name='ledger'),
    path('primary',views.primary,name='primary'),
    path('costcat',views.costcat,name='costcat'),
    path('costcentr',views.costcentr,name='costcentr'),
    path('voucher',views.voucher,name='voucher'),
    path('vouchpage',views.vouchpage,name='vouchpage'),



    path('load_employee_group',views.load_employee_group,name='load_employee_group'),
    path('load_employee',views.load_employee,name='load_employee'),
    path('load_unit_creation',views.load_unit_creation,name='load_unit_creation'),
    path('load_attendance',views.load_attendance,name='load_attendance'),
    path('load_payroll_voucher',views.load_payroll_voucher,name='load_payroll_voucher'),
    path('load_bank_details',views.load_bank_details,name='load_bank_details'),
    path('load_attendance_1',views.load_attendance_1,name='load_attendance_1'),
    path('load_attendance_2',views.load_attendance_2,name='load_attendance_2'),




    
]