from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, Numeric, CHAR, Integer, Date, VARCHAR
from sqlalchemy.dialects.mysql import DOUBLE

cc_perf_model = declarative_base()


class cc_perf(cc_perf_model):
    __tablename__ = 'CC_PERF'
    ACCT_NUM = Column("ACCT_NUM", Integer, nullable=False, primary_key=True)
    DATE = Column("DATE", Date, nullable=False)
    CC_TYPE = Column("CC_TYPE", Integer, nullable=False)
    CC_CRI = Column("CC_CRI", VARCHAR(1), nullable=False)
    DEL_DAYS = Column("DEL_DAYS", Integer, nullable=False)
    POSTAL = Column("POSTAL", VARCHAR(6))
    BALANCE = Column("BALANCE", DOUBLE, nullable=False)
    PREMIUM = Column("PREMIUM", VARCHAR(3), nullable=False)
    AUTH_LIMIT = Column("AUTH_LIMIT", DOUBLE, nullable=False)
    TM_ON_BOOK_MONTH = Column("ACCT_TM_ON_BOOK_MONTHNUM", Integer, nullable=False)
