from django.urls import path
from django.contrib.auth import views
from .views import (base,
                    feedback,
                    register,
                    PostsOfBooksView,
                    PostsOfMoviesView,
                    profile,
                    PostDetailViewBooks,
                    PostDetailViewMovies,
                    PostCreateViewBooks,
                    PostCreateViewMovies,
                    PostUpdateViewBooks,
                    PostUpdateViewMovies,
                    PostDeleteViewBooks,
                    PostDeleteViewMovies,
                    UserPostsOfBooksView,
                    UserPostsOfMoviesView,
                    add_comment_books,
                    add_comment_movies)



urlpatterns = [
    path('', base, name='home'),
    path('feedback', feedback, name='feedback'),
    path('login/', views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('postsOfBooks/', PostsOfBooksView.as_view(), name='postsOfBooks'),
    path('postsOfMovies/', PostsOfMoviesView.as_view(), name='postsOfMovies'),
    path('postDetailBooks/<int:pk>/', PostDetailViewBooks.as_view(), name='detail_books'),
    path('postDetailMovies/<int:pk>/', PostDetailViewMovies.as_view(), name='detail_movies'),
    path('newPost/books/', PostCreateViewBooks.as_view(), name='create_books'),
    path('newPost/movies/', PostCreateViewMovies.as_view(), name='create_movies'),
    path('postsOfBooks/<str:username>/', UserPostsOfBooksView.as_view(), name='user_posts_books'),
    path('postsOfMovies/<str:username>/', UserPostsOfMoviesView.as_view(), name='user_posts_movies'),
    path('postDetailBooks/<int:pk>/update/', PostUpdateViewBooks.as_view(), name='update_books'),
    path('postDetailMovies/<int:pk>/update/', PostUpdateViewMovies.as_view(), name='update_movies'),
    path('postDetailBooks/<int:pk>/delete/', PostDeleteViewBooks.as_view(), name='delete_books'),
    path('postDetailMovies/<int:pk>/delete/', PostDeleteViewMovies.as_view(), name='delete_movies'),
    path('comment/book/<int:id>/', add_comment_books, name='comment_books'),
    path('comment/movie/<int:id>/', add_comment_movies, name='comment_movies'),
]

