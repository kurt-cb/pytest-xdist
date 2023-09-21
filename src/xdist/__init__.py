from xdist.plugin import (
    is_xdist_worker,
    is_xdist_master,
    get_xdist_worker_id,
    is_xdist_controller,
)
import importlib.metadata

__version__ = importlib.metadata.version("pytest-xdist")

__all__ = [
    "__version__",
    "is_xdist_worker",
    "is_xdist_master",
    "is_xdist_controller",
    "get_xdist_worker_id",
]
