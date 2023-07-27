from django.urls import path
from ptproject.views import Home, pt, Member, book_session
from . import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path("pt/", views.pt.as_view(), name="pt"),
    path("member/", views.Member.as_view(), name="member"),
    path("booking/", views.book_session, name="book_session"),
]
