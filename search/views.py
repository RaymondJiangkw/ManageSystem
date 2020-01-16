from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Lesson
# Create your views here.
def min(a,b):
    if (a > b):
        return b
    else:
        return a

def index(request,number = 50,page = 1):
    begin_item = number * (page - 1)
    end_item = number * (page)
    lessons_all = Lesson.objects.all()
    cnt = lessons_all.count()
    end_item = min(end_item,cnt)
    lessons = lessons_all[begin_item:end_item]
    total_page = 0
    if (cnt % number == 0):
        total_page = cnt / number
    else:
        total_page = cnt // number + 1
    context = {'lessons':lessons,'page':page,'page_next':page+1,'page_pre':page-1,'number':number,"total_page":total_page}
    return render(request,'search/index.html',context)
def detail(request,lesson_id):
    lesson = get_object_or_404(Lesson,pk = lesson_id)
    return render(request,"search/detail.html",{"lesson":lesson})
def delete(request):
    post_context = str(request.body)
    post_context = post_context.replace("'","")
    post_context = post_context.split("&")
    post_context = [post.split("=") for post in post_context]
    del_list = []
    for post in post_context:
        if (post[0]=="choose"):
            lesson = get_object_or_404(Lesson,pk=post[1])
            lesson.delete()
            del_list.append(post[1])
    message = "Have successfully delete " + ",".join(del_list)
    return HttpResponse(message)
def add_html(request):
    return render(request,"search/add.html")
def add(request):
    preserve = 0
    try:
        preserve = request.POST['preserve']
    except:
        pass
    lesson = Lesson(
        name = request.POST['name'],
        teacher = request.POST['teacher'],
        capacity = request.POST['capacity'],
        classroom = request.POST['classroom'],
        supplement = request.POST['supplement'],
        collage = request.POST['collage'],
        school = request.POST['school'],
        lesson_id = request.POST['lesson_id'],
        score = request.POST['score'],
        time = request.POST['time'],
        weeks = request.POST['weeks']
    )
    lesson.save()
    #pass_values = {'preserve':preserve,
    #    'p_collage':request.POST['collage'],
    #    'p_school':request.POST['school'],
    #    'p_time':request.POST['time'],
    #    'p_weeks':request.POST['weeks']
    #}
    return HttpResponseRedirect(reverse("search:add"))

def modify(request,lesson_id):
    lesson = get_object_or_404(Lesson,pk = lesson_id)
    lesson.name = request.POST['name']
    lesson.teacher = request.POST['teacher']
    lesson.capacity = request.POST['capacity']
    lesson.classroom = request.POST['classroom']
    lesson.supplement = request.POST['supplement']
    lesson.collage = request.POST['collage']
    lesson.school = request.POST['school']
    lesson.lesson_id = request.POST['lesson_id']
    lesson.score = request.POST['score']
    lesson.time = request.POST['time']
    lesson.weeks = request.POST['weeks']
    lesson.save()
    return HttpResponseRedirect(reverse("search:detail",args = (lesson_id,)))
