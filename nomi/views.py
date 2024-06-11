from django.shortcuts import render

def index_view(requst):
    return render(request=requst, template_name='index.html')

def about_view(requst):
    return render(request=requst, template_name='about.html')

def category_view(requst):
    return render(request=requst, template_name='category.html')

def work_view(requst):
    return render(request=requst, template_name='work.html')


