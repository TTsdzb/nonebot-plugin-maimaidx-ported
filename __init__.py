from nonebot.plugin import PluginMetadata

from .plugin_data import load as plugin_data_load
from .types import Config

# 插件信息
__plugin_meta = PluginMetadata(
    name="MaimaiDX Nonebot",
    description="移植自Hoshino的国服舞萌DX插件",
    usage="查询舞萌DX的成绩等数据。",
    type="application",
    homepage="https://github.com/TTsdzb/nonebot-plugin-maimaidx-ported",
    config=Config,
)

plugin_data_load()
