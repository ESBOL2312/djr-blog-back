from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from blog.models import article, category
from blog.serializers import BlogSerializer, BlogCategorySerializer

# Create your views here.

@csrf_exempt
def article_list(request):
    if request.method == 'GET':
        snippets = article.objects.all()
        fields = ['id','title', 'authorFn']
        serializer = BlogSerializer(snippets, many=True,fields = fields)
        data =  {
            "articles":serializer.data
            }
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
@csrf_exempt
def article_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        blog = article.objects.get(pk=pk)
    except article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BlogSerializer(blog, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        blog.delete()
        return HttpResponse(status=204)
def category_list(request):
    if request.method == 'GET':
        categories = category.objects.all()
        serializer = BlogCategorySerializer(categories, many=True)
        data =  {
            "categories":serializer.data
            }
        return JsonResponse(data, safe=False)

def category_articles(request, pk):
    try:
        articles = article.objects.filter(category=pk)
    except articles.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        fields = ['id','title', 'authorFn']
        serializer = BlogSerializer(articles, many=True,fields = fields)
        data =  {
            "articles":serializer.data
            }
        return JsonResponse(data, safe=False)