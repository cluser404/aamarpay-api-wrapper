from dataclasses import dataclass


@dataclass
class InitiationResponse:
    result: bool
    payment_url: str
