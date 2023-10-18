from pydantic import BaseModel, Extra


class ScopedConfig(BaseModel, extra=Extra.ignore):
    """Plugin Config Here"""
    data_path: str


class Config(BaseModel):
    maimaidx: ScopedConfig
