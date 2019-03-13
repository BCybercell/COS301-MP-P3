
def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)
        status = '200 OK'
        output = 'Hello World!\n'
        response_headers = [('Content-type', 'text/plain'),
                            ('Content-Length', str(len(output)))]
        response(status, response_headers)
        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
