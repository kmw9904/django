import re
from django import views
from django.shortcuts import render, redirect

import articles
from .models import Article


# Create your views here.
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    # pk를 통해서 하나의 게시글을 조회하고
    article = Article.objects.get(pk=pk)
    # context에 해당 게시글 내용을 포함하여
    context = {
        'article': article,
    }
    # 상세 페이지를 렌더링
    return render(request, 'articles/detail.html', context)


# def new(request):
#     return render(request, 'articles/new.html')

def create(request):
    if request.method == 'GET':
        return render(request, 'articles/new.html')
    elif request.method == 'POST':
        # 사용자로 부터 전달 받은 제목과 내용 정보를 가지고
        # HTTP body 에 데이터가 담겨져 있다. -> request.POST
        title = request.POST.get('title')
        content = request.POST.get('content')
        # 새로운 게시글을 생성한다!
        # 1. 인스턴스를 생성한 후에 저장
        # article = Article()
        # # 인스턴스 변수에 제목과 내용을 할당
        # article.title = title
        # article.content = content
        # article.save()

        # 2. 인스턴스 초기화하 함께 생성하고 저장
        article = Article(title=title, content=content)
        article.save()
        # 3. 바로 queryset API 사용하여 저장
        # Article.objects.create(title=title, content=content)
        # 요청을 보낸 사용자에게는 해당 페이지로 이동 요청을 보낸다!
        # 리다이렉트 : 요청을 보낸 사용자를 다른 URL으로 보내기 위한 응답
    #  A 주소 요청 -> 응답(B 주소 가세요 = 리다이렉트) -> B 주소 이동
    return redirect('articles:detail', article.pk)

# View 클래스로 유지하도록 장고는 권장하고 있음
class UpdateView(views.View):
    # "GET" HTTP 메소드 요청
    def get(self, request, pk):
        pass

    # "POST"
    def post(self, request, pk):
        pass
    
# View 함수 (Functional Based View FBV)
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == "GET":
        # "GET"
        # 해당 게시글의 수정 페이지를 보여주도록

        # 컨텍스트에 실어서 수정 페이지를 렌더링
        context = {
            'article': article,
        }

        return render(request, 'articles/edit.html', context)
    elif request.method == "POST":
        # POST
        title = request.POST.get("title")
        content = request.POST.get("content")
        # 해당 게시글의 수정 작업을 진행
        # 해당 게시글을 조회하여

        # 그 글의 내용과 제목을 수정
        article.title = title
        article.content = content
        article.save()

        return redirect('articles:detail', article.pk)


def delete(request, pk):
    if request.method == "POST":
        # "POST"로 요청했을 떄에만 동작!
        # 해당 pk를 가지고 있는 게시글을 삭제한다
        article = Article.objects.get(pk=pk)
        article.delete()  # DB에서 해당 레코드 삭제
        # HTTP 응답 (게시글 전체 조회)
        return redirect('articles:index')
