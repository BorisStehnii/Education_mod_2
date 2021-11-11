from exercise_2_20_1.pack_2_20_1.exercise_2_20_1 import Open


def test_cass_open():
    with Open("file_11.txt") as file_:
        assert file_.closed is False
    assert file_.closed is True
