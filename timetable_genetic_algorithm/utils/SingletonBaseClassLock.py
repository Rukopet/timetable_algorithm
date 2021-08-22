from threading import Lock


class SingletonBaseClassLock(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super(SingletonBaseClassLock, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
