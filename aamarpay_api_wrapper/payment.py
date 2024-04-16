from dataclasses import dataclass
from dataclasses import fields
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


@dataclass
class Payment:
    store_id: str
    signature_key: str
    tran_id: str
    amount: float
    currency: Literal["BDT", "USD"]
    desc: str
    cus_name: str
    cus_email: str
    cus_phone: str
    success_url: str
    fail_url: str
    cancel_url: str
    type: Literal["json"] = "json"
    cus_add1: str = None
    cus_add2: str = None
    cus_city: str = None
    cus_state: str = None
    cus_country: str = None
    opt_a: str = None
    opt_b: str = None
    opt_c: str = None
    opt_d: str = None

    def to_dict(self):
        return {field.name: getattr(self, field.name) for field in fields(self) if getattr(self, field.name) is not None}
