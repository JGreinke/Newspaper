from django.views.generic.edit import DetailView
from django.views.generic.edit import CreateView
from .models import Article

class ArticleDetailView(DetailView): 
    template_name = "articles/detail.html"
    model = Article

class ArticleCreateView(CreateView):
    template_name = "articles/create.html"
    model = Article
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 

# this is how to overwrite and auto-generate the author. The form will ask for title and body but will automatically create author. 