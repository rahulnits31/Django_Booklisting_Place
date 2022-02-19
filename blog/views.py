from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
	model=Post
	template_name='blog/home.html'  #app/model_viewtype.html
	context_object_name='posts'

class DetailView(DetailView):
	model=Post
	


class DeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model=Post
	success_url='/'

	def test_func(self):
				post=self.get_object()
				if self.request.user==post.author:
					return True
				return False

class CreateView(LoginRequiredMixin,CreateView):
			model=Post
			success_url='/'
			fields=['bookname','description','category','image','price','Contact_no','Address']

			def form_valid(self, form):
				form.instance.author = self.request.user
				return super().form_valid(form)	

class UpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
			model=Post
			success_url='/'
			fields=['bookname','description','category','image','price','Contact_no','Address']

			def form_valid(self, form):
				form.instance.author = self.request.user
				return super().form_valid(form)	

			def test_func(self):
				post=self.get_object()
				if self.request.user==post.author:
					return True
				return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})



def search_Result(request):
    if request.method== 'POST':
        searh_query = request.POST['search']
        query_result = Post.objects.filter(bookname__startswith=searh_query)
        return render(request,'blog/search.html',{'query_result':query_result,'searh_query':searh_query})

def search_cat(request):
    if request.method== 'POST':
        searh_query = request.POST['searchcat']
        query_result = Post.objects.filter(category__startswith=searh_query)
        return render(request,'blog/search.html',{'query_result':query_result,'searh_query':searh_query})




@login_required
def mycontent(request):
    user = request.user
    user_posts = Post.objects.filter(author=request.user).order_by('date_posted')
   
    return render(request, 'blog/mycontent.html', {'user_posts':user_posts,'user': user})