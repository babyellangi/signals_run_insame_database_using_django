from django.dispatch import receiver, Signal
from .models import MyModel

# Define a custom signal
my_signal = Signal()

@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    # This will run in the same transaction
    MyModel.objects.create(name='Signal Created')
