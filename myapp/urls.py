from django.urls import path
from .import views


urlpatterns = [
    path('basic_form/',views.StudentBasicFormView,name='basic_form'),
    path('model_form/',views.StudentModelFormView,name='model_form'),
    path('form_set/',views.StudentFormSetView,name='form_set'),
    path('success/',views.success,name='success'),
    path('student_list/',views.StudentList,name='student_list'),
]
