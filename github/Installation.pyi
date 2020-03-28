from typing import Any, Dict

from github.GithubObject import _ValuedAttribute
from github.PaginatedList import PaginatedList

class Installation:
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def id(self) -> _ValuedAttribute: ...
    def get_repos(self) -> PaginatedList: ...