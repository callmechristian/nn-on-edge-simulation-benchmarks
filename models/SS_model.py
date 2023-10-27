from abc import ABC, abstractmethod

class InitMeta(type):
    def __call__(cls, *args, **kwargs):
        if cls is SS_Model:
            raise TypeError(f"Can't instantiate abstract class {cls.__name__}")
        instance = super().__call__(*args, **kwargs)
        if not hasattr(instance, '__init__') or instance.__init__ == SS_Model.__init__:
            raise NotImplementedError(f"Subclass {cls.__name__} must implement its own __init__ method.")
        return instance

class SS_Model(ABC):
    @abstractmethod
    def predict(self):
        pass

    @abstractmethod
    def correct_result(self):
        pass