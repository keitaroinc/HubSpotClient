"""
Copyright (c) 2016 Keitaro AB

Use of this source code is governed by an MIT license
that can be found in the LICENSE file or at
https://opensource.org/licenses/MIT.
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