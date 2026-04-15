from users import UserManager

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
