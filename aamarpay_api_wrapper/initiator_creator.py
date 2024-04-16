from abc import ABC
from abc import abstractmethod

from .initiator import Initiator


class InitiatorCreator(ABC):
    @abstractmethod
    def create_initiator(self) -> Initiator:
        return Initiator("https://...")
