from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, Numeric, CHAR, Integer, Date, VARCHAR, BINARY

cc_mob_delin_rate_model = declarative_base()


class cc_mob_delin_rate(cc_mob_delin_rate_model):
    __tablename__ = 'CC_MOB_DELIN_RATE'
    CUST_ID = Column("CUST_ID", Numeric, nullable=False, primary_key=True)
    QUARTER_YEAR = Column("QUARTER_YEAR", CHAR(7), nullable=False)
    CC_TM_ON_BOOK = Column("CC_TM_ON_BOOK", Numeric, nullable=False)
    PDG_ONE_MON = Column("PDG_ONE_MON", BINARY(6), nullable=False)
    PDG_TWO_MON = Column("PDG_TWO_MON", BINARY(6), nullable=False)
    PDG_THREE_MON = Column("PDG_THREE_MON", BINARY(6), nullable=False)
    CC_OUT_BAL = Column("CC_OUT_BAL", Numeric, nullable=False)
    CC_REP_DELINQUENCY = Column("CC_REP_DELINQUENCY", Numeric, nullable=False)

    def __repr__(self):
        return f"<id={self.id}, username={self.username}>"

