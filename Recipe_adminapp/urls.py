from django.urls import path,include
from.import views


urlpatterns = [
   path('',views.adminindex, name='adminindex'),
   path('add/',views.add,name='add'),
   path('recipedata/',views.recipedata,name='recipedata'),
   path('messages/',views.messages,name='messages'),
   path('view_recipe/<int:id>/',views.view_recipe,name='view_recipe'),
   path('update/<int:id>/',views.update,name='update'),
   path('delete/<int:id>/',views.delete,name='delete'),
   path('viewcontact/',views.viewcontact,name='viewcontact'),
   path('users/',views.users,name='users')
   ]