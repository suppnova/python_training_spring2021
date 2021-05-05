from homework6.src.counter import User


def test_get_created_instances_no_instances():
    assert User.get_created_instances() == 0


def test_get_created_instances_three_instances():
    user, _, _ = User(), User(), User()
    assert User.get_created_instances() == 3


def test_reset_instances_counter():
    assert User.reset_instances_counter() == 3
    assert User.get_created_instances() == 0
