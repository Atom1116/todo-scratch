from atom_bk_frame.validator.json_validator import JsonValidator
from atom_bk_frame.validator.validator_item import VcharValidatorItem


class UpdateAccountValidator(JsonValidator):
    """アカウント情報更新用リクエストボディバリデータ

    Args:
        JsonValidator (_type_): Jsonバリデーション基底クラス
    """

    def init_validator_items(self):
        self.user_name = VcharValidatorItem(is_required=True)
        self.email = VcharValidatorItem(is_required=True)
