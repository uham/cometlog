from django.views.generic import FormView, DetailView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from blog.forms import PostWriteForm

@method_decorator(staff_member_required(login_url='account:signin'), name='dispatch')
class WriteView(FormView):
    template_name = "blog/write.html"
    form_class = PostWriteForm
    success_url = reverse_lazy('blog:main')

    def form_valid(self, form):
        form.save()
        return super(WriteView, self).form_valid(form)