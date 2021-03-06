from atom_bk_frame.validator.json_validator import JsonValidator
from atom_bk_frame.validator.validator_item import DatetimeValidatorItem, IntValidatorItem, TextValidatorItem, VcharValidatorItem


class TaskDataValidator(JsonValidator):
    """タスク情報データリクエストボディバリデータ

    Args:
        JsonValidator (_type_): Jsonバリデーション基底クラス
    """

    def init_validator_items(self):
        self.title = VcharValidatorItem(is_required=True)
        self.context = TextValidatorItem()
        self.deadline_at = DatetimeValidatorItem(is_required=True)
        self.task_status_id = IntValidatorItem(is_required=True)
