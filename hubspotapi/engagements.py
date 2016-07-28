import json
from .base import BaseClient

class Engagements(BaseClient):
    
    def get_by_id(self, id, path=None):
        if path is None:
            path = '/engagements/v1/engagements/{id}'.format(id=id)

        return self.call(method='GET', path=path)
    
    def create(self, data, path = '/engagements/v1/engagements'):
        return self.call(method='POST', data=data, path=path)
    
    def update(self, id, data, path=None):
        if path is None:
            path = '/engagements/v1/engagements/{id}'.format(id=id)
            
        return self.call(method='PUT', data=data, path=path)
    
    def delete(self, id, path=None):
        if path is None:
            path = '/engagements/v1/engagements/{id}'.format(id=id)
            
        return self.call(method='DELETE', path=path)