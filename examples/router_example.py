import quart
import quart_classful

application = quart.Quart(__name__)

class Router(quart_classful.QuartClassful):
    @quart_classful.route("/hello")
    async def hello(self):
        return "Hello, World!"

    @quart_classful.route("/goodbye")
    async def goodbye(self):
        return "Goodbye, World!"
    
    @quart_classful.route("/hello/<name>")
    async def hello_name(self, name):
        return f"Hello, {name}!"

    @quart_classful.request_hook("after_request")
    async def after_request(self, response):
        response.headers["X-Test"] = "Test"
        return response
    
Router.register(application)
application.run()