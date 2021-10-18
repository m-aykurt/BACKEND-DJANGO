from django.shortcuts import redirect, render
from .forms import StudentForm
from django.contrib import messages

# from student.models import Student



def index(request):
    return render(request, 'student/index.html')

# form metodu ile olusturulan form yapısını kaydetme

def student_page(request):
    form = StudentForm()
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added succesfully")
            return redirect("index")

    form = StudentForm()
    context = {
        'form': form
    }
    return render(request, 'student/student.html', context)
