from todo_scratch.bk_base.db.entities.entity import Entity
from todo_scratch.bk_base.db.entities.items import items


class GroupBelongsUserEntity(Entity):
    """ユーザ情報とグループ所属情報エンティティ

    Args:
        Entity (_type_): エンティティ基底クラス
    """

    def __init__(self) -> None:
        self.user_id = items.IntItem(is_praimary=True)
        self.user_name = items.CharItem(length=30)
        self.auth_type = items.IntItem()
        self.user_status = items.IntItem()
        super().__init__()
