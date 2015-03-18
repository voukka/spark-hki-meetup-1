import hashlib
import urlparse
#import md5py


class Helper(object):

    def __call__(self, argument):
        return argument

    def _uri_parts(self, uri):
        """
        return tuple with three elements: scheme,  hostname, and the rest
        """
        #(scheme, netloc, path, query, fragment)
        try:
            result = urlparse.urlsplit(uri)
            return result.scheme, result.netloc, result.path + result.query + result.fragment
        except AttributeError:
            return 'http', 'unknown domain', 'rest'

    def _hash_string(self, s):
        return hashlib.md5(s).hexdigest()
        #return md5py.md5(s).hexdigest()

    def _anonymize_uri(self, uri):
        parts = self._uri_parts(uri)
        return "%s://%s/%s" % (parts[0], self._hash_string(parts[1]), self._hash_string(parts[2]))


    def _anonymize_ip(self, ip):
        return self._hash_string(ip)

    # _ipAddresses  ip_address
    def anonymize_event(self, event):
        if '_referrer' in event:
            event['_referrer'] = self._anonymize_uri(event['_referrer'])

        if 'page.original_uri' in event:
            event['page.original_uri'] = self._anonymize_uri(event['page.original_uri'])

        if 'page.uri' in event:
            event['page.uri'] = self._anonymize_uri(event['page.uri'])

        if 'ip_address' in event:
            event['ip_address'] = self._anonymize_ip(event['ip_address'])

        if '_ipAddresses' in event:
            del event['_ipAddresses']

        return event
