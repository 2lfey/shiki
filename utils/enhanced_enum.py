from enum import Enum

class EnhancedEnum(Enum):
    def __str__(self):
        return self.value