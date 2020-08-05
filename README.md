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

There is a Python client implementation provided as well.
<pre>
Usage: msgclient [OPTIONS] MESSAGE

  Python 3  implementation of a simple UDP-based message protocol, designed
  to be  sent to a  listening server  on a user's  graphical  desktop.  The
  message is then displayed using the server system's Desktop environment's
  notification  mechanism.  This  usually  manifests  as a "pop-up balloon"
  notification on the user's desktop.

  Optional  message types can be  specified for  additional handling on the
  server side.

  For convenience,  the  MSGTARGET  environment  variable can  be  used  to
  specify the IPv4 address that all  target messages will be sent to.  This
  means that MSGTARGET will override any other address specified.

Options:
  -a, --address TEXT  IPv4 address to send message to. Attempts to use the
                      MSGTARGET environment variable and if MSGTARGET is set,
                      will override any other address-setting options.
                      Default: 127.0.0.1
  -t, --type TEXT     Specify a type for the given message. The type will be
                      prepended, enclosed in square brackets, to the supplied
                      message. Not used by default.
  -p, --port INTEGER  Destination port to send message to. Default: 55555
  -q, --quiet         Quiet operation. Useful for shell scripting. Default:
                      False
  -F, --fullmsg
  --help              Show this message and exit.
<pre>
