from .base import BaseClient

class Deals(BaseClient):
    
    def get_by_id(self, deal_id, path=None):
        if path is None:
            path = '/deals/v1/deal/{deal_id}'.format(deal_id=deal_id)

        return self.call(method='GET', path=path)
    
    def create(self, data, path = '/deals/v1/deal'):
        return self.call(method='POST', data=data, path=path)
    
    def update(self, id, data, path=None):
        if path is None:
            path = '/deals/v1/deal/{deal_id}'.format(deal_id=id)
            
        return self.call(method='PUT', data=data, path=path)
    
    def delete(self, id, path=None):
        if path is None:
            path = '/deals/v1/deal/{deal_id}'.format(deal_id=id)
            
        return self.call(method='DELETE', path=path)