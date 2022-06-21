from django.urls import path
from .views import *

urlpatterns = [
    path('', index,name='home'),
    path('show/<int:file_id>/', show,name='show'),
    #path('show/<str:filePATH>/', show),
    path('upload/', upload,name='upload'),
    path('download/<str:path>/',download,name='download'),
    path('change_file/<int:file_id>/',change_file,name='change_file'),
]