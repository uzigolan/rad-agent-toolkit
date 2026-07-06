from .ssh import SSHBackend

_BACKENDS = {
    "ssh": SSHBackend,
}


def get_backend(name: str = "ssh"):
    return _BACKENDS[name]()
