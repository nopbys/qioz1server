from django.shortcuts import render
from django.views import View
from .models import *
from django.db.models import *
from django.http import JsonResponse
# Create your views here.
class MyEmployee(View):
        def get(self,request):
            empall = Employee.objects.all().order_by('id')
            empcount = empall.count()
            popo = {'emp':empall,'count':empcount}
            return render(request,"employee.html",popo)
        
class MyPosition(View):
        def get(self,request):
            posall = Position.objects.annotate(countpos=Count('employee')).order_by('id')
            pos = {'pos':posall} 
            return render(request,"position.html",pos)
        
class MyProject(View):
        def get(self,request):
            proall = Project.objects.all().order_by('id')
            pro = {'pro':proall} 
            return render(request,"project.html",pro)
        def delete(self,request,pro_id):
            Project.objects.filter(id=pro_id).delete()
            return JsonResponse({'Status':'success'}, status=200)
class MyProjectdetail(View):
        def get(self,request,pro_id):
            projectde = Project.objects.get(id=pro_id)
            start_date = projectde.start_date.strftime('%Y-%m-%d')
            due_date = projectde.due_date.strftime('%Y-%m-%d')
            allstaff = projectde.staff.all()
            prode = {'projectde':projectde,'start_date':start_date,'due_date':due_date,'staff':allstaff}
            return render(request,"project_detail.html",prode)
        def put(self,request,pro_id,emp_id):
            projectno = Project.objects.get(id = pro_id)
            empno = Employee.objects.get(id = emp_id)
            projectno.staff.add(empno)
            return JsonResponse({'status': 'เพิ่มพนักงานสำเร็จ'}, status=200)
        def delete(self, request, pro_id, emp_id):
            project = Project.objects.get(id=pro_id)
            employee = Employee.objects.get(id=emp_id)
            project.staff.remove(employee)
            return JsonResponse({'status': 'ลบพนักงานละ'}, status=200)

                      
              
              
