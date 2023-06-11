from models.tasks import Task
import pytest

def test_defaults():
    t1 = Task()
    t2 = Task(summary=None, owner=None, done=False, _id=None)

    assert t1 == t2

@pytest.mark.run_these_please
def test_member_access():
    t = Task(summary="buy milk", owner="naval")
    assert t.summary == "buy milk"
    assert t.owner == "naval"
    assert (t.done, t._id) == (False, None)

