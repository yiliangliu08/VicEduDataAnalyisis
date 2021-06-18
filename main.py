import db


def print_hi(name):
    db_session = db.database()
    # db_session.read_product()
    # db_session.read_credit_card()
    # db_session.create_cc_by_province()
    # db_session.create_cc_debt_trends()
    # db_session.create_cc_from_mob()
    db_session.get_cc_from_mob()
    print(f'Hi, {name}')  # Press Ctrl+F
    # 8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
