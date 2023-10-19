from typing import Dict, List, Optional
from pydantic import BaseModel, Field


class Best50Chart(BaseModel):
    """B50数据的单个谱面信息。"""
    achievements: float
    level: float = Field(alias="ds")
    dx_score: int = Field(alias="dxScore")
    fc: bool
    fs: bool
    level_str: str = Field(alias="level")
    level_index: int
    level_label: str
    rating: int = Field(alias="ra")
    rate: str
    song_id: int
    title: str
    type: str


class Best50Charts(BaseModel):
    """B50的主要数据对象。"""
    dx: List[Best50Chart]
    sd: List[Best50Chart]


class Best50(BaseModel):
    """向服务器查询B50时，返回的数据。"""
    additional_rating: int
    charts: Best50Charts
    nickname: str
    plate: str
    rating: int
    user_general_data: Optional[Dict]
    username: str
