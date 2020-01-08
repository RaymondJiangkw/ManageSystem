from django.urls import path

from . import views
app_name = "search"
urlpatterns = [
    path('',views.index,name = 'index'),
    path('<int:lesson_id>/',views.detail,name = "detail")
]
