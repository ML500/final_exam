import json

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.timezone import make_naive
from django.views import View
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView

from accounts.admin import User
from accounts.models import Profile
from webapp.models import Friend
from webapp.views.base_views import SearchView

BROWSER_DATETIME_FORMAT = '%d.%m.%Y %H:%M'


class IndexView(SearchView):
    template_name = 'friend/index.html'
    model = Profile
    context_object_name = 'users'
    paginate_by = 2
    paginate_orphans = 0

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
            return Profile.objects.exclude(user=user)
        else:
            return Profile.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            friend_in = Friend.objects.filter(user=self.request.user).values_list('friend', flat=True)

            context['friend_in'] = friend_in
        else:
            users = User.objects.all()
            context['users'] = users
        return context


class AddFriendView(LoginRequiredMixin,View):

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


class DeleteFriendView(LoginRequiredMixin,View):
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
