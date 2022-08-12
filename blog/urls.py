from django.urls import path
from .views import CreateBlogView, DetailView, LandingPageView, UpdatePageView



urlpatterns = [
    path('',LandingPageView.as_view(),name='landing'),
    path('detail_view/<int:id>/',DetailView.as_view(),name='detail_view'),
    path('create_blog',CreateBlogView.as_view(), name='create_blog'),
    path('update_view/<int:id>/',UpdatePageView.as_view(),name='update_view'),

]