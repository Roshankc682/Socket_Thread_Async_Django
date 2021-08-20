from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.student_details),
    path('student/', views.generate_studen_data),

]
