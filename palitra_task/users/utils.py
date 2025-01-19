from django.core.mail import send_mail
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator


def send_activation_email(user, request):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    activation_link = reverse('activate_user', kwargs={'uid': uid, 'token': token})
    activation_url = f'{request.scheme}://{request.get_host()}{activation_link}'

    subject = 'Activate Your Account'
    message = f'Hi {user.username},\n\nClick the link below to activate your account:\n{activation_url}'
    from_email = 'no-reply@yourdomain.com'

    send_mail(subject, message, from_email, [user.email])
    return activation_url

def send_password_reset_email(user, request):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    reset_link = request.build_absolute_uri(reverse('password_reset', kwargs={'uidb64': uid, 'token': token}))

    subject = 'Password Reset Request'
    message = f'Click the link to reset your password: {reset_link}'
    from_email = 'no-reply@yourdomain.com'

    send_mail(subject, message, from_email, [user.email])

    return reset_link