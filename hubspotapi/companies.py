"""
Copyright (c) 2016 Keitaro AB

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

https://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from .base import BaseClient

class Companies(BaseClient):
    
    def get_by_domain(self, domain, path=None):
        if path is None:
            path = '/companies/v2/companies/domain/{domain}'.format(domain=domain)

        return self.call(method='GET', path=path)
    
    def create(self, data, path = '/companies/v2/companies'):
        return self.call(method='POST', data=data, path=path, 
                         args={'portalId': self.portal_id})
    
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
        