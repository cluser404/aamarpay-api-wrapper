from dataclasses import dataclass
try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


@dataclass
class PaymentResponse:
    pg_service_charge_bdt: float
    amount_original: float
    status_code: int
    pay_status: str
    success_url: str
    fail_url: str
    cus_name: str
    cus_email: str
    cus_phone: str
    currency_merchant: Literal["BDT", "USD"]
    conversion_rate: float
    pg_txnid: str
    mer_txnid: str
    store_id: str
    merchant_id: str
    currency: Literal["BDT", "USD"]
    store_amount: float
    pay_time: str
    amount: float
    bank_txn: str
    card_type: str
    reason: str
    pg_card_risklevel: int
    pg_error_code_details: int
    opt_a: str = None
    opt_b: str = None
    opt_c: str = None
    opt_d: str = None
