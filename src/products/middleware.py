class Middleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'cart_count' not in request.session:
            request.session['cart_count'] = 0

        response = self.get_response(request)
        return response
