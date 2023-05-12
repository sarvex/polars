import polars as pl


def test_build_info() -> None:
    build_info = pl.build_info()
    assert "version" in build_info  # version is always present
    if features := build_info.get("features", {}):
        assert "BUILD_INFO" in features
