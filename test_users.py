from users import UserManager
import pytest

def test_add_and_get():
    um = UserManager()
    um.add_user("Alice", "alice@test.com")
    user = um.get_user("alice@test.com")
    assert user["name"] == "Alice"

def test_list_users():
    um = UserManager()
    um.add_user("Alice", "alice@test.com")
    um.add_user("Bob", "bob@test.com")
    assert len(um.list_users()) == 2

def test_get_nonexistent_user():
    """Should return None, not raise KeyError."""
    um = UserManager()
    assert um.get_user("nobody@test.com") is None

def test_delete_nonexistent_user():
    """Should raise ValueError with message, not KeyError."""
    um = UserManager()
    with pytest.raises(ValueError, match="User not found"):
        um.delete_user("nobody@test.com")
