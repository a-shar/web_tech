from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST

from qa.forms import AskForm, AnswerForm
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
    answer_form = AnswerForm(initial={'question': qid, 'author': User.objects.get(pk=1)})
    return render(request, 'ask/question.html', {
        'question': question,
        'answers': answers,
        "form": answer_form,
    })


def question_list(request, order_by, page_name, base_url):
    questions = Question.objects.order_by(order_by)
    paginator, page = paginate(request, questions)
    paginator.baseurl = base_url
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
    return paginator, page


def ask(request, *args, **kwargs):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()

    return render(request, 'ask/ask.html', {
        'form': form
    })

@require_POST
def answer(request, *args, **kwargs):
    form = AnswerForm(request.POST)
    if form.is_valid():
        answer = form.save()
        url = answer.question.get_url()
        return HttpResponseRedirect(url)

    q = get_object_or_404(Question, id=form['question'].data)
    return HttpResponseRedirect(q.get_url())