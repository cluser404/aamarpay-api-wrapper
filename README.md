# aamarpay-api-wrapper

## Basic Usage
```python
# test.py

from aamarpay_api_wrapper import Payment
from aamarpay_api_wrapper import SandboxedInitiatorCreator

# create a payment object
payment = Payment(
    store_id="aamarpaytest",
    signature_key="dbb74894e82415a2f7ff0ec3a97e4183",
    tran_id="1234123211",
    amount=100.00,
    currency="BDT",
    desc="Sample payment",
    cus_name="user",
    cus_email="user@example.com",
    cus_phone="1234567890",
    success_url="http://example.com/success",
    fail_url="http://example.com/fail",
    cancel_url="http://example.com/cancel",
)

# use LiveInitiatorCreator insted for real payments
initiator = SandboxedInitiatorCreator().create_initiator()
initiaion_response = initiator.initiate_payment(payment)

print(initiaion_response.payment_url)
```

running the above code will give you a URL
```shell
$ python test.py
https://sandbox.aamarpay.com/paynow.php?track=AAM123918230192831029
```
Open the URL in a browser to complete the transaction.
Ideally, this URL is supplied to the end user.
