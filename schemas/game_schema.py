def game_serializer(game) -> dict:
    data = {
        "_id": str(game.get("_id")),
        "chart_type": game.get("chart_type"),
        "gid": game.get("gid"),
        "game_time": game.get("game_time"),
        "game_date": game.get("game_date"),
        "team": game.get("team"),
        "sp_name": game.get("sp_name"),
        "League": game.get("League"),
        "Handed": game.get("Handed"),
        "age": game.get("age"),
        "height": game.get("height"),
        "weight": game.get("weight"),
        "career_inn": game.get("career_inn"),
        "wx_record": game.get("wx_record"),
        "A_1": game.get("A_1"),
        "A_2": game.get("A_2"),
        "Blurb": game.get("Blurb"),
        "GS": game.get("GS"),
        "y_arr": game.get("y_arr"),
        "bar_color": game.get("bar_color"),
        "awx": game.get("awx"),
        "twx": game.get("twx"),
        "cy_p": game.get("cy_p"),
        "x_arr": game.get("x_arr"),
        "awx_arr": game.get("awx_arr"),
        "mov_ave_arr": game.get("mov_ave_arr"),
        "homepage_x": game.get("homepage_x"),
        "Cy_rank_league": game.get("Cy_rank_league"),
        "Cy_rank_overall": game.get("Cy_rank_overall"),
        "sctr_arr": game.get("sctr_arr"),
    }

    return {k: v for k, v in data.items() if v is not None}


def games_serializer(games) -> list:
    return [game_serializer(game) for game in games]
