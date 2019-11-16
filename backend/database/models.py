from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, Float

metadata = MetaData()

User = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(64), unique=True),
    Column("icon", String(256), nullable=True),
)

UserStatistics = Table(
    "user_statistics",
    metadata,
    Column("user_id", ForeignKey("user.id"), primary_key=True),
    Column("level", Integer, server_default="1"),
    Column("xp_required", Integer),
    Column("hp", Integer, server_default="100"),
    Column("xp", Integer, server_default="0"),
)

Monster = Table(
    "monster",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(64), unique=True),
    Column("level", Integer, server_default="1"),
    Column("icon", String(256), nullable=True),
    Column("maximum_hp", Integer, nullable=False),
)

Fight = Table(
    "fight",
    metadata,
    Column("user_id", ForeignKey("user.id")),
    Column("monster_id", ForeignKey("monster.id")),
    Column("monster_hp", Float),
)
