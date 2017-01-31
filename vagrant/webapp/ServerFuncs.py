import cgi

def page_esponse(site):
    pass
    '''
    with open('sites/hello.html', 'r') as html:
        output = html.read()
    self.wfile.write(output)
    '''
def set_headers(self, status):
    self.send_response(status)
    if self.requestline.__contains__('GET'):
        self.send_header('Content-type', 'text/html')
    self.end_headers()

def get_form_fields(self):
    ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
    if ctype == 'multipart/form-data':
        return cgi.parse_multipart(self.rfile, pdict)