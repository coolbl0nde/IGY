from django.urls import path
from . import views

app_name = 'pharmacy_app'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('medicines', views.MedicinesList, name = 'medicines'),
    path('medicines/<int:id>', views.medicines_detail, name = 'medicines_details'),
    path('<str:type>', views.MedicinesList,name='medicines_list_by_type'),
    path('register/', views.RegisterUser.as_view(), name = 'register'),
    path('logout/', views.logout_user, name = 'logout'),
    path('login/', views.LoginUser.as_view(), name = 'login'),
    path("create/", views.medicines_create, name='create'),
    path("medicines/edit/<int:id>/", views.medicines_edit),
    path("medicines/delete/<int:id>/", views.medicines_delete),

]