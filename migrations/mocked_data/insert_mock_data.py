import asyncio
from backend.classes import Monster
from backend.database.monster import create_monster, get_all_monsters
from backend.database.user import create_user


async def insert(users, monsters):
    if not await get_all_monsters():
        for m in monsters:
            await create_monster(monster=m)

        for u in users:
            await create_user(user_name=u['name'], user_icon=u['icon'], monster=u['m'])


if __name__ == '__main__':
    monsters = [
        Monster(id=1, lvl=2, max_hp=150, icon="https://image.flaticon.com/icons/svg/2196/2196894.svg", name="M1"),
        Monster(id=2, lvl=1, max_hp=100, icon="https://image.flaticon.com/icons/svg/2196/2196894.svg", name="M2"),
        Monster(id=3, lvl=4, max_hp=90, icon="https://image.flaticon.com/icons/svg/2196/2196894.svg", name="M3"),
        Monster(id=4, lvl=3, max_hp=120, icon="https://image.flaticon.com/icons/svg/2196/2196894.svg", name="M4"),
        Monster(id=5, lvl=8, max_hp=130, icon="https://image.flaticon.com/icons/svg/2196/2196894.svg", name="M5"),
        Monster(id=6, lvl=7, max_hp=140, icon="https://image.flaticon.com/icons/svg/2196/2196894.svg", name="M6"),
        Monster(id=7, lvl=6, max_hp=110, icon="https://image.flaticon.com/icons/svg/2196/2196894.svg", name="M7"),
        Monster(id=8, lvl=9, max_hp=111, icon="https://image.flaticon.com/icons/svg/2196/2196894.svg", name="M8"),
        Monster(id=9, lvl=10, max_hp=20, icon="https://image.flaticon.com/icons/svg/2196/2196894.svg", name="M9"),
        Monster(id=10, lvl=12, max_hp=80, icon="https://image.flaticon.com/icons/svg/2196/2196894.svg", name="M10"),
    ]

    users = [
        {'name': 'Psyduck', 'icon': 'https://image.flaticon.com/icons/svg/189/189000.svg', 'm': monsters[2]}
    ]
    asyncio.run(insert(users, monsters))
