from pydantic import BaseModel, Extra


class ScopedConfig(BaseModel, extra=Extra.ignore):
    """插件配置的实际声明。"""
    data_path: str


class Config(BaseModel, extra=Extra.ignore):
    """插件配置对象，用于解析整个Nonebot配置。"""
    maimaidx: ScopedConfig
