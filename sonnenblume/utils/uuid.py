from sqlalchemy.dialects.mysql.base import MSBinary
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import types
import uuid


class UUID(types.TypeDecorator):
    impl = MSBinary
    def __init__(self):
        self.impl.length = 16
        types.TypeDecorator.__init__(self,length=self.impl.length)

    def process_bind_param(self,value,dialect=None):
        try:
            return value.bytes
        except AttributeError:
            try:
                return uuid.UUID(value).bytes
            except TypeError:
                return value

    def process_result_value(self,value,dialect=None):
        if value is None:
            return value
        try:
            return uuid.UUID(bytes=value)
        except TypeError:
            return uuid.UUID(value)

