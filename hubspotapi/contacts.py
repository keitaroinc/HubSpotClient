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