from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.views.generic import DetailView, UpdateView, DeleteView, ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm, UserProfileUpdateForm
from .models import PostForBooks, PostForMovies, Profile, Feedback
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
import logging

logger = logging.getLogger('django')

# Create your views here.


def base(requset):
    postM = PostForMovies.objects.order_by('-pub_date')[:2]
    postB = PostForBooks.objects.order_by('-pub_date')[:2]
    context = {
        'latest_post_movies': postM,
        'latest_post_books': postB,
    }

    return render(requset, 'home.html', context)


@require_http_methods(['POST'])
def feedback(request):
    if request.method == 'POST':
        try:
            userFeed = request.POST.get('feedbackUsername')
            emailFeed = request.POST.get('feedbackEmail')
            textFeed = request.POST.get('feedbackMessage')
            new_feedback = Feedback(name=userFeed, email=emailFeed, message=textFeed)
            logger.info("feedback() - saving feedback from {}".format(userFeed))
            new_feedback.save()

        except Exception as exc:
            print('Error: ', exc)
            logger.error("feedback() - error occurred: {}".format(exc))
            return HttpResponse(status=500)

        return HttpResponse(status=200)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, your account has been created. Now you are able to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

@login_required
def profile(request):
    Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileUpdateForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been updated')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileUpdateForm(instance=request.user.profile)

    content = {
        'UserUpdateForm': u_form,
        'UserProfileUpdateForm': p_form,
    }

    return render(request, 'user/profile.html', content)


class PostsOfBooksView(ListView):
    model = PostForBooks
    context_object_name = 'post'
    template_name = 'post/postsOfbooks.html'
    ordering = ['-pub_date']
    paginate_by = 3


class PostDetailViewBooks(DetailView):

    def get(self, request, *args, **kwargs):
        books = get_object_or_404(PostForBooks, pk=kwargs['pk'])
        comment_books = books.commentforbook_set.all()

        context = {'object': books,
                   'comment_books': comment_books}

        return render(request, 'post/post_detail_books.html', context)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['Coments'] = PostForMovies.philosophy


class PostCreateViewBooks(LoginRequiredMixin, CreateView):
    model = PostForBooks
    fields = ['title', 'content']
    template_name = 'post/post_create_books.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateViewBooks(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PostForBooks
    fields = ['title', 'content']
    template_name = 'post/post_create_books.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteViewBooks(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostForBooks
    template_name = 'post/post_confirm_delete_books.html'
    success_url = 'postsOfBooks'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class UserPostsOfMoviesView(ListView):
    model = PostForMovies
    context_object_name = 'post'
    template_name = 'post/user_postsOfmovies.html'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return PostForMovies.objects.filter(author=user).order_by('-pub_date')


class UserPostsOfBooksView(ListView):
    model = PostForBooks
    context_object_name = 'post'
    template_name = 'post/user_postsOfbooks.html'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return PostForBooks.objects.filter(author=user).order_by('-pub_date')


class PostsOfMoviesView(ListView):
    model = PostForMovies
    context_object_name = 'post'
    template_name = 'post/postsOfmovies.html'
    ordering = ['-pub_date']
    paginate_by = 3


class PostDetailViewMovies(DetailView):

    def get(self, request, *args, **kwargs):
        movies = get_object_or_404(PostForMovies, pk=kwargs['pk'])
        comment_movies = movies.commentformovie_set.all()

        context = {'object': movies,
                   'comment_movies': comment_movies}

        return render(request, 'post/post_detail_movies.html', context)


class PostCreateViewMovies(LoginRequiredMixin, CreateView):
    model = PostForMovies
    fields = ['title', 'content']
    template_name = 'post/post_create_movies.html'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateViewMovies(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PostForBooks
    fields = ['title', 'content']
    template_name = 'post/post_create_books.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteViewMovies(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PostForMovies
    template_name = 'post/post_confirm_delete_movies.html'
    success_url = 'postsOfMovies'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def add_comment_movies(request, id):
    comment = get_object_or_404(PostForMovies, pk=id)
    comment.commentformovie_set.create(author=request.POST['comment_auth_mov'], text=request.POST['comment_text_mov'])

    return HttpResponseRedirect(reverse('detail_movies', args=(id,)))


def add_comment_books(request, id):
    comment = get_object_or_404(PostForBooks, pk=id)
    comment.commentforbook_set.create(author=request.POST['comment_auth_book'], text=request.POST['comment_text_book'])

    return HttpResponseRedirect(reverse('detail_books', args=(id,)))
