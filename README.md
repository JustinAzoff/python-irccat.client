irccat.client
=======

API Usage
---------

### One shot

    irccat(msg, host='localhost', port=5000)

### Multiple, non-persistent


Multiple messages, but without holding a persistent connection

    c = SimpleClient(host="localhost", port=5000)
    c.send(msg)

### Multiple, persistent

Multiple messages, with a persistent connection

    c = PersistentClient(host="localhost", port=5000)
    c.send(msg)

Logbook Usage
-------------

    from logbook import Logger
    from irccat import logbookhandler

    logger=Logger("upgrader")
    h=logbookhandler.IrccatHandler('localhost',5000,channel="upgrades", bubble=True)
    h.push_application()

    l.info("Starting upgrade...")

CLI Usage
---------

    Not finished
