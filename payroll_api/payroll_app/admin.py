# from django.contrib import admin
#
# from django.contrib import admin
# from .models import Manager, Employee
#
#
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email')
#
#     # def get_position(self, obj):
#     #     employee = Grade.objects.filter(id=obj.id)
#     #     return list(employee)
#     #
#     # def get_basic_salary(self, obj):
#     #     salary = Grade.objects.get(id=obj.id)
#     #     return str(salary.basic_salary)
#
#
# class ManagerAdmin(admin.ModelAdmin):
#     list_display = ('employee',)
#
#
# admin.site.register(Manager, ManagerAdmin)
# admin.site.register(Employee, EmployeeAdmin)
