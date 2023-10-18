from typing import List
from pydantic import BaseModel, Field


class MusicChart(BaseModel):
    """乐曲的谱面信息。"""
    notes: List[int]
    charter: str


class MusicBasicInfo(BaseModel):
    """乐曲的一些基本信息。"""
    title: str
    artist: str
    genre: str
    bpm: int
    release_date: str
    source: str = Field(alias="from")
    is_new: bool


class Music(BaseModel):
    """
    一首乐曲的信息。
    同一个曲子的标谱与DX谱视为两首乐曲。
    """
    id: int
    title: str
    type: str
    level_str: List[str] = Field(alias="level")
    level: List[float] = Field(alias="ds")
    cids: List[int]
    charts: List[MusicChart]
    basic_info: MusicBasicInfo
