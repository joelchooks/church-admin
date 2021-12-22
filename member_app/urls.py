from django.urls import path, include
from member_app import APIviews, views
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'church_app'

urlpatterns = [
    path('api/members/', APIviews.MemberList.as_view()),
    path('api/members/<int:pk>/', APIviews.MemberDetail.as_view()),
    path('api/members/search/<str:q>/', APIviews.MemberSearchView.as_view()),


    path('members/', views.MemberListView.as_view(), name='list'),
    path('members/<int:pk>/', views.MemberDetailView, name='detail'),
    path('members/form/', views.MemberFormView, name='form'),
    path('members/<int:pk>/edit', views.MemberUpdateView.as_view(), name='edit'),
    path('members/<int:pk>/delete', views.MemberDeleteView, name='delete')
]

urlpatterns = format_suffix_patterns(urlpatterns)
