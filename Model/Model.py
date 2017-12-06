from . import Base, engine
from sqlalchemy import Column, Integer, String, BLOB, ForeignKey, Float, DateTime, Date, TIMESTAMP
from sqlalchemy.orm import sessionmaker
from functools import wraps
from json import dumps


class Slots(Base):
    __tablename__ = '__pymonitor_slots__'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), index=True, nullable=False)
    meta_info = Column(BLOB, nullable=True)
    meta_format = Column(String(128), nullable=False, default='json')


def __sqlchemy_type_name(t):
    return t.__name__


def sample_desc(name=None, x=None, y=None):
    def __wapper(sample_handler):
        @wraps(sample_handler)
        def __do_sample(__self, *args, **kwargs):
            id = None
            if not hasattr(__self, '__orm_class'):
                meta_info = {}
                meta_info = {'name': name}

                col = {}
                col['__tablename__'] = '__pymonitor_%s_values__' % name
                col['__slot_id'] = Column(Integer, ForeignKey('__pymonitor_slots__.id'), nullable=False)

                if x is None:
                    col['x'] = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
                    meta_info['x'] = 'Integer'
                else:
                    col['x'] = Column(x, nullable=False, primary_key=True)
                    meta_info['x'] = __sqlchemy_type_name(x)

                y_meta = []
                for idx, item in enumerate(y):
                    col['y' + str(idx)] = Column(item, nullable=False)
                    y_meta.append(__sqlchemy_type_name(item))

                meta_info['y'] = y_meta

                orm_class = type(name, (Base,), col)
                setattr(__self, '__orm_class', orm_class)

                Base.metadata.create_all(engine)

                session = sessionmaker(bind=engine)
                session = session()
                setattr(__self, '__session', session)

                result = session.query(Slots).filter(Slots.name==name).limit(1).first()
                if not result:
                    s = Slots(name=name, meta_info=dumps(meta_info))
                    session.add(s)
                    session.commit()
                    id = s.id
                else:
                    id = result.id


            data = sample_handler(__self, *args, **kwargs)

            param = {}
            if x is not None:
                param = {'x': data[0]}
                yy = data[1]
            else:
                yy = data

            param['__slot_id'] = id
            for idx, item in enumerate(yy):
                param['y' + str(idx)] = item

            orm_class = getattr(__self, '__orm_class')
            record = orm_class(**param)

            session = getattr(__self, '__session')
            session.add(record)
            session.commit()

        return __do_sample

    return __wapper