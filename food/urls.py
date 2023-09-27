from . import views
from django.urls import path


urlpatterns =[
    path('', views.IndexClassView.as_view(), name='index'),
    path('item', views.item, name='item'),
    path('<int:pk>', views.Fooddetail.as_view(), name='detail'),
    #add
    path('add', views.CreateItem.as_view(), name='create_item2'),
    #edit
    path('update/<int:id>', views.update_item, name='update_name'),
    #delete
    path('delete/<int:id>', views.delete_item, name='delete_item')
]
   

