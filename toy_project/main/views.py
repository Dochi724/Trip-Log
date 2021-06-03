from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    # all_write 변수에 내용 담아서 보내기
    return render(request, 'index.html')