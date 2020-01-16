from django.urls import path

from . import views
app_name = "search"
urlpatterns = [
    path('',views.index,name = 'index'),
    path('<int:number>/',views.index,name = 'index'),
    path('<int:number>/<int:page>/',views.index,name = 'index'),
    path('detail/<int:lesson_id>/',views.detail,name = "detail"),
    path('modify/<int:lesson_id>',views.modify,name = "modify"),
    path('delete/',views.delete,name = "delete"),
    path('add/',views.add_html,name = "add"),
    path('add_behavior/',views.add,name = "add_behavior"),
    path('filter/',views.filter,name = "filter"),
]
