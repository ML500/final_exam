from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, TemplateView, DetailView

from accounts.admin import User
from webapp.forms import MessageForm
from webapp.models import Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    template_name = 'message/message_create.html'
    form_class = MessageForm
    model = Message

    def form_valid(self, form):
        user = get_object_or_404(User, pk=self.kwargs.get('pk'))
        message = form.save(commit=False)
        message.froms = self.request.user
        message.whom = user
        message.save()
        return redirect('webapp:message_correspondance')


class MessageCorrespondenceView(LoginRequiredMixin, TemplateView):
    model = Message
    template_name = 'message/message_correspondence.html'
    paginate_by = 2
    paginate_orphans = 0

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        inbox = Message.objects.filter(whom=self.request.user)
        outbox = Message.objects.filter(froms=self.request.user).order_by('-created_at')
        context['inbox'] = inbox
        context['outbox'] = outbox
        return context



class MessageDetailView(DetailView):
    template_name = 'message/message_detail.html'
    model = Message
# class ProductCreateView(CreateView):
#     template_name = 'product/product_create.html'
#     form_class = ProductForm
#     model = Product
#     permission_required = 'webapp.add_product'
#
#     def post(self, request, *args, **kwargs):
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
#
#     def get_success_url(self):
#         return reverse('webapp:product_view', kwargs={'pk': self.object.pk})
