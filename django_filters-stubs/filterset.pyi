from typing import Any, Optional, TypeVar

from .conf import settings
from .constants import ALL_FIELDS
from .filters import (
    BaseInFilter,
    BaseRangeFilter,
    BooleanFilter,
    CharFilter,
    ChoiceFilter,
    DateFilter,
    DateTimeFilter,
    DurationFilter,
    Filter,
    ModelChoiceFilter,
    ModelMultipleChoiceFilter,
    NumberFilter,
    TimeFilter,
    UUIDFilter,
)
from .utils import get_all_model_fields, get_model_field, resolve_field, try_dbfield

def remote_queryset(field: Any): ...

class FilterSetOptions:
    model: Any = ...
    fields: Any = ...
    exclude: Any = ...
    filter_overrides: Any = ...
    form: Any = ...
    def __init__(self, options: Optional[Any] = ...) -> None: ...

class FilterSetMetaclass(type):
    def __new__(cls, name: Any, bases: Any, attrs: Any): ...
    @classmethod
    def get_declared_filters(cls, bases: Any, attrs: Any): ...

FILTER_FOR_DBFIELD_DEFAULTS: Any

class BaseFilterSet:
    FILTER_DEFAULTS: Any = ...
    is_bound: Any = ...
    data: Any = ...
    queryset: Any = ...
    request: Any = ...
    form_prefix: Any = ...
    filters: Any = ...
    def __init__(
        self,
        data: Optional[Any] = ...,
        queryset: Optional[Any] = ...,
        *,
        request: Optional[Any] = ...,
        prefix: Optional[Any] = ...
    ) -> None: ...
    def is_valid(self): ...
    @property
    def errors(self): ...
    def filter_queryset(self, queryset: Any): ...
    @property
    def qs(self): ...
    def get_form_class(self): ...
    @property
    def form(self): ...
    @classmethod
    def get_fields(cls): ...
    @classmethod
    def get_filter_name(cls, field_name: Any, lookup_expr: Any): ...
    @classmethod
    def get_filters(cls): ...
    @classmethod
    def filter_for_field(cls, field: Any, field_name: Any, lookup_expr: str | None = ...) -> Filter | None: ...
    @classmethod
    def filter_for_lookup(cls, field: Any, lookup_type: Any): ...

class FilterSet(BaseFilterSet, metaclass=FilterSetMetaclass): ...

_F = TypeVar("_F", bound=FilterSet)

def filterset_factory(model: Any, filterset: type[_F] | None = ..., fields: Any = ...) -> type[_F]: ...
