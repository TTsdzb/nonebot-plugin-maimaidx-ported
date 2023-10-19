from nonebot import get_driver, logger
from pydantic import BaseModel, ValidationError
from typing import Optional

from .types import Config, ScopedConfig


class PluginData(BaseModel):
    """
    供插件所有部分使用的全局对象。
    存储所有共享的数据。
    """
    config: Optional[ScopedConfig] = None


__data: PluginData = PluginData()


def load():
    """插件启动时加载基本数据。"""
    try:
        # 加载插件设置
        __data.config = Config.parse_obj(get_driver().config).maimaidx
    except ValidationError as e:
        logger.critical(f"未能加载插件配置：{e}")
        logger.critical("本插件将无法工作")
