from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('account:signin')
    template_name = 'account/signup.html'