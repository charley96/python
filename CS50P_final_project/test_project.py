import pytest
from project import (
    find_zip,
    extract_files,
    create_dfs,
    clean_world_cup,
    clean_matches,
    get_teams,
    formatting_players,
    merging_players,
    player_aggregation,
    player_dict,
    cup_dict,
    team_dicts,
    cup_stats,
    get_rand_country,
    country_check,
    country_nums,
    country_stats,
    player_list,
    player_select,
    get_rand_player,
    player_stats,
)


def test_missing_zip():
    with pytest.raises(SystemExit):
        find_zip("world-cup.zip")


def test_player_aggregation():
    with pytest.raises(SystemExit):
        player_aggregation("merged_df.txt")


def test_rand_country():
    assert get_rand_country(["England"]) == "England"


def test_country_stats():
    assert country_stats(0, 0, "England") == (
        "England has never won the World Cup.",
        "England has never been runner-up at the World Cup.",
    )


def test_player_select_1_value():
    assert player_select(["Smith"]) == "Smith"


def test_player_select_no_value():
    assert player_select([]) == 0
