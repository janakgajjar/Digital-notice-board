from django.urls import path
from . import views

app_name = 'notices'

urlpatterns = [
    path('', views.notice_board, name='notice_board'),
    path('department/<str:department>/<str:semester>/', 
         views.department_notice_view, 
         name='department_notices'),
]
