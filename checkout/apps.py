from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """
    Class for the configuration
    """
    name = 'checkout'

    def ready(self):
        """
        Function for importing signals
        """
        import checkout.signals
