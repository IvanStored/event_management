from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from events.models import EventRegistration


@receiver(post_save, sender=EventRegistration)
def send_registration_email(sender, instance, created, **kwargs):
    if created:
        event = instance.event
        user = instance.user
        subject = f"Registration Confirmed for {event.title}"
        message = f"Hi {user.username},\n\nYou have successfully registered for the event '{event.title}' scheduled for {event.date}.\n\nBest regards,\nThe Event Team"
        from_email = "your_email@example.com"
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)
