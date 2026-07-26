import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(self):
        if self._instance is None:
            with self._lock:
                if self._instance is None:
                    self._instance = super().__new__(self)

        return self._instance

s1 = Singleton()
s2 = Singleton()

print(s1 is s2)
