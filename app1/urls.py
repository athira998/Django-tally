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
    path('load_unit_compound',views.load_unit_compound,name='load_unit_compound'),
    path('load_attendance',views.load_attendance,name='load_attendance'),
    path('load_payroll_voucher',views.load_payroll_voucher,name='load_payroll_voucher'),
    path('load_bank_details',views.load_bank_details,name='load_bank_details'),
    path('load_attendance_1',views.load_attendance_1,name='load_attendance_1'),
    path('load_attendance_2',views.load_attendance_2,name='load_attendance_2'),
    path('load_pay_head_noapp',views.load_pay_head_noapp,name='load_pay_head_noapp'),
    path('load_pay_head_deduction',views.load_pay_head_deduction,name='load_pay_head_deduction'),
    path('load_pay_head_earning',views.load_pay_head_earning,name='load_pay_head_earning'),
    path('load_pay_head_loans',views.load_pay_head_loans,name='load_pay_head_loans'),
    path('load_demo',views.load_demo,name='load_demo'),





    
]