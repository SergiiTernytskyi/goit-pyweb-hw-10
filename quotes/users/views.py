from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from .forms import SignupForm


class SignupView(View):
    template_name = "users/signup.html"
    form_class = SignupForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(to="quotes_app:root")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, context={"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(
                request, message=f"Hello {username}. Your account successfully created."
            )
            return redirect(to="users:signin")
        return render(request, self.template_name, {"form": form})
