"""
URL configuration for employee_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from employee import views
from employee.views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("employee/", MyEmployee.as_view(),name='employeepage'),
    path("position/", MyPosition.as_view(),name='positionpage'),
    path("project/", MyProject.as_view(),name='projectpage'),
    path("project/delete/<int:pro_id>/", MyProject.as_view(),name='deletepro'),
    path("project/project_detail/<int:pro_id>/", MyProjectdetail.as_view(),name='projectdetailpage'),
    path("project/project_detail/<int:pro_id>/<int:emp_id>/", MyProjectdetail.as_view(),name='adddelprojectstaff'),
]
