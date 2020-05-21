from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import Ad,Rubric,Comment,Wish
from .forms import EmailPostForm,CommentForm,AdForm,WishForm

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views import generic

def index(request):
    ads = Ad.objects.all()
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    rubrics = Rubric.objects.all()
    context={'ads':ads,'rubrics':rubrics,'num_visits':num_visits}
    return render(request,'bboard/index.html',context)

def ad_share(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ad_url = request.build_absolute_uri(ad.get_absolute_url())
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], ad.title)
            message = 'Read "{}" at {}\n\n{}\'s comments: {}'.format(ad.title, ad_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'admin@myblog.com',[cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'bboard/share.html', {'ad': ad,
                                                    'form': form,
                                                    'sent': sent})

def ad_detail(request, pk):
    ad = get_object_or_404(Ad, pk=pk)
    comments = ad.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.ad = ad
            new_comment.author = request.user
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'bboard/ad_detail.html', {'ad': ad,'comments': comments,
'new_comment': new_comment, 'comment_form': comment_form})

def by_rubric(request,rubric_id):
    ads = Ad.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    context={'ads':ads,'rubrics':rubrics,'current_rubric':current_rubric}
    return render(request,'bboard/by_rubric.html',context)

def ad_create(request):
    if request.method == "POST":
        form = AdForm(request.POST,request.FILES)
        if form.is_valid():
            ad = form.save(commit=False)
            ad.author = request.user
            ad.save()
    else:
        form = AdForm()
    return render(request, 'bboard/create.html', {'form': form})

def wish(request):
    wish = Wish.objects.all()
    return render(request, "bboard/wish.html", {"wish": wish})

def create(request):
    if request.method == "POST":
        wish = Wish()
        wish.author = request.user
        wish.body = request.POST.get("body")
        wish.number = request.POST.get("number")
        wish.save()
    return HttpResponseRedirect("/bboard/wish/")
