from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import polars.internals as pli


def _to_rust_syntax(df: pli.DataFrame) -> str:
    """Utility to generate the syntax that creates a polars 'DataFrame' in Rust."""
    syntax = "df![\n"

    def format_s(s: pli.Series) -> str:
        if s.null_count() == 0:
            return str(s.to_list()).replace("'", '"')
        tmp = "["
        for val in s:
            if val is None:
                tmp += "None, "
            else:
                tmp += f'Some("{val}"), ' if isinstance(val, str) else f"Some({val}), "
        tmp = f"{tmp[:-2]}]"
        return tmp

    for s in df:
        syntax += f'    "{s.name}" => {format_s(s)},\n'
    syntax += "]"
    return syntax
