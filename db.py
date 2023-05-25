import sqlite3


def add_user_to_db(user_id, username, nick):
    with sqlite3.connect("users.db") as db:
        db.execute("""
            INSERT OR IGNORE INTO users (id, username, nick) VALUES (?, ?, ?)
        """, (user_id, username, nick))
        db.commit()

def get_profile_description(user_id):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT profile_description FROM users WHERE id=?", (user_id,))
        result = cursor.fetchone()
        return result[0] if result else None


def find_user_by_nickname(nickname: str):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT id FROM users WHERE nick=?", (nickname,))
        result = cursor.fetchone()
        return result[0] if result else None


def get_user_subscription(user_id: int):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT subscription FROM users WHERE id=?", (user_id,))
        result = cursor.fetchone()
        return result[0] if result else None


def update_emoji(user_id, new_emoji):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT nick FROM users WHERE id=?", (user_id,))
        result = cursor.fetchone()
        current_nick = result[0]

        current_emoji, current_name = current_nick.split(' ', 1)
        updated_nick = f"{new_emoji} {current_name}"

        cursor.execute("UPDATE users SET nick=? WHERE id=?", (updated_nick, user_id))
        db.commit()

def get_emoji(user_id):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT nick FROM users WHERE id=?", (user_id,))
        result = cursor.fetchone()
        current_nick = result[0]

        current_emoji, _ = current_nick.split(' ', 1)
        return current_emoji


def get_ban_status(user_id):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT ban FROM users WHERE id=?", (user_id,))
        ban_status = cursor.fetchone()
        return ban_status[0] if ban_status else None
    
def ban_user(user_id):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE users SET ban = 1 WHERE id=?", (user_id,))
        db.commit()

def unban_user(user_id):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE users SET ban = 0 WHERE id=?", (user_id,))
        db.commit()

def get_id(user_id):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT id FROM users WHERE id=?", (user_id,))
        result = cursor.fetchone()
        return result[0] if result else None

def get_group(user_id):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        # escape the column
        cursor.execute("SELECT user_group FROM users WHERE id=?", (user_id,))
        get_group = cursor.fetchone()
        return get_group[0] if get_group else None

def update_user_group(user_id, group):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE users SET user_group=? WHERE id=?", (group, user_id))
        db.commit()

def get_nick(user_id):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT username FROM users WHERE id=?", (user_id,))
        result = cursor.fetchone()
        return result[0] if result else None

def get_subscription(user_id):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT subscription FROM users WHERE id=?", (user_id,))
        result = cursor.fetchone()
        return result[0] if result else None
    
def get_users_without_subscription():
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT id, username, nick FROM users WHERE subscription=0")
        result = cursor.fetchall()
        return result
    
def update_remaining_name_changes(user_id, remaining_changes):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE users SET remaining_name_changes=? WHERE id=?", (remaining_changes, user_id))
        db.commit()
        
def get_subscription_and_remaining_changes(user_id):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT subscription, remaining_name_changes FROM users WHERE id=?", (user_id,))
        result = cursor.fetchone()
        return result if result else (None, None)

def get_nickName(user_id):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT nick FROM users WHERE id=?", (user_id,))
        result = cursor.fetchone()
        return result[0] if result else None
    
def update_nickName(user_id, nick):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE users SET nick=? WHERE id=?", (nick, user_id))
        db.commit()

def get_all_users():
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT id, username, nick FROM users")
        users_data = cursor.fetchall()

    users = []
    for user_data in users_data:
        user = {"id": user_data[0], "username": user_data[1], "nickname": user_data[2]}
        users.append(user)

    return users

import sqlite3

def get_user_info_by_nickname(nickname):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE nick=?", (nickname,))
        user_data = cursor.fetchone()

    if user_data is not None:
        user_info = {
            "id": user_data[0],
            "username": user_data[1],
            "nickname": user_data[2],
            "subscription": user_data[3],
        }
        return user_info
    else:
        return None


def get_all_usersSPAM():
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT id, username, nick FROM users")
        users_data = cursor.fetchall()
        user_ids = [user_data[0] for user_data in users_data]
        return user_ids

def is_admin(user_id: int) -> bool:
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT id FROM users WHERE id = ? AND is_admin = 1", (user_id,))
        user_data = cursor.fetchone()

    return bool(user_data)


def get_admins():
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT id, username, nick FROM users WHERE is_admin = 1")
        admins_data = cursor.fetchall()
    return admins_data

def get_admin_ids():
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT id FROM users WHERE is_admin = 1")
        admins_data = cursor.fetchall()

    return [admin_data[0] for admin_data in admins_data]

def get_user_id_by_nickname(target_nickname):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()

        # Запрос на поиск пользователя с заданным никнеймом
        query = "SELECT user_id FROM users WHERE nickname = ?"
        cursor.execute(query, (target_nickname,))

        return result[0] if (result := cursor.fetchone()) else None
def add_private_chat(user1_id, user2_id):
    with sqlite3.connect("users.db") as db:
        db.execute("""
            INSERT INTO private_chats (user1_id, user2_id) VALUES (?, ?)
        """, (user1_id, user2_id))
        db.commit()

def get_private_chats(user_id):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("""
            SELECT user1_id, user2_id FROM private_chats
            WHERE user1_id = ? OR user2_id = ?
        """, (user_id, user_id))

        return cursor.fetchall()
    
def get_target_user_id_for_private_chat(user_id):
    private_chats = get_private_chats(user_id)
    
    for chat in private_chats:
        user1_id, user2_id = chat
        if user1_id == user_id:
            return user2_id
        elif user2_id == user_id:
            return user1_id

    return None

def remove_admin(user_id):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE users SET is_admin = 0 WHERE id = ?", (user_id,))
        db.commit()

def add_admin(user_id):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE users SET is_admin = 1 WHERE id = ?", (user_id,))
        db.commit()

def get_all_usersreb():
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT id, username, nickname FROM users WHERE is_admin = 0")
        users_data = [{'id': row[0], 'username': row[1], 'nickname': row[2]} for row in cursor.fetchall()]
    return users_data

def add_admin(user_id):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("UPDATE users SET is_admin = 1 WHERE id = ?", (user_id,))
        db.commit()
def get_users():
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT id, username, nick FROM users WHERE is_admin = 0")
        users_data = cursor.fetchall()
    return users_data

# Функция для получения ID админа по нику
def get_admin_id_by_nick(admin_nick):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT id FROM users WHERE nick = ? AND is_admin = 1", (admin_nick,))
        admin_data = cursor.fetchone()

    return admin_data[0] if admin_data else None

def get_all_admins():
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT id FROM users WHERE is_admin = 1")
        admin_data = cursor.fetchall()

    return [admin_id[0] for admin_id in admin_data]

def get_admin_by_nickname(nickname):
    with sqlite3.connect("users.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT id, username, nick FROM users WHERE is_admin = 1 AND nick = ?", (nickname,))
        admin_data = cursor.fetchone()
    return admin_data

