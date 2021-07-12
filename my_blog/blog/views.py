from django.shortcuts import render

# Create your views here.


def starting_page(request):
    '''Function for the starting page'''
    return render(request, "index.html")

def posts(request):
    '''Required for the post routes/URLs'''
    pass

def post_detail(request):
    '''
    Function for the individual post. It should be trigger by our last path in urls.py
    '''
    pass

