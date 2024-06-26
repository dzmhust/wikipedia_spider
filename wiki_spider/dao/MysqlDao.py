from sqlalchemy.engine import create_engine
from wiki_spider.settings import MYSQL_CONFIG
from sqlalchemy.orm.session import sessionmaker

engine = create_engine('mysql+pymysql://{}:{}@{}:3306/{}'.format(MYSQL_CONFIG['user'], MYSQL_CONFIG['password'],
                                                                 MYSQL_CONFIG['host'], MYSQL_CONFIG['db']),
                       connect_args={'charset': 'utf8'}, pool_size=MYSQL_CONFIG['pool_size'])

DB_Session = sessionmaker(bind=engine)