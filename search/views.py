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
# Return a list of generated full text.
def __decode_left_bracket(string):
    result = []
    left_posi = string.find('[')
    right_posi = string.find(']')
    pre_text = string[:left_posi].strip()
    latter_text = string[right_posi+1:].strip()
    inter_text = string[left_posi+1:right_posi].split(',')
    for txt in inter_text:
        txt = txt.strip()
        if (txt.find('-') == -1):
            result.append(pre_text+txt+latter_text)
        else:
            pre = txt[:txt.find('-')]
            # print(pre)
            latter = txt[txt.find('-')+1:]
            # print(latter)
            generated = []
            if (pre.isdigit() == True):
                # All number
                generated = list(range(int(pre),int(latter)+1))
                generated = list(map(lambda x:str(x),generated))
            else:
                # All alpha
                generated = list(range(ord(pre[0]),ord(latter[0])+1))
                generated = map(lambda x:chr(x),generated)
            for gene in generated:
                result.append(pre_text + gene + latter_text)
    return result
    
def check_valid(string):
    left_bracket = 0
    for chr in string:
        if (chr == '['):
            left_bracket += 1
        elif (chr == ']'):
            left_bracket -= 1
        if (left_bracket < 0):
            return False
    if (left_bracket > 0):
        return False
    return True

def __paraphrase(encoded_comp):
    para_result = []
    para_result.append(encoded_comp)
    if check_valid(encoded_comp):
        while (para_result[-1].find('[') != -1):
            decoded = __decode_left_bracket(para_result[-1])
            para_result.pop()
            for decoded_text in decoded:
                para_result.insert(0,decoded_text)
        return para_result
    else:
        return []

def __single_compare(comp,desti):
    comp = comp.strip()
    comp = __paraphrase(comp)
    for cmp in comp:
        if (desti.find(cmp) != -1):
            return True
    return False

def compare(comp_list,desti):
    for comp in comp_list:
        if __single_compare(comp,desti):
            return True
    return False

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
    context = {
        'filter':0,
        'page_range':1,
        'lessons':lessons,
        'page':page,
        'page_next':page+1,
        'page_pre':page-1,
        'number':number,
        "total_page":total_page,
        'keywords_name':"",
        'keywords_id':"",
        'keywords_week':"",
        'keywords_time':"",
        'keywords_collage':"",
        'keywords_school':"",
    }
    return render(request,'search/index.html',context)
def filter(request):
    lesson_name = str(request.POST['keywords_name']).split(';')
    lesson_id = str(request.POST['keywords_id']).split(';')
    lesson_week = str(request.POST['keywords_week']).split(';')
    lesson_time = str(request.POST['keywords_time']).split(';')
    lesson_collage = str(request.POST['keywords_collage']).split(';')
    lesson_school = str(request.POST['keywords_school']).split(';')
    Lessons = Lesson.objects.all()
    filter_result = []
    for lesson in Lessons:
        if compare(lesson_name,lesson.name):
            if compare(lesson_id,lesson.lesson_id):
                if compare(lesson_week,lesson.weeks):
                    if compare(lesson_time,lesson.time):
                        if compare(lesson_collage,lesson.collage):
                            if compare(lesson_school,lesson.school):
                                filter_result.append(lesson)
    return render(request,'search/index.html',{'lessons':filter_result,
        'filter':1,
        'page_range':0,
        'keywords_name':request.POST['keywords_name'],
        'keywords_id':request.POST['keywords_id'],
        'keywords_week':request.POST['keywords_week'],
        'keywords_time':request.POST['keywords_time'],
        'keywords_collage':request.POST['keywords_collage'],
        'keywords_school':request.POST['keywords_school'],
    })
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
