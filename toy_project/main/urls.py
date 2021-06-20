from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('create/', views.create, name="create"),
    path('detail/<int:write_id>', views.detail, name="detail"),
    path('update/<int:write_id>', views.update, name="update"),
    path('delete/<int:write_id>', views.delete, name="delete"),
]
