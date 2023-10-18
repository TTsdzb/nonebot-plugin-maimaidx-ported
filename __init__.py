from nonebot import get_driver, logger
from nonebot.plugin import PluginMetadata
from pydantic import ValidationError

from .config import Config

# 插件信息
__plugin_meta = PluginMetadata(
    name="maimaidx-nonebot",
    description="移植自Hoshino的国服舞萌DX插件",
    usage="查询舞萌DX的成绩等数据。",
    type="application",
    homepage="https://github.com/TTsdzb/maimaidx-nonebot",
    config=Config,
)

try:
    # 加载插件设置
    config = Config.parse_obj(get_driver().config).maimaidx
except ValidationError as e:
    logger.critical(f"未能加载插件配置：{e}")
    logger.critical("本插件将无法工作")
