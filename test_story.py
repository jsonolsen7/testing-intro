import sys
sys.path.append('./src')
import pytest
# import sqlite3
# import requests
import os
import src.story_project

def test_file_exists():
    assert os.path.exists('./story_project.log')

def test_items_list():
    assert len(src.story_project.items_list) == 11

@pytest.mark.parametrize("inputs, expected_output", [
    (("100lb oxygen tank", 14), ("100lb oxygen tank", 14)),
    (("water", 4), ("water", 4)),
    (("stellar map", 1), ("stellar map", 1)),
    ((".45 calibre pistol", 1), (".45 calibre pistol", 1)),
    (("life raft", 1), ("life raft", 1))
])

def test_select_items(inputs, expected_output):
    print("\nSelect Items Iteration - Test Start")
    src.story_project.selected_items.append((inputs[0], inputs[1]))
    assert src.story_project.selected_items[len(src.story_project.selected_items) - 1] == expected_output

@pytest.mark.parametrize("inputs2, expected_output2", [
    (("100lb oxygen tank", 14), 62),
    (("water", 4), 32),
    (("stellar map", 1), 31.5),
    ((".45 calibre pistol", 1), 31),
    (("life raft", 1), 66)
])

def test_weight_limit(inputs2, expected_output2):
    print("\nCorrect Weight Limit Reduction - Test Start")
    if inputs2[0] == "100lb oxygen tank":
        src.story_project.weight_limit -= inputs2[1] * src.story_project.oxygen_tank[1]
        assert src.story_project.weight_limit == expected_output2
    elif inputs2[0] == "water":
        src.story_project.weight_limit -= inputs2[1] * src.story_project.water[1]
        assert src.story_project.weight_limit == expected_output2
    elif inputs2[0] == "stellar map":
        src.story_project.weight_limit -= inputs2[1] * src.story_project.stellar_map[1]
        assert src.story_project.weight_limit == expected_output2
    elif inputs2[0] == ".45 calibre pistol":
        src.story_project.weight_limit -= inputs2[1] * src.story_project.pistol[1]
        assert src.story_project.weight_limit == expected_output2
    elif inputs2[0] == "life raft":
        src.story_project.weight_limit -= inputs2[1] * src.story_project.life_raft[1]
        src.story_project.weight_limit += 50
        assert src.story_project.weight_limit == expected_output2