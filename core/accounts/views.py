from smtplib import SMTPDataError

from django.views.generic.edit import FormView
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode



from .forms import SignUpForm

UserModel = get_user_model()


class UserRegisterFormView(FormView):
    template_name = 'accounts/signup.html'
    form_class = SignUpForm
    success_url = '/accounts/need-activate/'

    def form_valid(self, form):
        """
        Регистрация пользователя с подтверждением
        по почте

        """
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'Activate your account.'
        message = render_to_string('accounts/acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': default_token_generator.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        try:
            email.send()
        except SMTPDataError:
            return HttpResponse('EMAIL BAD')
        #return redirect('/accounts/profile/')
        return super().form_valid(form)

    def activate_account(request, uidb64, token):
        """
        Активация учетной записи по ссылке из письма

        """
        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = UserModel._default_manager.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect('/accounts/profile/')
        else:
            return HttpResponse('Activation link is invalid!')

    def need_activate_page(request):
        """
        Вывод страницы с просьбой активировать аккаунт

        """
        return render(request, 'accounts/need-activate.html')

class UserDetailView(DetailView):
    model = UserModel
    context_object_name = 'user_account'
    template_name = 'accounts/profile.html'

    def get_object(self):
        obj = UserModel.objects.get(id = self.request.user.id)
        return obj