from django.urls import path
from . import views 
from .views import PostDetailView,PostListView,PostCreateView


urlpatterns = [
	path('',PostListView.as_view(),name='home'),
	path('<int:pk>/',PostDetailView.as_view(),name='viewpost'),
	path('createpost/',PostCreateView.as_view(),name='createpost'),
	path('signup/',views.signup,name='signup'),
	path('login/',views.login,name='login'),
	
    
]



'''















urlpatterns = [
	path('',views.home,name='home'),
	path('<int:pk>/',PostDetailView.as_view(),name='viewpost'),
	path('addblog/',views.addblog,name='addblog'),
	path('signup/',views.signup,name='signup'),
	path('login/',views.login,name='login'),
	
    
]

'''