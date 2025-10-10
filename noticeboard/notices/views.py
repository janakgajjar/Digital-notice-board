from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import notices
from .forms import NoticeForm  # We'll create this
from django.utils import timezone

def is_admin(user):
    return user.is_staff

# Login View (separate for user/admin based on credentials)
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST, request.FILES)
        if form.is_valid():
            notice = form.save(commit=False)
            notice.created_by = request.user
            notice.save()
            messages.success(request, 'Notice added with push pin animation!')
            return redirect('admin_dashboard')
    else:
        form = NoticeForm()
    notices = notices.objects.filter(created_by=request.user, is_active=True)
    return render(request, 'admin_dashboard.html', {'form': form, 'notices': notices})

@login_required
def user_dashboard(request):
    active_notices = notices.objects.filter(is_active=True, expiry_date__gte=timezone.now())
    return render(request, 'user_dashboard.html', {'notices': active_notices})
# Register new user (for regular users)
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})