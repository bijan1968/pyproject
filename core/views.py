from django.shortcuts import redirect,render
from django.views import View
from.models import Student
from.forms import AddStudentForm
from django.http import HttpResponse
from core.forms import RegistrationForm

# Create your views here.
class Home(View):
    def get(self,request):
        stu_data=Student.objects.all()
        return render(request,'core/home.html',{'studata':stu_data})

class Add_Student(View):
    def get(self,request):
        fm=AddStudentForm()
        return render(request,'core/add_student.html',{'form':fm})

    def post(self,request):
        fm=AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
            return render(request,'core/add_student.html',{'form':fm})

class Delete_Student(View):
    def post(self,request):
        data=request.POST
        id= data.get('id')
        #print(id)
        studata=Student.objects.get(id=id)
        #print(studata)
        studata.delete()
        return redirect('/')

class EditStudent(View):
    def get(self,request,id):
        stu=Student.objects.get(id=id)
        fm=AddStudentForm(instance=stu)
        return render(request, 'core/edit_student.html',{'form':fm})

    def post(self,request,id):
        stu=Student.objects.get(id=id)
        fm = AddStudentForm(request.POST,instance=stu)
        if fm.is_valid():
            fm.save()
            return redirect('/')

class Reg(View):

    def get(self,request):
        if request.User.is_authenticated:
            return HttpResponse('already login')
        else:
            form=RegistrationForm()
        context={
               'form':form
        }

        return render(request, 'core/register.html',context)
