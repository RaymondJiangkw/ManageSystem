from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
from .models import Lesson
# Create your views here.
def index(request):
    lessons = Lesson.objects.all()[:50]
    context = {'lessons':lessons}
    return render(request,'search/index.html',context)
def detail(request,lesson_id):
    lesson = get_object_or_404(Lesson,pk = lesson_id)
    return render(request,"search/detail.html",{"lesson":lesson})
def modify(request):
    pre_text = "Modify Page."
    return HttpResponse(request,pre_text)
def add(request):
    return render(request,"search/add.html")
