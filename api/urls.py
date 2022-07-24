from django.urls import path
from . import views
urlpatterns = [
    path('list/',views.StudentList.as_view(),name="StudentList"),
    path('list/<int:pk>',views.StudentRetrieve.as_view(),name=""),
    path('create/',views.StudentCreate.as_view(),name="Studentcreate"),
    path('update/<int:pk>',views.StudentUpdate.as_view(),name="StudentUpdate"),
    path('delete/<int:id>',views.StudentDelete.as_view(),name="StudentDelete"),
]
