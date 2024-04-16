from .initiator_creator import InitiatorCreator
from .sandboxed_initiator import SandboxedInitiator


class SandboxedInitiatorCreator(InitiatorCreator):
    def create_initiator(self) -> SandboxedInitiator:
        return SandboxedInitiator("https://sandbox.aamarpay.com/jsonpost.php")