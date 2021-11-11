from .models import Books
from django.views.generic import ListView

class PostListView(ListView):
        model=Books
        paginate_by =2
        ordering = ['id']