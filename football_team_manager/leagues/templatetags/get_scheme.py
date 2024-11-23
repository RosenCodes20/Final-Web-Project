from django.template import Library

from football_team_manager.schemes.models import Scheme

register = Library()

@register.simple_tag(takes_context=True)
def get_scheme(context):

    user = context["user"]

    if user.is_authenticated:
        return Scheme.objects.filter(user=user).first()