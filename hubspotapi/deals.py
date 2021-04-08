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

import json
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
    
    def get_pipelines(self, path=None):
        if path is None:
            path = '/deals/v1/pipelines'
            
        return self.call(method='GET', path=path)
    
    def get_pipeline_by_id(self, id, path=None):
        if path is None:
            path = '/deals/v1/pipelines/{pipeline_id}'.format(pipeline_id=id)
            
        return self.call(method='GET', path=path)
    
    def get_app_pipeline(self):
        response = self.get_pipelines()
        pipelines = json.loads(response.content)
        
        for pipeline in pipelines:
            if 'label' in pipeline:
                if pipeline.get('label').lower() == self.pipeline.lower():
                    return pipeline
                
        return None