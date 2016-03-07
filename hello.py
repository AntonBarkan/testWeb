

def app(environ, start_response):
    status = '200 OK'
    headers = [ ('Content-type', 'text/plain')]
    body = environ['QUERY_STRING'].replace('&', '\n')
    start_response(status, headers)
    return [body]
