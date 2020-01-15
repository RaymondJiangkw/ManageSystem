from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
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
def modify(request):
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
def add(request):
    return render(request,"search/add.html")
