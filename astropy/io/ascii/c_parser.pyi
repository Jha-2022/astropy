from collections.abc import Mapping, Sequence


class CParser:
    def __init__(
        self,
        source: object,
        strip_line_whitespace: bool,
        strip_line_fields: bool,
        delimiter: str = ...,
        comment: str | None = ...,
        quotechar: str = ...,
        header_start: int | None = ...,
        data_start: int = ...,
        data_end: int | None = ...,
        names: Sequence[str] | None = ...,
        include_names: Sequence[str] | None = ...,
        exclude_names: Sequence[str] | None = ...,
        fill_values: object = ...,
        fill_include_names: Sequence[str] | None = ...,
        fill_exclude_names: Sequence[str] | None = ...,
        fill_extra_cols: bool = ...,
        fast_reader: Mapping[str, object] | None = ...,
    ) -> None: ...

    def read(
        self,
        try_int: Mapping[str, bool] | None,
        try_float: Mapping[str, bool] | None,
        try_string: Mapping[str, bool] | None,
    ) -> tuple[dict[str, object] | list[object], list[str]]: ...

    def setup_tokenizer(self, source: object) -> None: ...
