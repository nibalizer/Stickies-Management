from twisted.web import server
from twisted.application import service, internet

from txjsonrpc.web import jsonrpc
entries = {}


class Example(jsonrpc.JSONRPC):
    """
    An example object to be published.
    """

    addSlash = True

    def jsonrpc_echo(self, x):
        """Return all passed args."""
        return x

class Science(jsonrpc.JSONRPC):
    """
    An example science subhandler.
    """
    def jsonrpc_compare(self, a, b):
        """Return greater of two values."""
        return a if a > b else b

class Stikies(jsonrpc.JSONRPC):
    """
    A sticky subhandler.
    """
    def jsonrpc_add(self, name, entry):
        """Add entry."""
        try:
            entries[name] = entry
        except SyntaxError:
            return "Whoops, dun broke"
        else:
            return "Teleport Succesful"

    def jsonrpc_get(self, name):
        """Get entry."""
        try:
            return entries[name]
        except SyntaxError:
            return "Whoops, dun broke"


class Math(jsonrpc.JSONRPC):
    """
    An example subhandler.
    """
    def jsonrpc_add(self, a, b):
        """Return sum of arguments."""
        return a + b


application = service.Application("Example JSON-RPC Server")
root = Example()
root.putSubHandler('math', Math())
root.putSubHandler('science', Science())
root.putSubHandler('stikies', Stikies())
site = server.Site(root)
server = internet.TCPServer(6969, site)
server.setServiceParent(application)
