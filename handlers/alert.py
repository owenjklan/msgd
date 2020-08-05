import logging

import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify, GdkPixbuf


def motd():
    return ("Alert handling plugin. "
            "Special bomb icon and red console text. "
            "w00t!")


def handle_message(message, msglog=None, hostname=None):
    msg = "\033[31;1m !! ALERT !!  " + message.message + "\033[0m"
    logging.info(msg)
    if msglog is not None:
        msglog.write(msg)
        msglog.flush()
    icon = GdkPixbuf.Pixbuf.new_from_file("icons/alert.png")
    notification = Notify.Notification.new(
        hostname if hostname is not None else message.from_ip,
        message.message)
    notification.set_icon_from_pixbuf(icon)
    notification.set_image_from_pixbuf(icon)
    notification.set_urgency(2)
    notification.show()
