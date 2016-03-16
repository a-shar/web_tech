from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404

from qa.models import Question, Answer


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def main_page(request, *args, **kwargs):
    return question_list(request, '-added_at', 'main.html', '/?page=')


def popular_page(request, *args, **kwargs):
    return question_list(request, '-rating', 'popular.html', '/popular/?page=')


def question_detail(request, qid):
    question = get_object_or_404(Question, id=qid)
    answers = Answer.objects.filter(question=question)
    return render(request, 'ask/question.html', {
        'question': question,
        'answers': answers,
    })


def question_list(request, order_by, page_name, base_url):
    questions = Question.objects.order_by(order_by)
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = base_url
    page = paginator.page(page)  # Page
    return render(request, 'ask/' + page_name, {
        'asks': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
        if limit > 100:
            limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404

    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page
