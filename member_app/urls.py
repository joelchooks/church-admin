from django.urls import path, include
from .filters import OrderMemberFilter
from member_app import APIviews, views, messageViews
from rest_framework.urlpatterns import format_suffix_patterns
from django_filters.views import FilterView

app_name = 'church_app'

urlpatterns = [
    # API

    path('api/members/', APIviews.MemberList.as_view()),
    path('api/members/<int:pk>/', APIviews.MemberDetail.as_view()),
    path('api/messages/', APIviews.MessageList.as_view()),
    path('api/messages/<int:pk>/', APIviews.MessageDetail.as_view()),
    path('api/members/search/<str:q>/', APIviews.MemberSearchView.as_view()),
    path('members/messages/drafts/<int:pk>/detail/status/', APIviews.MessageAPIView.as_view()),
    path('members/json/<int:num_members>/', APIviews.MemberJsonView.as_view()),
  

    # Members

    path('', views.index, name='index'),
    path('members/', views.MemberListView.as_view(), name='list'),
    path('generate-member-details/', views.GenerateMemberDetails, name='generate-member'),
    path('members/<int:pk>/', views.MemberDetailView, name='detail'),
    path('members/form/', views.MemberFormView.as_view(), name='form'),
    path('members/<int:pk>/edit', views.MemberUpdateView.as_view(), name='edit'),
    path('members/<int:pk>/delete', views.MemberDeleteView, name='delete'),

    # Attendance

    path('attendance/', views.AttendanceListView.as_view(), name='att_list'),
    path('attendance/<int:pk>/', views.AttendanceDetailView, name='att_detail'),
    path('attendance/form/', views.AttendanceCreateView.as_view(), name='att_form'),
    path('attendance/<int:pk>/edit/', views.AttendanceUpdateView.as_view(), name='att_edit'),

    # Messages

    path('members/messages/', messageViews.MessageListView.as_view(), name='message_list'),
    path('members/messages/form/', messageViews.MessageFormView, name='message_form'),
    path('members/messages/<int:pk>/', messageViews.MessageDetailView, name='message_detail'),
    path('members/messages/drafts/', messageViews.MessageDraftView.as_view(), name='message_draft'),
    path('members/messages/drafts/<int:pk>/form/', messageViews.UpdateMessageView.as_view(), name='message_update'),
    path('members/messages/drafts/<int:pk>/detail/', messageViews.DraftMessageDetailView, name='draft_message_detail'),



    # path('attendance/<int:pk>/calc-overall', views.AttendOverall, name='calc_overall'),
    # path('attendance/<int:pk>/delete', views.AttendanceUpdateView.as_view(), name='att_delete')

    # path('members/', FilterView.as_view(filterset_class=OrderMemberFilter,
    #     template_name='church_app/member_list.html'), name='search'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
