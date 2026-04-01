from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
    @abstractmethod
    def PaymentUser(self, user, balance):
        pass
