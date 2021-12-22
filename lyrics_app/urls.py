from django.urls import path, include
from lyrics_app import APIviews, views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'lyrics_app'

urlpatterns = [
    path('api/lyrics/', APIviews.LyricsList.as_view()),
    path('api/lyrics/<int:pk>/', APIviews.LyricsDetail.as_view()),
    path('api/lyrics/search/<str:q>/', APIviews.LyricsSearchView.as_view()),


    path('lyrics/', views.LyricsListView.as_view(), name='list'),
    path('lyrics/<int:pk>/', views.LyricsDetailView, name='detail'),
    path('lyrics/form/', views.LyricsFormView, name='form'),
    path('lyrics/<int:pk>/edit', views.LyricsUpdateView.as_view(), name='edit'),
    path('lyrics/<int:pk>/delete', views.LyricsDeleteView, name='delete')
]

urlpatterns = format_suffix_patterns(urlpatterns)