import tornado.web
import tornado.ioloop


## Running tornado applications required this for running in windows.
import asyncio
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


class basicRequestHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hey there! we are getting started with backend development")



if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", basicRequestHandler)
    ])

    port = 8000
    app.listen(port)
    print("Application is listening")
    tornado.ioloop.IOLoop.current().start()

## Run this on debug mode so you can stop this.
## Now open browser:
## localhost:8000  