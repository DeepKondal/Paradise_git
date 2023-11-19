from django.shortcuts import render
from .models import Category,Product
from django.shortcuts import get_object_or_404
import random
from . import ml_predict
# Create your views here.

def store(request):

    all_products =Product.objects.all()
    shuffled_products = random.sample(list(all_products),len(all_products))
    
    context = {'my_products': shuffled_products}
    return render(request,'store/store.html',context=context)

def all(request):

    all_products =Product.objects.all()
    context = {'my_products': all_products}
    return render(request,'store/all.html',context=context)

def categories(request):
    all_categories = Category.objects.all()

    return {'all_categories': all_categories}

def product_info(request,product_slug):
    product = get_object_or_404(Product,slug=product_slug)
    context = {'product': product}
    return render(request, 'store/product-info.html',context=context)


def list_category(request,category_slug=None):
    category = get_object_or_404(Category,slug=category_slug)
    products = Product.objects.filter(category=category)

    return render(request, 'store/list-category.html',{'category': category,'products':products})

def reccommend(request):
    pclass = int(request.GET['pclass'])
    sex = int(request.GET['sex'])
    age = int(request.GET['age'])
    sibsp = int(request.GET['sibsp'])
    parch = int(request.GET['parch'])
    fare = int(request.GET['fare'])
    embarked = int(request.GET['embarked'])
    title = int(request.GET['title'])

    reccomendations = ml_predict.prediction_model(pclass,sex,age,sibsp,parch,fare,embarked,title)
    context = {'reccomendations':reccomendations}
    return render(request,'store/reccomendations.html', context=context)