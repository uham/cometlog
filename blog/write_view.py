from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

class WriteView(TemplateView):
    template_name = "blog/write.html"

    def get(self, request, *args, **kwargs):
        context = {}
        return self.render_to_response(context)