from django.urls import path
from .views import WebtoonListView, WebtoonCreateView, WebtoonDetailView, WebtoonDeleteView

urlpatterns = [
    path('webtoons/', WebtoonListView.as_view(), name='webtoon_list'),
    path('webtoons/create/', WebtoonCreateView.as_view(), name='webtoon_create'),
    path('webtoons/<int:id>/', WebtoonDetailView.as_view(), name='webtoon_detail'),
    path('webtoons/delete/<int:id>/', WebtoonDeleteView.as_view(), name='webtoon_delete'),
]
