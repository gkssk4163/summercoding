from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.utils import timezone

from django.contrib.auth.models import User
from todo.models import List
from todo.forms import SignupForm, LoginForm, TodoForm

def main(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return redirect('todo_list')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('main')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            return HttpResponse("<script>alert('로그인 실패. 다시 시도해주세요.');history.back();</script>")
    else:
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})


@login_required(login_url='/')
def todo_list(request):
    if request.method == "POST":
        filter1 = request.POST.get('filter1')
        filter2 = request.POST.get('filter2')
        column = request.POST.get('column')
        sort = request.POST.get('sort')
        mode = request.POST.get('mode')
        checkOne = request.POST.getlist('checkOne')

        check_lists = List.objects.filter(user=request.user, pk__in=checkOne)
        if mode == "complete":
            for check_list in check_lists:
                check_list.complete()
        elif mode == "delete":
            for check_list in check_lists:
                check_list.delete()

        response = redirect('todo_list')
        response['Location'] += '?filter1='+filter1+'&filter2='+filter2+'&column='+column+'&sort='+sort
        return response
    else:
        column = request.GET.get('column', 'pk')  #번호(등록순서),우선순위,마감기한
        sort = request.GET.get('sort', '')  #asc,desc
        today = timezone.now()
        filter1 = request.GET.get('filter1', 'all')
        filter2 = request.GET.get('filter2', 'all')
        
        lists = List.objects.filter(user=request.user)

        if filter1 == 'completed':
            lists = lists.filter(completed_date__isnull=False)
        elif filter1 == 'incompleted':
            lists = lists.filter(completed_date__isnull=True)

        if filter2 == 'none':
            lists = lists.filter(deadline__isnull=True)
        elif filter2 == 'before':
            lists = lists.filter(deadline__gte=today)
        elif filter2 == 'after':
            lists = lists.filter(deadline__lt=today)

        lists = lists.order_by(sort+column)

        incompleted_in_deadline_count = List.objects.filter(user=request.user, deadline__lt=today,
                                        completed_date__isnull=True).count()

        return render(request, 'todo/list.html', {
            'menu': 'list', 'lists': lists, 'incompleted_count': incompleted_in_deadline_count,
            'filter1': filter1, 'filter2': filter2,
            'column': column, 'sort': sort
        })

@login_required(login_url='/')
def todo_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo_view', todo.pk)
    else:
        form = TodoForm()
    return render(request, 'todo/edit.html', {'menu': 'list', 'form': form})

@login_required(login_url='/')
def todo_edit(request, pk):
    todo = List.objects.get(user=request.user, pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_view', todo.pk)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/edit.html', {'menu': 'list', 'form': form, 'pk': pk})

@login_required(login_url='/')
def todo_view(request, pk):
    todo = get_object_or_404(List, user=request.user, pk=pk)
    return render(request, 'todo/view.html', {'menu': 'list', 'todo': todo, 'pk': pk})

@login_required(login_url='/')
def todo_delete(request, pk):
    todo = List.objects.get(user=request.user, pk=pk)
    todo.delete()
    return redirect('todo_list')

@login_required(login_url='/')
def todo_complete(request, pk):
    todo = List.objects.get(user=request.user, pk=pk)
    todo.complete()
    return redirect('todo_view', todo.pk)

@login_required(login_url='/')
def undo_complete(request, pk):
    todo = List.objects.get(user=request.user, pk=pk)
    todo.undo_complete()
    return redirect('todo_view', todo.pk)
