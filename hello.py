def app(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    qs = env['QUERY_STRING']
    result = qs.replace('&', '\n')
    return result