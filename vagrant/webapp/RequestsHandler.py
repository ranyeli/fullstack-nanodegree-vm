from BaseHTTPServer import BaseHTTPRequestHandler
from ServerFuncs import *
from DBFuncs import *
import re

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

            if(self.path.endswith("/restaurants")):
                set_headers(self, 200)
                restaurants = get_all_restaurants()
                list = ""
                for r in restaurants:
                    list += "<li>{name} <br /> " \
                            "<a href='/restaurant/{id}/edit'>Edit</a> <br/>" \
                            "<a href='/restaurant/{id}/delete' data-id='{id}' name='delete'>Delete</a><br/></li>"\
                        .format(name=r.name, id=r.id)
                with open('sites/restaurants.html', 'r') as html:
                    output = html.read().format(restaurants_list=list)
                self.wfile.write(output)
                return

            if(self.path.endswith("/restaurants/new")):
                set_headers(self, 200)
                with open('sites/restaurant_form.html', 'r') as html:
                    output = html.read()
                self.wfile.write(output)
                return
            if re.search("/restaurant/\d+/edit", self.path):
                set_headers(self, 200)
                rest_id = re.search("/restaurant/(\d+)/edit", self.path).group(1)
                rest = get_restaurant(rest_id)
                with open('sites/restaurant_form.html', 'r') as html:
                    output = html.read().replace("Restaurant", rest.name)
                self.wfile.write(output)
                return

            if re.search("/restaurant/\d+/delete", self.path):
                set_headers(self, 200)
                rest_id = re.search("/restaurant/(\d+)/delete", self.path).group(1)
                rest = get_restaurant(rest_id)
                with open('sites/delete_rest.html', 'r') as html:
                    output = html.read().format(restaurant=rest.name, id=rest_id)
                self.wfile.write(output)
                return

        except IOError:
            self.send_error(404, "File Not Found $s" % self.path)

    def do_POST(self):
        try:
            if self.path.endswith(("/hello", "/hola")):
                set_headers(self, 301)
                fields = get_form_fields(self)
                messageContent = fields.get('message')
                with open('sites/post_test.html', 'r') as html:
                    output = html.read().format(data=messageContent[0])
                self.wfile.write(output)
                return

            if self.path.endswith("/restaurants/new"):
                fields = get_form_fields(self)
                rest_name = fields.get("rest_name")
                create_restaurant(rest_name[0])
                self.send_response(303)
                self.send_header('Location', '/restaurants')
                self.end_headers()
                return

            if re.search("/restaurant/\d+/edit", self.path):
                rest_id = re.search("/restaurant/(\d+)/edit", self.path).group(1)
                fields = get_form_fields(self)
                rest_name = fields.get("rest_name")
                update_restaurant(rest_id, rest_name[0])
                self.send_response(303)
                self.send_header('Location', '/restaurants')
                self.end_headers()
                return

            if re.search("/restaurant/\d+/delete", self.path):
                fields = get_form_fields(self)
                rest_id = fields.get("rest_id")
                delete_restaurant(rest_id[0])
                self.send_response(303)
                self.send_header('Location', '/restaurants')
                self.end_headers()
                return
        except:
            pass