from rest_framework import serializers
from .models import Employee, Payroll, Department, Manager
from django.contrib.auth.models import User


class PayrollSerializer(serializers.ModelSerializer):
    gross_salary = serializers.SerializerMethodField(read_only=True)

    def get_gross_salary(self, payroll):
        return (payroll.basic_salary + (payroll.extra_work_hours * payroll.extra_paid)
                + payroll.bonus - ((payroll.income_tax / payroll.percent) * payroll.basic_salary))

    class Meta:
        model = Payroll
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class EmployeeSerializer(serializers.ModelSerializer):
    payrolls = PayrollSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ['user', 'manager', 'payrolls']


class DepartmentSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ['dep_name', 'dep_place', 'manager', 'employees']


class ManagerSerializer(serializers.ModelSerializer):
    departments = DepartmentSerializer(many=True, read_only=True)
    employees = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Manager
        fields = ['employee', 'departments', 'employees']
