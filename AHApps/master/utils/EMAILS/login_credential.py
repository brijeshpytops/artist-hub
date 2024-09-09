from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

def send_welcome_email(artist_id, email, password):

    subject = 'Welcome to Artist Hub!'
    from_email = settings.EMAIL_HOST_USER
    recipient_email = email

    html_message = render_to_string(r'templates\artist\email_templates\email_send_login_credential.html', {
        'artist': artist_id,
        'password': password  
    })

    email = EmailMessage(
        subject,
        strip_tags(html_message), 
        from_email,
        [recipient_email]
    )
    email.content_subtype = 'html' 
    email.attach_alternative(html_message, 'text/html')
    email.send()