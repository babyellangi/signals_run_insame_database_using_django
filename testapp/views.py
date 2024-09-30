from django.http import HttpResponse
from django.db import transaction
from .signals import my_signal
from .models import MyModel

def trigger_signal(request):
    try:
        with transaction.atomic():
            my_signal.send(sender=None)
            # Simulate an error to demonstrate rollback
            raise Exception("Simulated error")
    except Exception as e:
        return HttpResponse(f"An error occurred: {str(e)}. Check the database for MyModel entries at /check-model/.")

def check_model(request):
    entries = MyModel.objects.all()
    if entries:
        entry_list = ", ".join([entry.name for entry in entries])
        return HttpResponse(f"MyModel entries: {entry_list}")
    else:
        return HttpResponse("No entries found in MyModel.")
