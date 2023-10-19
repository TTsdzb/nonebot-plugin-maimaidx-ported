from typing import Dict, List

from .music import Music


def collect_by_artist(music_list: List[Music]) -> Dict[str, List[Music]]:
    """
    将歌曲按曲师分类。
    :param music_list: 所有歌曲的列表
    :return: 分类后的字典
    """
    by_artist: Dict[str, List[Music]] = {}
    for music in music_list:
        if music.basic_info.artist not in by_artist.keys():
            by_artist[music.basic_info.artist] = []
        by_artist[music.basic_info.artist].append(music)
    return by_artist


def collect_by_genre(music_list: List[Music]) -> Dict[str, List[Music]]:
    """
    将歌曲按游戏内的类别分类。
    :param music_list: 所有歌曲的列表
    :return: 分类后的字典
    """
    by_genre: Dict[str, List[Music]] = {}
    for music in music_list:
        if music.basic_info.genre not in by_genre.keys():
            by_genre[music.basic_info.genre] = []
        by_genre[music.basic_info.genre].append(music)
    return by_genre


def collect_by_bpm(music_list: List[Music]) -> Dict[int, List[Music]]:
    """
    将歌曲按BPM分类。
    :param music_list: 所有歌曲的列表
    :return: 分类后的字典
    """
    by_genre: Dict[int, List[Music]] = {}
    for music in music_list:
        if music.basic_info.bpm not in by_genre.keys():
            by_genre[music.basic_info.bpm] = []
        by_genre[music.basic_info.bpm].append(music)
    return by_genre


def collect_by_charter(music_list: List[Music]) -> Dict[str, List[Music]]:
    """
    将歌曲按谱师分类。
    :param music_list: 所有歌曲的列表
    :return: 分类后的字典
    """
    by_charter: Dict[str, List[Music]] = {}
    for music in music_list:
        for chart in music.charts:
            if chart.charter not in by_charter.keys():
                by_charter[chart.charter] = []
            by_charter[chart.charter].append(music)
    return by_charter


class MusicList:
    all: List[Music]
    by_id: Dict[int, Music]
    by_title: Dict[str, Music]
    by_artist: Dict[str, List[Music]]
    by_genre: Dict[str, List[Music]]
    by_bpm: Dict[int, List[Music]]
    by_charter: Dict[str, List[Music]]

    def __init__(self, music_list: List[Music]):
        self.all = music_list
        self.by_id = {m.id: m for m in music_list}
        self.by_title = {m.title: m for m in music_list}
        self.by_artist = collect_by_artist(music_list)
        self.by_genre = collect_by_genre(music_list)
        self.by_bpm = collect_by_bpm(music_list)
        self.by_charter = collect_by_charter(music_list)
