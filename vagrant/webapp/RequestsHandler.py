from BaseHTTPServer import BaseHTTPRequestHandler
from ServerFuncs import *

class WebServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if(self.path.endswith("/hello")):
                set_headers(self, 200)
                with open('sites/hello.html', 'r') as html:
                    output = html.read()
                self.wfile.write(output)
                return

            if (self.path.endswith("/hola")):
                set_headers(self, 200)
                with open('sites/hola.html', 'r') as html:
                    output = html.read()
                self.wfile.write(output)
                return
        except IOError:
            self.send_error(404, "File Not Found $s" % self.path)

    def do_POST(self):
        try:
            set_headers(self, 301)
            fields = get_form_fields(self)
            messageContent = fields.get('message')
            with open('sites/post_test.html', 'r') as html:
                output = html.read().format(data=messageContent[0])
            self.wfile.write(output)
            return
        except:
            pass
