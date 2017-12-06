from . import Base, engine
from sqlalchemy import Column, Integer, String, BLOB


class Slots(Base):
    __tablename__ = '__pymonitor_slots__'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), index=True, nullable=False)


    def __init__(self):
        pass


    def _create_instance(self):
        """
        @comment : 根据meta信息创建具体的表格
        """
        pass


    def sample_desc(self, x=None, y=None):
        return lambda *args: 0


class Meta(Base):
    __tablename__ = "__pymonitor_meta__"
    slot_id = Column(Integer, index=True, nullable=False)
    meta_info = Column(BLOB, nullable=True)



slot = Slots()
class OnlineAndCellStatis:
    def __init__(self):
        pass


    @slot.sample_desc(x=Integer, y=[Integer, Integer])
    def sample(self):
        pass


if __name__ == '__main__':
    online_and_cell_statis = OnlineAndCellStatis()
