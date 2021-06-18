from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, Numeric, CHAR, Integer, Date, VARCHAR, BINARY
from sqlalchemy.dialects.mysql import DOUBLE

cc_delin_rate_model = declarative_base()


class cc_delin_rate(cc_delin_rate_model):
    __tablename__ = 'CC_DELIN_RATE'
    CUST_ID = Column("CUST_ID", Numeric, nullable=False, primary_key=True)
    QUARTER_YEAR = Column("QUARTER_YEAR", CHAR(7), nullable=False)
    ROLLOVERS = Column("ROLLOVERS", BINARY(6), nullable=False)
    BAD_CUST = Column("BAD_CUST", BINARY(6), nullable=False)
    CC_OUT_BAL = Column("CC_OUT_BAL", Numeric, nullable=False)
    REPORTABLE = Column("REPORTABLE", Numeric, nullable=False)
    CC_DELINQUENCY = Column("CC_DELINQUENCY", Float, nullable=False, primary_key=True)


