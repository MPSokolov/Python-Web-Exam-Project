from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DIY_comunity.accounts'

    def ready(self):
        import DIY_comunity.accounts.signals