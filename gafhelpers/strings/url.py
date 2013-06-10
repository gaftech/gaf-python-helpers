# -*- coding: utf-8 -*-
import urllib
import posixpath
import urlparse

def build_url(*args, **kwargs):
    """
    function build_url(netloc[, path_part1[, ...]][, scheme='http'][, query=''][, fragment=''][, trailing_slash=''][, port=None][, username=None[, password=None]])  
    
    >>> build_url('www.example.com', 'part1/', 'part2/part3', 'part4.html')
    'http://www.example.com/part1/part2/part3/part4.html'
    
    """
    netloc = args[0]
    port = kwargs.get('port', None)
    if port:
        assert ':' not in netloc
        netloc = '%s:%s' % (netloc, port)
    username = kwargs.get("username", None)
    if username:
        userinfos = username
        password = kwargs.get("passwrod", None)
        if password:
            userinfos = "%s:%s" % (userinfos, password)
        netloc = "%s@%s" % (userinfos, netloc)
    parts = args[1:]
    scheme = kwargs.get('scheme', 'http')
    query = kwargs.get('query', '')
    fragment = kwargs.get('fragment', '')
    trailing_slash = kwargs.get('trailing_slash', False)
    
    if not isinstance(query, basestring):
        query = urllib.urlencode(query)
    
    if len(args) > 1:
        path = posixpath.normpath('/'.join(parts))
    else:
        path = '' 
    if trailing_slash and path[-1] != '/':
        path += '/'
    url  = urlparse.urlunsplit((scheme, netloc, path, query, fragment))
    return url
        