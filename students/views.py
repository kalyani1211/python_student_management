from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Student
from .forms import StudentForm

def student_list(request):
    students = Student.objects.filter(is_deleted=False)
    paginator = Paginator(students, 5)
    page = request.GET.get('page')
    students_page = paginator.get_page(page)
    return render(request, 'students/student_list.html', {'students': students_page})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.is_deleted = True
    student.save()
    return redirect('student_list')

def student_search(request):
    query = request.GET.get('q', '')
    students = Student.objects.filter(student_name__icontains=query, is_deleted=False)
    return render(request, 'students/student_list.html', {'students': students})

