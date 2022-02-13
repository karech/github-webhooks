from . import ping
from .registry import HandlersRegistry

__all__ = (
    'HandlersRegistry',
    'registry',
)


registry = HandlersRegistry()
registry.add_handler('ping', ping.PingPayload, ping.handle_ping)
