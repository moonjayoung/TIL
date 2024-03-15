from django.shortcuts import render

# Create your views here.
# 메인 페이지를 만드는 index라는 이름의 함수를 작성
def index(request) :
    # 왜? - render 함수가 그렇게 만들어져 있음
    # render(요청 객체, 템플릿 경로)
    return render(request, 'index.html')