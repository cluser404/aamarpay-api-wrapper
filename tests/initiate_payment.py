import pytest
import os
import sys
import subprocess
from uuid import uuid4
from aamarpay_api_wrapper import Payment
from aamarpay_api_wrapper import SandboxedInitiatorCreator


def test_payment_initiation():
    payment = Payment(
        store_id="aamarpaytest",
        signature_key="dbb74894e82415a2f7ff0ec3a97e4183",
        tran_id=uuid4().hex,
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


    initiator = SandboxedInitiatorCreator().create_initiator()
    initiaion_response = initiator.initiate_payment(payment)

    if sys.platform=='win32':
        os.startfile(initiaion_response.payment_url)
    elif sys.platform=='darwin':
        subprocess.Popen(['open', initiaion_response.payment_url])
    else:
        try:
            subprocess.Popen(['xdg-open', initiaion_response.payment_url])
        except OSError:
            print ('Please open a browser on: '+initiaion_response.payment_url)

