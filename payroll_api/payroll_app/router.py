from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('user', views.ListUsers, basename='user'),
router.register('employee', views.EmployeeViewSet, basename='employee'),
router.register('manager', views.ManagerViewSet, basename='manager'),
router.register('department', views.DepartmentVieSet, basename='department'),
router.register('payroll', views.PayrollViewSet, basename='payroll'),
