from datetime import date

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from posts.models import Post
from report_post.forms import FormReportPost
from report_post.models import Report


@login_required
def report_post(request, post_id):
    if get_current_user(request).is_superuser:
        if request.method == 'POST':
            form = FormReportPost(request.POST)
            if form.is_valid():
                post = Post.objects.get(id=post_id)
                if Report.objects.filter(post_id=post.id).exists():
                    report = Report.objects.filter(post_id__exact=post.id)[:1]
                    report_current = Report.objects.get(id=report[0].id)
                    report_current.amount += 1
                    report_current.save()
                    dados = form.cleaned_data
                    comment = dados['comment']
                    currrent_date = date.today()
                    messages.success(request, 'Reportado com sucesso.')
                    Report(post=post, comment=comment, date_report=currrent_date, amount=0).save()
                    return redirect('index')
                else:
                    dados = form.cleaned_data
                    comment = dados['comment']
                    currrent_date = date.today()
                    messages.success(request, 'Reportado com sucesso.')
                    Report(post=post, comment=comment, date_report=currrent_date, amount=1).save()
                    return redirect('index')

        elif request.method == 'GET':
            post = Post.objects.get(id=post_id)
            return render(request, 'report_post.html', {'current_user': get_current_user(request), 'post': post})
    else:
        return render(request, 'access_denied.html', {'current_user': get_current_user(request)})


def get_current_user(request):
    return request.user


@login_required
def show_reports(request):
    if get_current_user(request).is_superuser:
        reports = Report.objects.exclude(amount=0).order_by('-id')
        paginador = Paginator(reports, 10)
        page = request.GET.get('page')
        reports = paginador.get_page(page)
        return render(request, 'show_reports.html', {'current_user': get_current_user(request), 'reports': reports})
    else:
        return render(request, 'access_denied.html', {'current_user': get_current_user(request)})


@login_required
def delete_report(request, report_id):
    if get_current_user(request).is_superuser:
        report = Report.objects.get(id=report_id)
        all_reports = Report.objects.filter(post_id=report.post)
        for report_current in all_reports:
            Report.objects.get(id=report_current.id).delete()
        messages.success(request, 'Report deletado!.')
        return redirect('show_reports')
    else:
        return render(request, 'access_denied.html', {'current_user': get_current_user(request)})


@login_required
def delete_post_reported(request, post_id):
    if get_current_user(request).is_superuser:
        post = Post.objects.get(id=post_id)
        post.delete()
        messages.success(request, 'Deletado com sucesso.')
        return redirect('show_reports')
    else:
        return render(request, 'access_denied.html', {'current_user': get_current_user(request)})


@login_required
def show_comments_report(request, report_id):
    if get_current_user(request).is_superuser:
        report = Report.objects.get(id=report_id)
        reports_comments = Report.objects.filter(post_id=report.post.id)
        paginador = Paginator(reports_comments, 10)
        page = request.GET.get('page')
        reports_comments = paginador.get_page(page)
        return render(request, 'show_comments_report.html',
                      {'current_user': get_current_user(request), 'reports': reports_comments})
    else:
        return render(request, 'access_denied.html', {'current_user': get_current_user(request)})
