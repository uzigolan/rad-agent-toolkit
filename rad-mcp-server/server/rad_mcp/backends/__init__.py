from .ssh import SSHBackend

_BACKENDS = {
    "ssh": SSHBackend,
}

# Backends are stateful (they cache live device sessions), so hand out one
# shared instance per backend name instead of constructing per call.
_instances: dict[str, object] = {}


def get_backend(name: str = "ssh"):
    if name not in _instances:
        _instances[name] = _BACKENDS[name]()
    return _instances[name]
