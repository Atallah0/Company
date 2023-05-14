from rest_framework import viewsets, generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import DepartmentSerializer, ManagerSerializer, EmployeeSerializer, PayrollSerializer, UserSerializer
from .models import Department, Manager, Employee, Payroll
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import authentication, permissions
from django.contrib.auth.models import User


class ListUsers(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        return self.queryset.filter(employees=self.request.user.pk).all()


class EmployeeViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user.pk).all()


class ManagerViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    serializer_class = ManagerSerializer
    queryset = Manager.objects.all()

    def get_queryset(self):
        return self.queryset.filter(employee=self.request.user.pk).all()


class DepartmentVieSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()

    def get_queryset(self):
        return self.queryset.filter(manager=self.request.user.pk).all()


class PayrollViewSet(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = (IsAuthenticated,)

    serializer_class = PayrollSerializer
    queryset = Payroll.objects.all()

    def get_queryset(self):
        return Payroll.objects.filter(employee=self.request.user.pk).all()


class FilterByName(APIView):
    def get(self, request, name):
        user = User.objects.filter(first_name=name)
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


class FilterBySalary(APIView):
    def get(self, request, salary):
        payroll = Payroll.objects.filter(basic_salary__gt=salary)
        serializer = PayrollSerializer(payroll, many=True)
        return Response(serializer.data)


class FilterByManager(APIView):
    def get(self, request, id):
        employee = Employee.objects.filter(manager__id=id)
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)
