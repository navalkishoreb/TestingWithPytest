from models.tasks import Task
from dataclasses import asdict
from copy import copy
import pytest

def test_asdict():
    t_task = Task(summary="do something", owner="naval", done=True, _id= 21)
    t_dict = asdict(t_task)

    expected = dict(summary="do something", owner="naval", done=True, _id = 21)

    assert t_dict == expected

@pytest.mark.run_these_please
def test_replace():
    t_before = Task(summary="do something", owner= "naval", done=True, _id = 21)
    t_after = copy(t_before)
    t_replace = setattr(t_before, "summary","replace doing something")
    t_after.summary = "replace something"
#    import time
#    time.sleep(1)
    t_expected = Task(summary = "replace something", owner = "naval", done=True, _id = 21 )

    assert t_after == t_expected
