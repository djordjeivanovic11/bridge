from base64 import urlsafe_b64encode
from tokenize import generate_tokens
from django.conf import settings
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import SetPasswordForm

# Views
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from .forms import CustomUserCreationForm

def index(request):
    return render(request, "authentication/index.html")


class EmailConfirmationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            str(user.pk) + str(timestamp) + str(user.is_active)
        )

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Welcome Email
            subject = "Welcome to Bridge!!"
            message = f"Hello {user.first_name}!! \nWelcome to Bride!!\nThank you for visiting our website.\nWe have also sent you a confirmation email. Please confirm your email address.\n\nThanking You\n The Bridge Team"
            send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=True)

            # Email Address Confirmation Email
            current_site = get_current_site(request)
            email_subject = "Confirm your Email @Bridge!!"
            
            # Generate email confirmation token
            token_generator = EmailConfirmationTokenGenerator()
            uid = urlsafe_b64encode(force_bytes(user.pk))
            token = token_generator.make_token(user)

            # Generate the confirmation URL using reverse
            confirmation_url = reverse('name_of_confirmation_view', kwargs={'uidb64': uid, 'token': token})
            confirmation_url = f'http://{current_site.domain}{confirmation_url}'

            # Render email template
            message2 = render_to_string('email_confirmation.html', {
                'name': user.first_name,
                'domain': current_site.domain,
                'confirmation_url': confirmation_url,
            })

            # Send confirmation email using send_mail
            send_mail(
                email_subject,
                message2,
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=True,
            )

            auth_login(request, user)  
            return redirect('login/') 

    else:
        form = CustomUserCreationForm()
    return render(request, "authentication/register.html", {"form": form})


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  
        else:
            # Authentication failed, handle accordingly (e.g., show an error message)
            return render(request, 'authentication/login.html', {'error': 'Invalid credentials'})

    return render(request, "authentication/login.html")

@login_required
def custom_logout(request):
    logout(request)
    return render(request, "authentication/logout.html")


# Password Reset Views
class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = '/password_reset/done/'
    subject_template_name = 'registration/password_reset_subject.txt'


class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    form_class = SetPasswordForm  # Use the default SetPasswordForm
    success_url = reverse_lazy('password_reset_complete')


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'registration/password_reset_complete.html'

