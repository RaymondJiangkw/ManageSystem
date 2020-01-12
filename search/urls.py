from django.urls import path

from . import views
app_name = "search"
urlpatterns = [
    path('',views.index,name = 'index'),
    path('detail/<int:lesson_id>/',views.detail,name = "detail"),
    path('modify/',views.modify,name = "modify"),
    path('add/',views.add,name = "add"),
]
