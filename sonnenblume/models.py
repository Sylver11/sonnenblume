from sqlalchemy import Boolean, Column, ForeignKey, Integer,String,DateTime,Text, Table, MetaData
from sqlalchemy.orm import relationship
from .database import Base
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import uuid as uuid_ext
from .utils.uuid import UUID

metadata = MetaData()

class DatabaseResponse():
    query_status = None
    query_message = None
    query_type = None


class Log(Base):
    __tablename__ = 'so_logs'
    uuid = Column(
            UUID(),
            primary_key=True,
            default=uuid_ext.uuid4)
    logger = Column(String(255))
    level = Column(String(255))
    trace = Column(Text)
    msg = Column(Text)
    created = Column(DateTime, default=datetime.utcnow)
    updated = Column(DateTime,
            default=datetime.utcnow,
            onupdate=datetime.utcnow)

    def __init__(self, logger=None, level=None, trace=None, msg=None):
        self.logger = logger
        self.level = level
        self.trace = trace
        self.msg = msg

    def __unicode__(self):
        return self.__repr__()

    def __repr__(self):
        return "<Log: %s - %s>" % (self.created_at.strftime('%m/%d/%Y-%H:%M:%S'), self.msg[:50])


user_role_assoc = Table('so_user_role_assoc',
        metadata,
        Column(
            'user_uuid',
            UUID,
            ForeignKey('so_user.uuid'),
            primary_key=True),
        Column(
            'role_uuid',
            UUID,
            ForeignKey('so_user_role.uuid'),
            primary_key=True),
        extend_existing=True)

user_group_assoc = Table('so_user_group_assoc',
        metadata,
        Column(
            'user_uuid',
            UUID,
            ForeignKey('so_user.uuid'),
            primary_key=True),
        Column(
            'group_uuid',
            UUID,
            ForeignKey('so_user_group.uuid'),
            primary_key=True),
        extend_existing=True)

class Role(Base, DatabaseResponse):
    __tablename__ = 'so_user_role'
    __table_args__ = {'extend_existing': True}
    uuid = Column(
            UUID(),
            primary_key=True,
            default=uuid_ext.uuid4)
    name = Column(String(255), unique=True)
    description = Column(String(255))
    users = relationship('User',
            secondary=user_role_assoc,
            back_populates='roles')
    created = Column(DateTime, default=datetime.utcnow)
    updated = Column(DateTime,
            default=datetime.utcnow,
            onupdate=datetime.utcnow)

class User(Base, DatabaseResponse):
    __tablename__ = 'so_user'
    __table_args__ = {'extend_existing': True}
    uuid = Column(
            UUID(),
            primary_key=True,
            default=uuid_ext.uuid4)
    firstname = Column(String(255),index=True, nullable=False)
    secondname = Column(String(255), index=True, nullable=False)
    email = Column(String(255), index=True, unique=True, nullable=False)
    password_hash = Column(String(128))
    thirdparty_authenticated = Column(Boolean, nullable=False,
            default=False)
    thirdparty_name = Column(String(255))
    authenticated = Column(Boolean, nullable=False, default=False)
    last_login_at = Column(DateTime())
    current_login_at = Column(DateTime())
    last_login_ip = Column(String(100))
    current_login_ip = Column(String(100))
    login_count = Column(Integer)
    active = Column(Boolean())
    roles = relationship('Role',
            secondary=user_role_assoc,
            back_populates='users')
    groups = relationship('Group',
            secondary=user_group_assoc,
            back_populates='users')
    created = Column(DateTime, default=datetime.utcnow)
    updated = Column(DateTime,
            default=datetime.utcnow,
            onupdate=datetime.utcnow)

    def get_id(self):
        return self.uuid

    def is_authenticated(self):
        return self.authenticated

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        return self.active

    def toggle_active(self):
        self.active = not self.active

    def deactivate_user(self):
        self.active = False

    def add_groups(self, *groups):
        self.groups.extend([group for group in groups if group not in
            self.groups])

    def remove_groups(self, *groups):
        self.groups = [group for group in self.groups if group not in groups]

    def add_roles(self, *roles):
        self.roles.extend([role for role in roles if role not in self.roles])

    def remove_roles(self, *roles):
        self.roles = [role for role in self.roles if role not in roles]

    def has_role(self, *requirements):
        user_roles = [role.name for role in self.roles]
        for requirement in requirements:
            if isinstance(requirement, (list, tuple)):
                tuple_of_role_names = requirement
                authorized = False
                for role_name in tuple_of_role_names:
                    if role_name in user_roles:
                        return True
            else:
                role_name = requirement
                if role_name in user_roles:
                    return True
        return False


class Group(Base, DatabaseResponse):
    __tablename__ = 'so_user_group'
    __table_args__ = {'extend_existing': True}
    uuid = Column(
            UUID(),
            primary_key=True,
            default=uuid_ext.uuid4)
    name = Column(String(255),index=True, unique= True, nullable=False)
    admin_uuid = Column(UUID(), ForeignKey('so_user.uuid'))
    users = relationship('User',
            secondary=user_group_assoc,
            back_populates='groups')
    created = Column(DateTime, default=datetime.utcnow)
    updated = Column(DateTime,
            default=datetime.utcnow,
            onupdate=datetime.utcnow)
