import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify, GdkPixbuf

from . import MSG_TYPE_HANDLERS


def motd():
    return ("supported message types query extension")


def handle_message(message, msglog=None, hostname=None):
    return_message = "\n".join(sorted(MSG_TYPE_HANDLERS.keys()))
    print("SUPPORTED MESSAGE TYPES:")
    print(return_message)

    return True  # Handling should cease
