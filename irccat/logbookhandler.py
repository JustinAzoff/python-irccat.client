from irccat import client
from logbook.notifiers import NotificationBaseHandler
from logbook.base import NOTSET

class IrccatHandler(NotificationBaseHandler):
    """Sends notifications to an irccat server
       >>> from logbook import Logger
       >>> from irccat import logbookhandler

       >>> l=Logger("my logger")
       >>> h=logbookhandler.IrccatHandler('localhost',5000,bubble=True)
       >>> h.push_application()
       >>> l.info("Hello, World!")
    """

    def __init__(self, host, port, channel=None, record_limit=None, record_delta=None,
                 level=NOTSET, filter=None, bubble=False):
        NotificationBaseHandler.__init__(self, None, record_limit, record_delta,
                                         level, filter, bubble)
        self.host = host
        self.port = port
        self.channel = channel
        self.c = client.PersistentClient(host, port)

    def emit(self, record):
        msg = "%s: %s" % (self.make_title(record), self.make_text(record))
        if self.channel:
            msg = "#%s %s" % (self.channel, msg)
        self.c.send(msg)
