from nonebot import get_driver
from nonebot.plugin import PluginMetadata

from .config import Config

__plugin_meta = PluginMetadata(
    name="maimaidx-nonebot",
    description="移植自Hoshino的国服舞萌DX插件",
    usage="",
    config=Config,
)

config = Config.parse_obj(get_driver().config).maimaidx

