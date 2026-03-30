# Level 9: Abstraction (Class Suci)
# Di sini kita akan belajar cara membuat 'Template' yang tidak bisa disentuh langsung.

from abc import ABC, abstractmethod

class Transportasi(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def bergerak(self):
        pass
