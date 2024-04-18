from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.utils import timezone
from memo.models import Memo
from memo.forms.memo.forms import MemoForm
# List of Memos
class MemoListView(generic.ListView):
     model = Memo
     queryset = Memo.objects.order_by('-created_at')
     # items per page
     paginate_by = 10
     template_name = "memo/list_memo.html"
     success_url = reverse_lazy('home')
# Create new Memo
class MemoCreateView(generic.CreateView):
     model = Memo
     form_class = MemoForm
     template_name = "memo/memo_form.html"
     success_url = reverse_lazy('memo:list_memo')
     object = None
     def form_valid(self, form):
         self.object = form.save(commit=False)
         self.object.created_at = timezone.now()
         self.object.save()
         return redirect('memo:list_memo')
# Update Memo
class MemoUpdateView(generic.UpdateView):
     model = Memo
     form_class = MemoForm
     template_name = "memo/memo_form.html"
     success_url = reverse_lazy('memo:list_memo')
     object = None
     def form_valid(self, form):
         self.object = form.save(commit=False)
         self.object.save()
         return redirect('memo:list_memo')
# Remove Memo
class MemoDeleteView(generic.DeleteView):
     model = Memo
     success_url = reverse_lazy('memo:list_memo')
     object = None
     def get(self, request, *args, **kwargs):
         self.object = Memo.objects.get(pk=kwargs['pk'])
         self.object.delete()
         return redirect('memo:list_memo')
