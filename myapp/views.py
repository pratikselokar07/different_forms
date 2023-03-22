from django.shortcuts import redirect, render
from django.views import View
# from django.views import View
from myapp.forms import StudentModelForm,StudentBasicForm
from django.forms import formset_factory
from myapp.models import Student

def StudentBasicFormView(request):
    if request.method=='POST':
        form=StudentBasicForm(request.POST)
        if form.is_valid():
            student=Student(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data['phone'],
            )
            student.save()  # save student to database
            return render(request, 'success.html')
    else:
        form=StudentBasicForm()
    return render(request, 'basic_form.html',{'form':form})


def StudentModelFormView(request):
    if request.method=='POST':
        form=StudentModelForm(request.POST)
        if form.is_valid():
            print("valid")
            form.save()
            return render(request, 'success.html')
    else:
        form=StudentModelForm()
        return render(request, 'model_form.html',{'form':form})

def success(request):
    return render(request,'success.html')

def StudentFormSetView(request):
    StudentFormSet=formset_factory(StudentBasicForm, extra=1)
    if request.method=='POST':
        formset=StudentFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                student=Student(
                    name=form.cleaned_data['name'],
                    email=form.cleaned_data['email'],
                    phone=form.cleaned_data['phone'],
                )
                student.save()
            return render(request, 'success.html')
    else:
        formset=StudentFormSet()
    return render(request, 'form_set.html',{'formset':formset})

def StudentList(request):
    students=Student.objects.all()
    return render(request,'student_list.html',{'students':students})