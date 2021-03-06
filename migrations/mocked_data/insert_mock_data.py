from backend.classes import Monster
from backend.database.monster import create_monster, get_all_monsters
from backend.database.user import create_user


async def insert(users, monsters):
    if not await get_all_monsters():
        for m in monsters:
            await create_monster(monster=m)

        for u in users:
            await create_user(user_name=u['name'], user_icon=u['icon'], monster=u['m'])


async def insert_data():
    monsters = [
        Monster(id=1, lvl=2, max_hp=150, icon="https://drive.google.com/uc?id=117Jvzb6PTym84CiF8qi_0Q6NYth19GqO",
                name="Dioxider"),
        Monster(id=2, lvl=1, max_hp=100, icon="https://drive.google.com/uc?id=1SBGkcKdlUqjg40B_TNqUV7F3BtnhHQSD",
                name="Ozonator"),
        Monster(id=3, lvl=4, max_hp=90, icon="https://drive.google.com/uc?id=14KilPOpzYQHOrs3tWqp-ZnFh_0rMibhM",
                name="The iron spite particle"),
        Monster(id=4, lvl=3, max_hp=120, icon="https://drive.google.com/uc?id=1qF7ATZ172nFpzBTya1KNy8wawuntAUjh",
                name="Shadebrute"),
        Monster(id=5, lvl=8, max_hp=130, icon="https://drive.google.com/uc?id=1pdfeneCRld71lXX5A5RgSZw_LVGjECGF",
                name="The dark razordust"),
        Monster(id=6, lvl=7, max_hp=140, icon="https://drive.google.com/uc?id=117Jvzb6PTym84CiF8qi_0Q6NYth19GqO",
                name="Acidhound"),
        Monster(id=7, lvl=6, max_hp=110, icon="https://drive.google.com/uc?id=1SBGkcKdlUqjg40B_TNqUV7F3BtnhHQSD",
                name="Smokechild"),
        Monster(id=8, lvl=9, max_hp=111, icon="https://drive.google.com/uc?id=14KilPOpzYQHOrs3tWqp-ZnFh_0rMibhM",
                name="Dusthag"),
        Monster(id=9, lvl=10, max_hp=20, icon="https://drive.google.com/uc?id=1qF7ATZ172nFpzBTya1KNy8wawuntAUjh",
                name="Radioactive cloud"),
        Monster(id=10, lvl=12, max_hp=80, icon="https://drive.google.com/uc?id=1pdfeneCRld71lXX5A5RgSZw_LVGjECGF",
                name="Chaoscat"),
    ]

    users = [
        {'name': 'Psyduck', 'icon': 'https://drive.google.com/uc?id=18Hz6uyLsnGTnUmezXtA5bGqbVYBvJJRf',
         'm': monsters[2]}
    ]
    await insert(users, monsters)
