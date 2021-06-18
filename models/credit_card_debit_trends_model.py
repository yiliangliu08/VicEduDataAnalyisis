from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, Numeric, CHAR, Integer, Date, VARCHAR, BINARY
from sqlalchemy.dialects.mysql import DOUBLE

cc_debt_trends_model = declarative_base()


class cc_debt_trends(cc_debt_trends_model):
    __tablename__ = 'CC_DEBT_TRENDS'
    CUST_ID = Column("CUST_ID", Numeric, nullable=False, primary_key=True)
    OS_BAL_AMT = Column("OS_BAL_AMT", Numeric, nullable=False)
    QUARTER_YEAR = Column("QUARTER_YEAR", CHAR(7), nullable=False)
    CC_TYPE = Column("CC_TYPE", CHAR(10), nullable=False)