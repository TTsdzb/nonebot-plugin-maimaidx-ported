from nonebot import get_driver
from nonebot.plugin import PluginMetadata

from .config import Config

__plugin_meta = PluginMetadata(
    name="maimaidx-nonebot",
    description="移植自Hoshino的国服舞萌DX插件",
    usage="查询舞萌DX的成绩等数据。",
    type="application",
    homepage="https://github.com/TTsdzb/maimaidx-nonebot",
    config=Config,
)

config = Config.parse_obj(get_driver().config).maimaidx

