import json

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.timezone import make_naive
from django.views import View
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView

# from webapp.forms import FileForm
# from webapp.models import File

from accounts.admin import User
from accounts.models import Profile
from webapp.models import Friend
from webapp.views.base_views import SearchView

BROWSER_DATETIME_FORMAT = '%d.%m.%Y %H:%M'


class IndexView(SearchView):
    template_name = 'friend/index.html'
    model = Profile
    context_object_name = 'users'
    paginate_by = 10
    paginate_orphans = 0

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        friend_in = Friend.objects.filter(user=self.request.user).values_list('friend', flat=True)

        context['friend_in'] = friend_in
        return context


class AddFriendView(View):

    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs.get('pk'))
        data = json.loads(request.body)
        friend = User.objects.get(pk=data['id'])
        friends, _ = Friend.objects.get_or_create(user=user, friend=friend)
        try:
            friends.save()
            return JsonResponse({'add': 'add'})
        except:
            return JsonResponse({'add': False})


class DeleteFriendView(View):
    def delete(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs.get('pk'))
        data = json.loads(request.body)
        friend = User.objects.get(pk=data['id'])
        friends = get_object_or_404(Friend, user=user, friend=friend)
        try:
            friends.delete()
            return JsonResponse({'remove': 'remove'})
        except:
            return JsonResponse({'remove': False})

# class FileDetailView(DetailView):
#     template_name = 'friend/file_detail.html'
#     model = File
#     context_object_name = 'file'


# class FileUpdateView(PermissionRequiredMixin, UpdateView):
#     template_name = 'friend/file_update.html'
#     form_class = FileForm
#     model = File
#     permission_required = 'webapp.change_file'
#
#     def has_permission(self):
#         file = self.get_object()
#         return super().has_permission() or file.author == self.request.user
#
#     def form_valid(self, form):
#         file = form.save()
#         return redirect('webapp:file_detail', pk=file.pk)
#
# class FileCreateView(CreateView):
#     template_name = 'friend/file_create.html'
#     form_class = FileForm
#     model = File
#
#     def form_valid(self, form):
#         file = form.save(commit=False)
#         file.author = self.request.user
#         file.save()
#         form.save_m2m()
#         return super().form_valid(form)
#
#     def get_success_url(self):
#         return reverse('webapp:file_detail', kwargs={'pk': self.object.pk})
#
#
# class FileDeleteView(DeleteView):
#     template_name = 'friend/file_delete.html'
#     model = File
#     success_url = reverse_lazy('webapp:index')
