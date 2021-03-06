from copy import deepcopy

import emanager.accounting.accounts as acc
from emanager.utils.data_types import CUSTOMER_DATA
from emanager.utils.directories import SELL_DATA_DIR
from emanager.utils.stakeholder import *

SELL_DATA_FILE_NAME = "customer_data.csv"
SELL_DATA_FILE_PATH = f"{SELL_DATA_DIR}/{SELL_DATA_FILE_NAME}"
CUSTOMER_GROUP = {
    "I": "Individual",
    "A": "Association",
    "B": "Business",
    "G": "Government",
}


class Customer(StakeHolder):
    def __init__(self, id):
        print(f"Customer {id}  initiated...")
        self._id = id
        super().__init__(id, SELL_DATA_DIR, SELL_DATA_FILE_NAME, CUSTOMER_DATA)


class AddCustomer(AddStakeHolder):
    """Add new customers to database"""

    def __init__(
        self, name, address, mobile_no, group=CUSTOMER_GROUP["I"], **acc_kwargs
    ):
        print(f"Adding new Customer {name}....")
        self.name = name
        self.data_dir = SELL_DATA_DIR
        self.details = deepcopy(CUSTOMER_DATA)
        self.details.update(
            {
                "NAME": name,
                "ADDRESS": address,
                "MOBILE_NO": mobile_no,
                "GROUP": group,
            }
        )
        super().__init__(stakeholder_type="CUSTOMER")
        self.add_entry(SELL_DATA_FILE_PATH)
        # TODO find proper way to connet to ui
        acc_no = acc.check_account_existance(self.name, self.mobile_no)
        if acc_no is None:
            self.open_account(**acc_kwargs)
