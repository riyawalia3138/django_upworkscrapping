from django.urls import path
from .import views
from upwork_app.views import get_data#,get_all_values

app_name = 'upwork_app'

urlpatterns = [

    path('', get_data, name='upwork'),

]


