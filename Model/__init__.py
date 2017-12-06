from .config import  config
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, BLOB, DateTime, Date, TIMESTAMP, Float


engine = create_engine(config['db_url'])
Base = declarative_base()

from .Model import Slots, sample_desc
