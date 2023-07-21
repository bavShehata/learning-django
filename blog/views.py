from django.shortcuts import render
# Create your views here.

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'July 12, 2020'
    },
    {
        'author': 'BavlyS',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'July 25, 2020'
    },
]
def home(request):
    context = {
        'posts': posts,
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
