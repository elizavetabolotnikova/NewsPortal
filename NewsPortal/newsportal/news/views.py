from django.shortcuts import render,redirect
from .models import Articles
from django.views.generic import DetailView,UpdateView,DeleteView
from .forms import ArticlesForm

def news_home(request):
    news=Articles.objects.order_by('-date')
    return render(request,'news/news_home.html', {'news' : news})
def create(request):
    error=''
    if request.method=='POST':
        form=ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error='Форма былап неверной'

    form=ArticlesForm()
    data={'form':form}
    return render(request, 'news/create.html',data)

class NewsDetailView(DetailView):
    model=Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    success_url = '/news/'
    fields=['title','first_words','text_feild','date']

class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/delete.html'

