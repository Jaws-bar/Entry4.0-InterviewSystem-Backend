from sqlalchemy import Column, String, ForeignKey, Integer, Text

from ysl.db import Base


class Interviewee(Base):
    __tablename__ = 'INTERVIEWEE_TB'
    _table_args_ = {'mysql_collate': 'utf8_general_ci'}

    student_code = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=True)
    type = Column(Integer, nullable=True)
    interview = Column(Integer, ForeignKey("INTERVIEW_TB.interview_id"), nullable=True)
