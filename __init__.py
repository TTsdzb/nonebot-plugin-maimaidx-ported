from nonebot import get_driver
from nonebot.plugin import PluginMetadata

from .config import Config

__plugin_meta = PluginMetadata(
    name="maimaidx-nonebot",
    description="",
    usage="",
    config=Config,
)

global_config = get_driver().config
config = Config.parse_obj(global_config)

