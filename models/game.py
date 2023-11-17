from typing import List, Union, Optional
from pydantic import BaseModel


class ObjectId(BaseModel):
    oid: str


class GameData(BaseModel):
    _id: ObjectId
    chart_type: str
    gid: str
    game_time: str
    game_date: str
    team: str
    sp_name: str
    League: str
    Handed: str
    age: str
    height: str
    weight: str
    career_inn: str
    wx_record: str
    A_1: str
    A_2: str
    Blurb: str
    GS: Union[int, str]
    y_arr: str
    bar_color: str
    awx: Union[float, str]
    twx: Union[int, str]
    cy_p: float
    x_arr: str
    awx_arr: str
    mov_ave_arr: str
    homepage_x: str
    Cy_rank_league: Optional[int] = None
    Cy_rank_overall: Optional[int] = None
    sctr_arr: List[Union[str, int]]


class GameResponse(BaseModel):
    game_data: GameData
