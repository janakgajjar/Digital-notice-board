from django.shortcuts import render
from django.utils import timezone
from .models import Notice
from django.db.models import Q


def notice_board(request):
    notices = Notice.objects.all()
    today = timezone.now().date()
    notices = Notice.objects.filter(
        is_active=True,
        expiry_date__gte=today
    ).order_by('-created_at')

    context = {
        'notices': notices,
        'page_title': 'All Notices'
    }
    return render(request, 'index.html', context)

def department_notice_view(request, department, semester):
    if semester == 'all':
        filtered_notices = Notice.objects.filter(Q(department=department) | Q(is_common=True)).distinct().order_by('-expiry_date')
        title = f"Department :{department}"
    else:
        filtered_notices = Notice.objects.filter(
            Q(department=department,semester=semester) | Q(is_common=True)).distinct().order_by('-expiry_date')
        title = f"Department :{department} ({semester})"

    context = {
        'notices' : filtered_notices,
        'current-department' : department,
        'current_semester' : semester,
        'page_title' : title
    }

    return render(request, 'index.html', context)