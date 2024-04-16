from .initiator_creator import InitiatorCreator
from .live_initiator import LiveInitiator


class LiveInitiatorCreator(InitiatorCreator):
    def create_initiator(self) -> LiveInitiator:
        return LiveInitiator("https://secure.aamarpay.com/jsonpost.php")