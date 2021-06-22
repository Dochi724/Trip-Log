from django.urls import path
from . import views
from django.conf.urls import include

app_name = 'main'

urlpatterns = [
    path('create/', views.create, name="create"),
    path('', views.index, name="index"),
    path('detail/<int:write_id>', views.detail, name="detail"),
    path('update/<int:write_id>', views.update, name="update"),
    path('delete/<int:write_id>', views.delete, name="delete"),
    path('create_comment/<int:write_id>', views.create_comment, name='create_comment'),
    path('delete_comment/<int:write_id>/<int:comment_id>', views.delete_comment, name='delete_comment'),
    path('map/<int:write_id>', views.map, name="map"),
    path('page/<int:write_id>', views.page, name="page"),

]
