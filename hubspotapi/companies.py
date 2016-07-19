from .base import BaseClient

class Companies(BaseClient):
    
    def get_by_domain(self, domain, path=None):
        if path is None:
            path = '/companies/v2/companies/domain/{domain}'.format(domain=domain)

        return self.call(method='GET', path=path)
    
    def create(self, data, path = '/companies/v2/companies'):
        return self.call(method='POST', data=data, path=path, 
                         args={'portalId': self.portal_id},
                         headers={'Accept': 'applicaton/json'})
    
    def update(self, cid, data, path=None):
        if path is None:
            path = '/companies/v2/companies/{company_id}'.format(company_id=cid)
            
        return self.call(method='PUT', data=data, path=path)
    
    def delete(self, cid, path=None):
        if path is None:
            path = '/companies/v2/companies/{company_id}'.format(company_id=cid)
            
        return self.call(method='DELETE', path=path)
    
    def add_contact(self, company_id, contact_id, path=None):
        if path is None:
            path = '/companies/v2/companies/{company_id}/contacts/{contact_id}'\
                    .format(company_id=company_id, contact_id=contact_id)
            
        return self.call(method='PUT', path=path)
        