from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='display_files'),
    path('upload_image/', views.uploadView, name= 'upload_image'),
    path('edit/<int:id>',views.editView,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.destroy,name='delete'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('signup/',views.register,name='register'),
]