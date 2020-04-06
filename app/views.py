from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth 
from .models import Post
#for class based view **Very Important
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import PostForm
#to use the url name
from django.urls import reverse_lazy
#so that only the user logged in can make changes
from django.contrib.auth.mixins import UserPassesTestMixin

def home(request):
		return render(request,'app/home.html',{'post':Post.objects.all()})

'''
def addblog(request):
	if request.method == 'POST':
		form = PostForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = PostForm()
	return render(request,'app/addblog.html',{'form':form})

'''

class PostListView(ListView):
	model = Post
	# page djago looking for now has syntax app/model_viewtype.html
	# in this case app/post_list.html
	template_name = 'app/home.html'
	# to show model stuff on page
	context_object_name = 'post' 

class PostDeleteView(UserPassesTestMixin,DeleteView):
	model = Post
	# page djago looking for now has syntax app/model_viewtype.html
	# in this case app/post_list.html
	template_name = 'app/deletepost.html'
	# to show model stuff on page
	#context_object_name = 'post'
	success_url = reverse_lazy('home') 

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False 


#This is class based way of doint the view details thing
class PostDetailView(DetailView):
	model = Post
	template_name = 'app/viewpost.html'


class PostCreateView(CreateView):
	form_class = PostForm
	#template_name = 'app/createpost.html'
	#fields = ['title','content','pic']
	template_name = 'app/post_form.html'
	success_url = reverse_lazy('home')

	#validating form form without mentioning the author
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin,UpdateView):
	model = Post
	form_class = PostForm
	#template_name = 'app/createpost.html'
	#fields = ['title','content','pic']
	#template_name = 'app/post_form.html'
	success_url = reverse_lazy('home')

	#validating form form without mentioning the author
	def form_valid(self,form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	#method to make sure the user is looged in to make amends
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False 



#This is function way of doing the view post thing
def viewpost(request,post_id):
	post = get_object_or_404(Post,pk=post_id)
	return render(request,'app/viewpost.html',{'post':post})





































# NOT NEEDED FOR NOW



def signup(request):
	if request.method == 'POST':
		if request.POST['password1'] == request.POST['password2']:
			try:
				user = User.objects.get(username=request.POST['username'])
				return render(request,'app/signup.html',{'error': 'Username already exists!'})
			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'],request.POST['email'],password = request.POST['password1'])
				auth.login(request,user)
				return redirect('home')
		else:
			return render(request,'app/signup.html',{'error': 'Password must match!'})

	else:
		return render(request,'app/signup.html')

def login(request):
	return render(request,'app/login.html')

# Create your views here.
