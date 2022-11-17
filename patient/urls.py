from django.urls import path
from .import views

urlpatterns = [
    path('create',views.load_create,name="create"),
    path('delete/<int:pk>',views.del_entry,name='del_entry'),
    path('<int:pk>',views.update_entry,name='update_entry'),
    path('display',views.load_data,name='display_data')
]