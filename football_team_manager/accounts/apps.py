from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'football_team_manager.accounts'

    def ready(self):
        import football_team_manager.accounts.signals
