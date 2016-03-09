import urlparse


def app(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/palin')])
    qs = env['QUERY_STRING']
    params = urlparse.parse_qsl(qs)
    result = ['%s=%s\n' % (k[0], k[1]) for k in params]
    return result