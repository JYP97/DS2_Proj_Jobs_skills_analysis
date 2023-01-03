from nameko.rpc import rpc

class GreetingService:
    name = "greeting_serviceW"

    @rpc
    def hello(self, name):
        return "Hello, {}!".format(name)
