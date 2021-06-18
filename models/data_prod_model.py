from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, Numeric, CHAR, Integer, Date, VARCHAR, BINARY

data_prod_model = declarative_base()


class data_prod(data_prod_model):
    __tablename__ = 'Data_Prod'
    PROD_COD = Column("Product Code", Numeric, nullable=False, primary_key=True)
    IB_CB_INDIC = Column("IB CB Indicator", CHAR(2), nullable=False)
    PROD_HIERA_LV1_DES = Column("Product Hierarchy Level 1 Description", VARCHAR(256), nullable=False)
    PROD_HIREA_LV2_COD = Column("Product Hierarchy Level 2 Code", VARCHAR(256), nullable=False)
    PROD_HIREA_LV2_DES = Column("Product Hierarchy Level 2 Description", VARCHAR(256), nullable=False)
    PROD_HIREA_LV3_DES = Column("Product Hierarchy Level 3 Description", VARCHAR(256), nullable=False)
    PROD_HIREA_LV4_DES = Column("Product Hierarchy Level 4 Description", VARCHAR(256), nullable=False)
    PROD_HIREA_LV5 = Column("Product Hierarchy Level 5 Description", VARCHAR(256), nullable=False)
