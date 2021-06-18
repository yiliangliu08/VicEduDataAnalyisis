from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, Numeric, CHAR, Integer, Date, VARCHAR
from sqlalchemy.dialects.mysql import DOUBLE
acct_perf_model = declarative_base()


class acct_perf(acct_perf_model):
    __tablename__ = 'ACCT_PERF'
    MTH_END_DT = Column("MTH_END_DT", Date, nullable=False)
    ACCT_NUM = Column("ACCT_NUM", Numeric, nullable=False, primary_key=True)
    PRD_CD = Column("PRD_CD", VARCHAR(32), nullable=False, primary_key=True)
    CNTRY_BOOKED_CD = Column("CNTRY_BOOKED_CD", VARCHAR(32), nullable=False)
    ACCT_STAT_CD = Column("ACCT_STAT_CD", VARCHAR(32), nullable=False)
    TM_ON_BOOK = Column("TM_ON_BOOK", Integer, nullable=False)
    CURRENCY_CD = Column("CURRENCY_CD", Integer, nullable=False)
    DAY_PST_DUE = Column("DAY_PST_DUE", Integer, nullable=False)
    RMNG_AMORT_PERIOD = Column("RMNG_AMORT_PERIOD", Numeric, nullable=False)
    DEFLT_INSUR_CD = Column("DEFLT_INSUR_CD", VARCHAR(32), nullable=False)
    CRNT_AUTH_LIMIT_AMT = Column("CRNT_AUTH_LIMIT_AMT", DOUBLE, nullable=False)
    OS_BAL_AMT = Column("OS_BAL_AMT", DOUBLE, nullable=False)
    SCRTY_TYPE_CD = Column("SCRTY_TYPE_CD", VARCHAR(32), nullable=False)
    DIRECT_INDIRECT_INDICATOR = Column("DIRECT_INDIRECT_INDICATOR", VARCHAR(32), nullable=False)
    PRPTY_TYPE_CD = Column("PRPTY_TYPE_CD", VARCHAR(32), nullable=False)
    PRPTY_POSTAL_CD = Column("PRPTY_POSTAL_CD", VARCHAR(32), nullable=False)
    CRNT_PRPTY_VAL_AMT = Column("CRNT_PRPTY_VAL_AMT", DOUBLE, nullable=False)
    CONTRCT_AMORT_PERIOD = Column("CONTRCT_AMORT_PERIOD", Integer, nullable=False)
    BOOKED_INTR_RATE = Column("BOOKED_INTR_RATE", Float, nullable=False)
    BOOKED_AMT = Column("BOOKED_AMT", DOUBLE, nullable=False)
    BOOKED_LTV_RATIO = Column("BOOKED_LTV_RATIO", Float, nullable=False)
    CRNT_LTV_RATIO = Column("CRNT_LTV_RATIO", Float, nullable=False)
    ACCT_OPEN_DATE = Column("ACCT_OPEN_DATE", Date, nullable=False)
    BOOK_VAL = Column("BOOK_VAL", DOUBLE, nullable=False)
    RISK_FSA = Column("RISK_FSA", VARCHAR(32), nullable=False)
    CREDIT_BUREAU_SCORE = Column("CREDIT_BUREAU_SCORE", VARCHAR(32), nullable=False)
    CREDIT_RISK_INDICATOR = Column("CREDIT_RISK_INDICATOR", CHAR(32), nullable=False)
    CURRENT_TDSR = Column("CURRENT_TDSR", Float, nullable=False)
    FORECLOSER_INDICATOR = Column("FORECLOSER_INDICATOR", VARCHAR(32), nullable=False)