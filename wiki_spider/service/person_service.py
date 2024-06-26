# -*- coding: utf-8 -*-
# @time    : 2024/6/26
# @author  : dzm
# @dsec    : wiki人物
import datetime
from sqlalchemy import Column,String,DateTime,Integer
from sqlalchemy.ext.declarative import declarative_base
from wiki_spider.dao.MysqlDao import DB_Session
from contextlib import contextmanager
import traceback
from wiki_spider.utils import str_util

Model = declarative_base()

@contextmanager
def session_scope(realonly=False):
    session = DB_Session()
    try:
        yield session
        if not realonly:
            session.commit()
    except Exception as e:
        session.rollback()
        traceback.print_exc()
        raise
    finally:
        session.close()

class PersonUrl(Model):
    __tablename__ = 'person_url'
    id = Column(String(32), primary_key=True)
    name = Column(String(50), nullable=False)
    url = Column(String(200), nullable=False)
    create_time = Column(DateTime, nullable=False)

    def __init__(self, **items):
        for key in items:
            if hasattr(self, key):
                setattr(self,key,items[key])

class PersonUrlService(object):
    '''
    人物url服务
    '''
    def __init__(self):
        pass

    def exist(self,url):
        '''
        判断url是否存在
        :param url:
        :return:
        '''
        with session_scope(True) as session:
            query = session.query(PersonUrl).filter(PersonUrl.url==url)
            return query.count()>0

    def add(self,record):
        '''
        新增
        :param record:
        :return:
        '''
        with session_scope() as session:
            if not self.exist(record.url):
                record.id = str_util.get_uuid()
                record.create_time = datetime.datetime.now()
                session.add(record)


