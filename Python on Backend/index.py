import tornado.web
import tornado.ioloop


## Running tornado applications required this for running in windows.
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hey there! we are getting started with backend development")


## Query is different than simple get request.
## As get request is just providing a static page, query is asking a demanding an 
# answer to a customized problem.

class queryparamRequestHandler(tornado.web.RequestHandler):
    def get(self):
        num = self.get_argument("num")
        if (num.isdigit()):
            h = "Even" if int(num) % 2 == 0 else "Odd"
            self.write(f"The digit {num} is {h}")
        else:
            self.write(f"It is not a valid integer. Please enter a valid integer")

## Writing a query in the url bar:

## url/route_name?variable_name=value   [Standard way.]

# For this case:
##localhost:8000/evenodd?num=3

class factorialRequestHandler(tornado.web.RequestHandler):
    def get(self):
        x = self.get_argument("x")
        if (x.isdigit()):
            self.write(f"The factorial of {x} is {self.fact(int(x))}")
        else:
            self.write(f"{x} is not a valid integer")

    def fact(self,x):
        if x==0:
            return 1
        elif x==1:
            return 1
        else:
            return x * self.fact(x-1)    

## Query: http://localhost:8000/factorial?x=6

## OUTPUT: The factorial of 6 is 720

## Resource Parameter:

class resourceRequestHandler(tornado.web.RequestHandler):
    def get(self,x,y):
        self.write(f"We are just returning the input, first one is Character: {x} and the second one is Integer: {int(y)}")

# INPUT: http://localhost:8000/resource/aditya/990

# Output: We are just returning the input, first one is Character: aditya and the second one is Integer: 990


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler),
        (r"/evenodd", queryparamRequestHandler),
        (r"/factorial", factorialRequestHandler),
        (r"/resource/([a-z]+)/([0-9]+)", resourceRequestHandler)
    ])

    port = 8000
    app.listen(port)
    print("Application is listening")
    tornado.ioloop.IOLoop.current().start()

## Run this on debug mode so you can stop this.
## Now open browser:
## localhost:8000  


# (r"/resource/((a-z)+)/((0-9)+)")
# REGEX:
# [a-z]+ means anything between a-z and + will allow multiple values.
# [0-9]+ means anything between 0-9 and + will allow multiple values.