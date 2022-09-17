from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

@method_decorator(staff_member_required(login_url='account:signin'), name='dispatch')
class WriteView(TemplateView):
    template_name = "blog/write.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return self.render_to_response(context)