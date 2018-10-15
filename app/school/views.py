from django.shortcuts import render

# Create your views here.
from school.models import School, Student


def school_list(request):
    schools = School.objects.all()
    context = {
        'schools': schools
    }
    return render(request, 'index.html', context)


def school_detail(request, pk):
    school = School.objects.get(pk=pk)
    students = Student.objects.get(school=pk)
    context = {
        'school': school,
        'students': students,
    }
    return render(request, 'school_detail.html', context)
