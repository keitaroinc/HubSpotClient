import os
import json
import requests
import logging

log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())

log_filename = os.path.join(os.getcwd(), 'error.log')
log.addHandler(logging.FileHandler(log_filename))

class BaseClient(object):
    """Simple wrapper around the HubSpot's API"""
    
    def __init__(self, api_key=None, base_url=None, portal_id=None, pipeline=None):
        
        if api_key is None:
            raise ValueError, 'Missing HubSpot API Key'
        
        if portal_id is None:
            raise ValueError, 'Missing HubSpot Portal ID'
        
        if base_url is None:
            base_url = 'https://api.hubapi.com'
            
        if pipeline is None:
            pipeline = 'default'
            
        self.api_key = api_key
        self.base_url = base_url
        self.pipeline = pipeline
        self.portal_id = portal_id
        self.allowed_status_codes = [200, 404]
            
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            print exc_type, exc_value, traceback
            
    def _generate_endpoint(self, path, query=''):
        return '{0}{1}?hapikey={2}'.format(self.base_url, 
                                           path, 
                                           self.api_key)
    
    def call(self, method, **kwargs):
        
        r = None
        endpoint = self._generate_endpoint(kwargs.pop('path'))
        if method.lower() == 'get':
            query_args = kwargs.pop('args', {})
            r = requests.get(endpoint, params=query_args)
            
        elif method.lower() == 'post':
            data = kwargs.pop('data', {}) 
            headers = kwargs.pop('headers', {})
            q_args = kwargs.pop('args', {})
            headers.update({'Content-Type': 'application/json'})
            r = requests.post(endpoint, headers=headers, json=data, params=q_args)
            
        elif method.lower() == 'put':
            data, headers = kwargs.pop('data', {}), kwargs.pop('headers', {})
            headers.update({'Content-Type': 'application/json'})
            r = requests.put(endpoint, headers=headers, json=data)
            
        elif method.lower() == 'delete':
            r = requests.delete(endpoint)
            
        else:
            raise ValueError, 'Missing implementation for %s' % method
        
        if r.status_code not in self.allowed_status_codes:
            log.error('method:{0}\nurl: {1}\nstatus_code: {2}\ncontent: {3}\nrbody:{4}\nrheaders:{5}\nrurl:{6}'\
                      .format(method, r.url, r.status_code, r.content,
                              r.request.body, r.request.headers, r.request.url))
            r = None
            
        return r
