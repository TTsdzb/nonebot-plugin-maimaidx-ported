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
    ready: bool = False


__data: PluginData = PluginData()


def load() -> None:
    """插件启动时加载基本数据。"""
    try:
        # 加载插件设置
        __data.config = Config.parse_obj(get_driver().config).maimaidx
    except ValidationError as e:
        logger.critical(f"未能加载插件配置：{e}")
        logger.critical("本插件将无法工作")
        return
    try:
        __data.config.data_path.mkdir(parents=True, exist_ok=True)
    except PermissionError as e:
        logger.critical(f"没有足够的权限，无法创建数据文件夹：{e}")
        logger.critical("如果您使用Windows，请避免将数据目录设置在C盘；如果您使用Linux，请避免将数据目录设置在家目录之外的地方。")
        return
    __data.ready = True
