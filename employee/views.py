from django.shortcuts import render
from django.views import View
from .models import *
from django.db.models import *
from django.http import JsonResponse
# Create your views here.
class MyEmployee(View):#มีViewด้วย
    def get(self,request):
        empall = Employee.objects.all().order_by('id')
        empcount = empall.count()
        popo = {'emp':empall,'count':empcount}
        #return render (request ต้องมี,"ชื่อไฟลhtmlที่จะใช้",ตัวแปรที่จะส่งข้อมูลไปเป็นdict)
        return render (request,"employee.html",popo)
class MyPosition(View):#มีViewด้วย
    def get(self,request):
        posall = Position.objects.annotate(countpos=Count('employee')).order_by('id')
        pos = {'pos':posall}
        
        #return render (request ต้องมี,"ชื่อไฟลhtmlที่จะใช้",ตัวแปรที่จะส่งข้อมูลไปเป็นdict)
        return render (request,"position.html",pos)
class MyProject(View):#มีviewด้วย
    def get(self,request):
        proall = Project.objects.all().order_by('id')
        pro = {'pro':proall}
        return render (request,"project.html",pro)
    def delete(self,request,pro_id):#ถ้ามันได้parameter จาก method ใส่ไว้ข้างหลัง requestต้องมีself request ทั้งสอง
        Project.objects.filter(id=pro_id).delete()
        return JsonResponse({'Status':'success'}, status=200)
class MyProjectDetail(View):
    def get(self,request,pro_id):
        projectde = Project.objects.get(id=pro_id)
        start_date = projectde.start_date.strftime('%Y-%m-%d')
        due_date = projectde.due_date.strftime('%Y-%m-%d')
        allstaff=projectde.staff.all()
        runout = {'projecdetail':projectde,'start_date':start_date,'due_date':due_date,'staff':allstaff}
        return render (request,"project_detail.html",runout)
    def put(self,request,pro_id,emp_id):
        projectadd = Project.objects.get(id=pro_id)
        empadd = Employee.objects.get(id=emp_id)
        projectadd.staff.add(empadd)
        return JsonResponse({'Status': 'Employee added'}, status=200)
    def delete(self,request,pro_id,emp_id):
        projectdel = Project.objects.get(id=pro_id)
        empdel = Employee.objects.get(id=emp_id)
        projectdel.staff.remove(empdel)
        return JsonResponse({'Status': 'Employee Kicked'}, status=200)