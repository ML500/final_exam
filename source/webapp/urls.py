from django.urls import path, include

from webapp.views.friend_views import IndexView, AddFriendView, DeleteFriendView
from webapp.views.message_views import MessageCreateView, MessageCorrespondenceView, MessageDetailView

# FileDetailView, FileUpdateView, FileCreateView, FileDeleteView

app_name = 'webapp'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/add/', AddFriendView.as_view(), name='add_friend'),
    path('<int:pk>/delete/', DeleteFriendView.as_view(), name='delete_friend'),
    path('<int:pk>/create/', MessageCreateView.as_view(), name='message_create'),
    path('correspondance/', MessageCorrespondenceView.as_view(), name='message_correspondance'),
    path('<int:pk>/detail/', MessageDetailView.as_view(), name='messasge_detail'),
    # path('create/', FileCreateView.as_view(), name='file_create'),
    # path('<int:pk>/', FileDetailView.as_view(), name='file_detail'),
    # path('<int:pk>/update', FileUpdateView.as_view(), name='file_update'),
    # path('<int:pk>/delete', FileDeleteView.as_view(), name='file_delete'),
]
