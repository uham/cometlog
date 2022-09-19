from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator

@method_decorator(staff_member_required(login_url='account:signin'), name='dispatch')
class WriteView(FormView):
    template_name = "blog/write.html"