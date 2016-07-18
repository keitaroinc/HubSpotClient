from .companies import Companies
from .contacts import Contacts
from .deals import Deals

class HubSpotClient(object):
    def __init__(self, api_key, api_url=None):
        # Register contacts API client
        self.contacts = Contacts(api_key, api_url)
        
        # Register Companies API client 
        self.companies = Companies(api_key, api_url)
        
        # Register Deals API client
        self.deals = Deals(api_key, api_url)