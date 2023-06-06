from django.urls import path
from.import views


urlpatterns = [
   path('userindex1/',views.userindex1, name='userindex1'),
   path('recipe_detail/<int:id>/',views.recipe_detail, name='recipe_detail'),
   path('usercontact/',views.usercontact, name='usercontact'),
   path('getData/',views.getData,name='getData'),
   path('userregister/',views.userregister,name='userregister'),
   path('registerdata/',views.registerdata,name='registerdata'),
   path('login/',views.login,name='login'),
   path('userlogin/',views.userlogin,name='userlogin'),
   path('logout/',views.logout,name='logout'),
   ]