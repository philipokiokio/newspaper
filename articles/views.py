from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import Article
from django.views.generic import ListView,DetailView
from django.views.generic.edit import UpdateView, DeleteView,CreateView
from django.urls import reverse_lazy, reverse
from django.core.exceptions import PermissionDenied

# Create your views here.
class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'article_list.html'
    login_url = 'login'

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Article 
    template_name = 'article_detail.html'
    login_url = 'login'    

class ArticleEditView(LoginRequiredMixin,UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    # success_url = reverse_lazy('article_list')
    login_url = 'login'   

    def dispatch(self,request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request,*args,**kwargs) 





class ArticleDeleteView(LoginRequiredMixin,DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'    
    
    def dispatch(self,request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request,*args,**kwargs) 


class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_create.html'
    # success_url = reverse_lazy('article_list')
    login_url = 'login'
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)