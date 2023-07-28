from django.urls import path
from ptproject.views import Home, PersonalTrainer, Member, book_session, Register, Profile
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="index"),
    path('personaltrainer/', views.PersonalTrainer.as_view(),
         name='personaltrainer'),
    path("member/", views.Member.as_view(), name="member"),
    path("booking/", views.book_session, name="book_session"),
    path("register/", views.Register, name="register"),
    path("profile/", views.Profile, name="profile"),
    path('book/', views.Book.as_view(), name='book'),
]
