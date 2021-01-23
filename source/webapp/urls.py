from django.urls import path, include

from webapp.views.friend_views import IndexView, AddFriendView

# FileDetailView, FileUpdateView, FileCreateView, FileDeleteView

app_name = 'webapp'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/add/', AddFriendView.as_view(), name='add_friend')
    # path('create/', FileCreateView.as_view(), name='file_create'),
    # path('<int:pk>/', FileDetailView.as_view(), name='file_detail'),
    # path('<int:pk>/update', FileUpdateView.as_view(), name='file_update'),
    # path('<int:pk>/delete', FileDeleteView.as_view(), name='file_delete'),
]
