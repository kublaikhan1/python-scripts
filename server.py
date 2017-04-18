#ps -fA | grep python
#sudo kill -9 PID
#hamad
#web.py running the server 
#python3 server.py 127.0.0.1

import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'World'
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()
