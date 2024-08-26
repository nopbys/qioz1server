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
#from ชื่อไฟล.views import *import ทุกอย่างจากไฟล view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("employee/", MyEmployee.as_view()),
    path("position/", MyPosition.as_view()),
    path("project/", MyProject.as_view()),
    path("project/delete/<int:pro_id>/", MyProject.as_view()),####เอาไว้deleteในหน้าเดียวกับ project
    path("project/project_detail/<int:pro_id>/", MyProjectDetail.as_view()),
    path("project/project_detail/<int:pro_id>/<int:emp_id>/", MyProjectDetail.as_view()),
]