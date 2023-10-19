from typing import Dict, List
from pydantic import BaseModel


class StatsChart(BaseModel):
    cnt: int
    diff: str
    fit_diff: float
    avg: float
    avg_dx: float
    std_dev: float
    dist: List[int]
    fc_dist: List[int]


class StatsDiff(BaseModel):
    achievements: float
    dist: List[float]
    fc_dist: List[float]


class Stats(BaseModel):
    charts: Dict[str, List[StatsChart]]
    diff_data: Dict[str, StatsDiff]
