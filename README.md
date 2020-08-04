The ```msgd``` server listens on UDP and sends notifications to the Desktop
environments notification system. This usually shows up as "pop-up ballons"
on a users desktop.
<pre>
Usage: msgd [OPTIONS]

  Message Daemon --- A simple program to receive textual messages via UDP
  and use the desktop environment's notification system to display the
  message.

  Allows optional logging of messages to a file.

  Also allows the idea of "message types". For example, a message of type,
  'alert' could take additional measures to notify somebody. A message type
  of 'status' could be used for telemetry recording purposes.

  The message's subtype, if present, is pre-pended to the message. For
  example, for an 'alert' subtype, the following text should be pre-pended
  to the supplied message:

          [alert]message text here

  If the text within the brackets matches a registered handler function,
  then that function will be executed.

Options:
  -b, --bindaddr TEXT     IPv4 Address to listen on. Default: 0.0.0.0
  -p, --port INTEGER      UDP port number to listen on. Default: 55555
  -l, --logfile FILENAME  File to save log messages to. Not used by default.
  --help                  Show this message and exit.

<pre>
