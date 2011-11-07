from twisted.internet import reactor, defer

from txjsonrpc.web.jsonrpc import Proxy


def printValue(value):
    print "Result: %s" % str(value)


def printError(error):
    print 'error', error


def shutDown(data):
    print "Shutting down reactor..."
    reactor.stop()


proxy = Proxy('http://127.0.0.1:6969/')
dl = []
"""
d = proxy.callRemote('echo', 'bite me')
d.addCallbacks(printValue, printError)
dl.append(d)

d = proxy.callRemote('math.add', 3, 5)
d.addCallbacks(printValue, printError)
dl.append(d)

d = proxy.callRemote('science.compare', 5, 7)
d.addCallbacks(printValue, printError)
dl.append(d)

d = proxy.callRemote('science.compare', 7, 5)
d.addCallbacks(printValue, printError)
dl.append(d)
"""

d = proxy.callRemote('stikies.get', "will")
d.addCallbacks(printValue, printError)
dl.append(d)

d = proxy.callRemote('stikies.add', "will1", "message1")
d.addCallbacks(printValue, printError)
dl.append(d)

d = proxy.callRemote('stikies.add', "will", "message")
d.addCallbacks(printValue, printError)
dl.append(d)

d = proxy.callRemote('stikies.add', "will2", "message2")
d.addCallbacks(printValue, printError)
dl.append(d)

d = proxy.callRemote('stikies.list', "will")
d.addCallbacks(printValue, printError)
dl.append(d)


dl = defer.DeferredList(dl)
dl.addCallback(shutDown)
reactor.run()
