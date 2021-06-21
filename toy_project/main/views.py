from django.shortcuts import render, redirect, get_object_or_404
from .forms import WriteForm, CommentForm
from .models import Write, Comment
from django.contrib.auth.models import User


# Create your views here.


def index(request):
    # all_write 변수에 내용 담아서 보내기
    all_write = Write.objects.all()
    return render(request, 'index.html', {'all_write': all_write})


def create(request):
    if request.method == "POST":
        create_form = WriteForm(request.POST,request.FILES)
        if create_form.is_valid():
            create_form.save()
            return redirect('index')
    write_form = WriteForm
    return render(request, 'create.html', {'write_form': write_form})


def detail(request, write_id):
    user = request.user
    my_write = get_object_or_404(Write, pk=write_id)
    comment_form = CommentForm()
    comments = Comment.objects.filter(post = write_id)
    return render(request, 'detail.html', {'my_write': my_write, 'comment_form': comment_form, 'comments':comments, 'user':user})


def update(request, write_id):
    my_write = get_object_or_404(Write, id=write_id)
    if request.method == "POST":
        update_form = WriteForm(request.POST,request.FILES,instance=my_write)
        if update_form.is_valid():
            update_form.save()
            return redirect('index')
    update_form = WriteForm(instance=my_write)
    return render(request, 'update.html', {'update_form': update_form})


def delete(request, write_id):
    my_write = get_object_or_404(Write, id=write_id)
    my_write.delete()
    return redirect('index')

def create_comment(request, write_id):
    if request.method == "POST":
        comment = CommentForm(request.POST) #POST 요청으로 넘어온 데이터를 CommentForm 양식에 넣고 comment 변수에 담기
        if comment.is_valid: #해당 폼이 유효한 경우 저장하고 detail.html로 돌아가기
            form = comment.save(commit=False)
            user = request.user
            form.user = User.objects.get(id=user.id) #user 필드에 값 추가
            form.post = Write.objects.get(id=write_id) #post 필드에 값 추가
            form.save()
        return redirect("main:detail", write_id)

def delete_comment(request, write_id, comment_id):
    my_comment = get_object_or_404(Comment, id=comment_id)
    my_comment.delete()
    return  redirect("main:detail", write_id)