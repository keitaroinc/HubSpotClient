from .base import BaseClient

class Contacts(BaseClient):
    
    def get_by_email(self, email, **kwargs):
        path = '/contacts/v1/contact/email/{email}/profile'.format(email=email)
        return self.call(method='GET', path=path, args=kwargs)
    
    def create(self, data, path = '/contacts/v1/contact'):
        return self.call(method='POST', data=data, path=path)
        
    def update(self, cid, data, path=None):
        if path is None:
            path = '/contacts/v1/contact/vid/{contact_id}/profile'.format(contact_id=cid)
            
        return self.call(method='POST', data=data, path=path)
    
    def delete(self, cid, path=None):
        if path is None:
            path = '/contacts/v1/contact/vid/{contact_id}'.format(contact_id=cid)
            
        return self.call(method='DELETE', path=path)