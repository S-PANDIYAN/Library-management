def test_add_user():
    from src.services.user_service import add_user
    assert add_user("John Doe", "member") == True

def test_remove_user():
    from src.services.user_service import remove_user
    assert remove_user(1) == True

def test_get_user():
    from src.services.user_service import get_user
    user = get_user(1)
    assert user['name'] == "John Doe"
    assert user['type'] == "member"

def test_get_all_users():
    from src.services.user_service import get_all_users
    users = get_all_users()
    assert isinstance(users, list)  # Ensure it returns a list

def test_update_user():
    from src.services.user_service import update_user
    assert update_user(1, name="Jane Doe") == True