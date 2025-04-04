from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as DjangoLoginView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class RegisterView(View):
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally log the user in immediately after registration:
            # login(request, user)
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})

class LoginView(DjangoLoginView):
    template_name = 'accounts/login.html'
    next_page = reverse_lazy('profile')  # Redirect after successful login

class ProfileView(LoginRequiredMixin, View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        return render(request, self.template_name, {'user': request.user})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('login')) # Redirect to login page after logout
