import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.inspection import inspect
from models import acct_perf_model
from models import cc_delinquency_from_mob_model
from models import cc_perf_model
from models import credit_card_by_province_model
from models import credit_card_debit_trends_model
from models import credit_card_delinquency_model
from models import data_prod_model

acct_perf = acct_perf_model.acct_perf
cc_mob_delin_rate = cc_delinquency_from_mob_model.cc_mob_delin_rate
cc_perf = cc_perf_model.cc_perf
cc_prvn_delin_rate = credit_card_by_province_model.cc_prvn_delin_rate
cc_debt_trends = credit_card_debit_trends_model.cc_debt_trends
cc_delin_rate = credit_card_delinquency_model.cc_delin_rate
data_prod = data_prod_model.data_prod

postal_list = {
    "Atlantic": "B",
    "Alberta": "T",
    "British Columbia": "V",
    "Prairies": "H",
    "Ontario": "K L M N P",
    "Quebec": "G H J",
    "Overall Canada": "O",
}


class database:
    def __init__(self):
        self.session = self.create_session()

    def create_session(self):
        connection = "mysql+pymysql://Tony:1231589976@127.0.0.1:3306/mydb"
        engine = create_engine(connection)
        self.create_table(engine)
        session = sessionmaker(bind=engine, autocommit=False, autoflush=False)
        return session()

    def create_table(self, eng):
        acct_perf.metadata.create_all(eng)
        cc_mob_delin_rate.metadata.create_all(eng)
        cc_perf.metadata.create_all(eng)
        cc_prvn_delin_rate.metadata.create_all(eng)
        cc_debt_trends.metadata.create_all(eng)
        cc_delin_rate.metadata.create_all(eng)
        data_prod.metadata.create_all(eng)

    def read_product(self):
        product_dict = {"PROD_COD": "",
                        "IB_CB_INDIC": " ",
                        "PROD_HIERA_LV1_DES": "",
                        "PROD_HIREA_LV2_COD": "",
                        "PROD_HIREA_LV2_DES": "",
                        "PROD_HIREA_LV3_DES": "",
                        "PROD_HIREA_LV4_DES": "",
                        "PROD_HIREA_LV5": ""}
        data = pd.read_excel("excel/Data_Product_Hierarchy.xlsx", usecols="A:H")
        for rowIndex, row in data.iterrows():
            temp = {}
            for columnIndex, value in row.items():
                temp[columnIndex] = value
            i = 0
            for k, v in product_dict.items():
                product_dict[k] = list(temp.values())[i]
                i += 1
            print(product_dict)
            self.session.add(data_prod(**product_dict))
        self.session.commit()

    def read_credit_card(self):
        data = pd.read_csv("excel/credit_card.csv")
        for rowIndex, row in data.iterrows():
            temp = {}
            for columnIndex, value in row.items():
                if columnIndex == "product_code":
                    temp["CC_TYPE"] = value
                else:
                    temp[columnIndex.upper()] = value
            print(temp)
            self.session.add(cc_perf(**temp))
        self.session.commit()

    def create_cc_by_province(self):
        key_list = [
            "CUST_ID",
            "QUARTER_YEAR",
            "POSTAL",
            "BALANCE",
            "AUTH_LIMIT",
            "DEL_DAYS"
        ]
        results = self.session.query(
            cc_perf.ACCT_NUM,
            cc_perf.DATE,
            cc_perf.POSTAL,
            cc_perf.BALANCE,
            cc_perf.AUTH_LIMIT,
            cc_perf.DEL_DAYS,
        )
        for result in results:
            i = 0
            cc_by_province = dict()
            for data in result:
                cc_by_province[key_list[i]] = data
                i += 1

            # Get Quarter Year
            cc_by_province["QUARTER_YEAR"] =  self.get_quarter_year(cc_by_province["QUARTER_YEAR"])

            # Get Province
            for key, value in postal_list.items():
                if cc_by_province["POSTAL"][0] in value:
                    cc_by_province["CC_PROVINCE"] = key
                else:
                    cc_by_province["CC_PROVINCE"] = "Overall Canada"

            # Get Balance and Reportanble
            cc_by_province["CC_OUT_BAL"] = cc_by_province["BALANCE"] - cc_by_province["AUTH_LIMIT"]
            cc_by_province["REPORTABLE"] = cc_by_province["CC_OUT_BAL"] - cc_by_province["AUTH_LIMIT"]

            # Get Delinquency
            if cc_by_province["DEL_DAYS"] > 90:
                cc_by_province["CC_DELINQUENCY"] = cc_by_province["BALANCE"]/cc_by_province["CC_OUT_BAL"]
            else:
                cc_by_province["CC_DELINQUENCY"] = 0

            # Remove extra from dictionary
            del cc_by_province["POSTAL"]
            del cc_by_province["BALANCE"]
            del cc_by_province["AUTH_LIMIT"]
            del cc_by_province["DEL_DAYS"]

            print(cc_by_province)
            self.session.add(cc_prvn_delin_rate(**cc_by_province))
        self.session.commit()

    def create_cc_debt_trends(self):
        key_list = [
            "CUST_ID",
            "QUARTER_YEAR",
            "BALANCE",
            "AUTH_LIMIT",
            "CC_TYPE"
        ]
        results = self.session.query(
            cc_perf.ACCT_NUM,
            cc_perf.DATE,
            cc_perf.BALANCE,
            cc_perf.AUTH_LIMIT,
            cc_perf.CC_TYPE
        )
        for result in results:
            i = 0
            cc_trends = dict()
            for data in result:
                cc_trends[key_list[i]] = data
                i += 1
            cc_trends["QUARTER_YEAR"] = self.get_quarter_year(cc_trends["QUARTER_YEAR"])
            cc_trends["OS_BAL_AMT"] = cc_trends["BALANCE"] - cc_trends["AUTH_LIMIT"]
            del cc_trends["BALANCE"]
            del cc_trends["AUTH_LIMIT"]
            print(cc_trends)
            self.session.add(cc_debt_trends(**cc_trends))
        self.session.commit()

    def create_cc_from_mob(self):
        key_list = [
            "CUST_ID",
            "QUARTER_YEAR",
            "CC_TM_ON_BOOK",
            "BALANCE",
            "AUTH_LIMIT",
            "DEL_DAYS"
        ]
        results = self.session.query(
            cc_perf.ACCT_NUM,
            cc_perf.DATE,
            cc_perf.TM_ON_BOOK_MONTH,
            cc_perf.BALANCE,
            cc_perf.AUTH_LIMIT,
            cc_perf.DEL_DAYS
        )
        for result in results:
            i = 0
            cc_mob = dict()
            for data in result:
                cc_mob[key_list[i]] = data
                i += 1
            cc_mob["QUARTER_YEAR"] = self.get_quarter_year(cc_mob["QUARTER_YEAR"])
            cc_mob["PDG_ONE_MON"] = 0
            cc_mob["PDG_TWO_MON"] = 0
            cc_mob["PDG_THREE_MON"] = 0
            if cc_mob["DEL_DAYS"] > 90:
                cc_mob["PDG_THREE_MON"] = 1
            if cc_mob["DEL_DAYS"] > 60:
                cc_mob["PDG_TWO_MON"] = 1
            if cc_mob["DEL_DAYS"] > 30:
                cc_mob["PDG_THREE_MON"] = 1

            cc_mob["CC_OUT_BAL"] = cc_mob["BALANCE"] - cc_mob["AUTH_LIMIT"]

            if cc_mob["DEL_DAYS"] > 90:
                cc_mob["CC_REP_DELINQUENCY"] = cc_mob["BALANCE"] / cc_mob["CC_OUT_BAL"]
            else:
                cc_mob["CC_REP_DELINQUENCY"] = 0

            del cc_mob["BALANCE"]
            del cc_mob["AUTH_LIMIT"]
            del cc_mob["DEL_DAYS"]

            print(cc_mob)

            self.session.add(cc_mob_delin_rate(**cc_mob))
        self.session.commit()

    def get_cc_from_mob(self):
        results = self.session.query(*cc_mob_delin_rate.__table__.columns).all()
        for row in results:
            row_as_dict = dict(row)
            print(row_as_dict)

    def get_quarter_year(self, date):
        date_quarter_month = ((date.month - 1) // 3 + 1)
        date_year = date.year
        quarter_year = "q" + str(date_quarter_month) + "_" + str(date_year)
        return quarter_year
