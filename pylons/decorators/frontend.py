"""Frontend decorators"""

import logging
from decorator import decorator

from js import jquery as jq
from js import bootstrap as bs

__all__ = ['jquery', 'bootstrap']

log = logging.getLogger(__name__)

def jquery():
    def include_jquery(func, self, *args, **kwargs):
        jq.need()
        return func(self, *args, **kwargs)
    return decorator(include_jquery)

def bootstrap():
    def include_bootstrap(func, self, *args, **kwargs):
        bs.need()
        return func(self, *args, **kwargs)
    return decorator(include_bootstrap)
    
