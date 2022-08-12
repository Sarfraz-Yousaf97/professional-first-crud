from django.shortcuts import get_object_or_404, redirect, render
from django.urls import is_valid_path
from django.views import View

from blog.forms import CreateForm
from .models import User


# Create your views here.

class LandingPageView(View):
    def get(self,request):
        blog_list = User.objects.order_by('-created_on')[0:3]
        blog_all = User.objects.all()
        title = 'Landing'
        context = {
            'blog_list':blog_list,
            'title':title,
            'blog_all':blog_all
            
        } 
        return render(request, 'landing.html',context)


class DetailView(View):
    def get(self,request, *args, **kwargs):
        id = kwargs.get('id')
        blog_detail = get_object_or_404(User, id= id)
        context = {
            "blog_detail":blog_detail
        }
        return render(request, 'detail_view.html', context)


class CreateBlogView(View):
    def get(self,request):
        create_form = CreateForm()
        context = {
            'form':create_form
        }
        return render(request, 'create_blog.html' , context)


    def post(self,request):
        form = CreateForm(request.POST,request.FILES)

        if form.is_valid():
            obj = form.save(commit=False)
            thumbnail = request.FILES['thumbnail']
            second_thumbnail = request.FILES['seconed_thumbnail']
            profile=request.FILES['author_profile']
            obj.thumbnail = thumbnail
            obj.seconed_thumbnail = second_thumbnail
            obj.author_profile = profile
            obj.save()
            return redirect('landing')
            
        else:
            print(request.POST)
            return redirect('create_blog')



class UpdatePageView(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get('id')
        object = get_object_or_404(User,id=id)
        update_form = CreateForm(instance=object)
        context = {
            'update_object':object,
            'update_form':update_form 
        }
        return render(request, 'update_view.html' , context)

    def post(self,request,*args,**kwargs):
        id = kwargs.get('id')
        update_id=get_object_or_404(User,id=id)
        update_form = CreateForm(request.POST or None,instance=update_id)
        if update_form.is_valid():
            obj = update_form.save(commit=False)


            if 'thumbnail' in request.FILES:
               thumbnail = request.FILES['thumbnail']
               obj.thumbnail = thumbnail
            if 'seconed_thumbnail' in request.FILES:
               second_thumbnail = request.FILES['seconed_thumbnail']
               obj.seconed_thumbnail = second_thumbnail
            if 'author_profile' in request.FILES:

               profile=request.FILES['author_profile']
               obj.author_profile = profile
            obj.save()
            return redirect('landing')
            
        else:
            print(request.POST)
            return redirect('update_view',id=id)
