from django.urls import path, include

from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *




app_name = 'home_cell'

urlpatterns = [
    # API
    # path('api/members/', APIviews.MemberList.as_view()),
    path('api/cells/json/', views.CellJsonView.as_view()),
    path('api/cells/search/<str:q>/', views.CellSearchView.as_view()),


    # HOME CELL
    path('homecell/', views.CellListView.as_view(), name='cell_list'),
    path('homecell/<int:pk>/', views.CellDetailView, name='cell_detail'),
    path('homecell/form/', views.CellFormView.as_view(), name='cell_form'),
    path('homecell/<int:pk>/form/', views.CellUpdateView.as_view(), name='cell_form_edit'),
    # path('members/form/', views.MemberFormView, name='form'),
    # path('members/<int:pk>/edit', views.MemberUpdateView.as_view(), name='edit'),
    path('homecell/<int:pk>/delete', views.CellDeleteView, name='cell_delete')
]

# urlpatterns = format_suffix_patterns(urlpatterns)
