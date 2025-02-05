from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "human_design_in_action.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import human_design_in_action.users.signals  # noqa F401
        except ImportError:
            pass
