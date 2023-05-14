from django.urls import path
from . import views
from .router import router

urlpatterns = [
    path('name_filter/<str:name>', views.FilterByName.as_view()),
    path('salary_filter/<int:salary>', views.FilterBySalary.as_view()),
    path('manager_filter/<int:id>', views.FilterByManager.as_view()),
]

urlpatterns = urlpatterns + router.urls
