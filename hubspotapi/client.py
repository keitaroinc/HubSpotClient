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

from .companies import Companies
from .contacts import Contacts
from .deals import Deals
from .engagements import Engagements

class HubSpotClient(object):
    def __init__(self, api_key, api_url=None, portal_id=None, pipeline=None):
        # Register contacts API client
        self.contacts = Contacts(api_key, api_url, portal_id, pipeline)
        
        # Register Companies API client 
        self.companies = Companies(api_key, api_url, portal_id, pipeline)
        
        # Register Deals API client
        self.deals = Deals(api_key, api_url, portal_id, pipeline)
        
        self.engagements = Engagements(api_key, api_url, portal_id, pipeline)
        
        self.portal_id = portal_id
        self.pipeline = self.deals.get_app_pipeline()