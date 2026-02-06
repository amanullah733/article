from django.shortcuts import render

# Create your views here.
article_data = [
    {
        'id':1,
        'title': 'This is all about India',
        'desc': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Rem dolor excepturi qui quidem eligendi quaerat ullam, et quam sit molestias cum impedit suscipit facilis! Et illo, laudantium distinctio minus dolore pariatur veniam dolores voluptate aspernatur! Nulla perferendis modi saepe animi aliquam, at neque qui aperiam, illum iste laboriosam aspernatur sit!'
    },
    {
        'id':2,
        'title': 'This is all about China',
        'desc': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Rem dolor excepturi qui quidem eligendi quaerat ullam, et quam sit molestias cum impedit suscipit facilis! Et illo, laudantium distinctio minus dolore pariatur veniam dolores voluptate aspernatur! Nulla perferendis modi saepe animi aliquam, at neque qui aperiam, illum iste laboriosam aspernatur sit!'
    },
    {
        'id':3,
        'title': 'This is all about USA',
        'desc': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Rem dolor excepturi qui quidem eligendi quaerat ullam, et quam sit molestias cum impedit suscipit facilis! Et illo, laudantium distinctio minus dolore pariatur veniam dolores voluptate aspernatur! Nulla perferendis modi saepe animi aliquam, at neque qui aperiam, illum iste laboriosam aspernatur sit!'
    },
    {
        'id':4,
        'title': 'This is all about KARnataka',
        'desc': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Rem dolor excepturi qui quidem eligendi quaerat ullam, et quam sit molestias cum impedit suscipit facilis! Et illo, laudantium distinctio minus dolore pariatur veniam dolores voluptate aspernatur! Nulla perferendis modi saepe animi aliquam, at neque qui aperiam, illum iste laboriosam aspernatur sit!'
    },
    {
        'id':5,
        'title': 'This is all about goa',
        'desc': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Rem dolor excepturi qui quidem eligendi quaerat ullam, et quam sit molestias cum impedit suscipit facilis! Et illo, laudantium distinctio minus dolore pariatur veniam dolores voluptate aspernatur! Nulla perferendis modi saepe animi aliquam, at neque qui aperiam, illum iste laboriosam aspernatur sit!'
    },
    {
        'id':6,
        'title': 'This is all about Dubai',
        'desc': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Rem dolor excepturi qui quidem eligendi quaerat ullam, et quam sit molestias cum impedit suscipit facilis! Et illo, laudantium distinctio minus dolore pariatur veniam dolores voluptate aspernatur! Nulla perferendis modi saepe animi aliquam, at neque qui aperiam, illum iste laboriosam aspernatur sit!'
    },
]


def home(request):
    context = {'data_key':article_data}
    return render(request,'home.html',context)

def news(request):
    return render(request,'news.html')

def events(request):
    return render(request,'events.html')

def about(request):
    return render(request,'about.html')

def read(request,pk):
    for i in article_data:
        if i['id']==pk:
            context={'data':i}
    return render(request,'read.html',context)