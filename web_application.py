from wsgiref.simple_server import make_server

def application(environ, start_response):
    path = environ.get('PATH_INFO')
    html_start = """<html>
                    <head>
                    <link rel="stylesheet" href="/static/site.css">
                    </head>
                    <body>
                    <p>"""
    html_end = """</p>
                  </body>
                  </html>"""
    status = "200 OK"
    if path == '/':
        response_body = "Index"
    elif path == '/hello':
        response_body = "paas"
    else:
        status = "404 Not Found"
        response_body = "Page not found"
    response_body = html_start + response_body + html_end
    response_headers = [("Content-Length", str(len(response_body)))]
    start_response(status, response_headers)
    return [response_body]

if __name__ == '__main__':
    httpd = make_server(
        '127.0.0.1', 8001, application)
    httpd.serve_forever()
