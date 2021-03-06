from typing import List
from todo_scratch.bk_app.entities.user_entity import UserEntity
from todo_scratch.bk_app.handlers.task_handler import TaskHandler
from todo_scratch.bk_app.validators.request_body_validators.task_data_validator import TaskDataValidator
from atom_bk_frame.controller.controller import Controller
from atom_bk_frame.http.request import Request
from atom_bk_frame.http.response.http_error_response import Response404
from atom_bk_frame.http.response.json_response import JSONResponse
from atom_bk_frame.http.response.response import Response


class TaskController(Controller):
    """タスクコントローラ
    ApiUrl[/group/<int:group_id>/task]のメソッドをまとめたクラスです

    Args:
        Controller (_type_): コントローラ基底クラス
    """

    def get(self, request: Request, user: UserEntity, url_path_param: List, **kwargs) -> Response:

        if len(url_path_param) <= 0:
            return Response404()

        return JSONResponse(dic=self._get_handler().get_task(
            group_id=int(url_path_param[0]),
            query_param=request.path_query
        ))

    def post(self, request: Request, user: UserEntity, url_path_param: List, **kwargs) -> Response:
        if len(url_path_param) <= 0:
            return Response404()

        group_id = int(url_path_param[0])
        body = request.json
        validator = TaskDataValidator(body)
        if not validator.validate():
            return Response404()

        handler = self._get_handler()

        if not handler.is_join_to_group(user.user_id.value, group_id):
            return Response404()

        if not handler.create_task(group_id, user.user_id.value, validator.result):
            return Response404()

        return Response()

    def put(self, request: Request, user: UserEntity, url_path_param: List, **kwargs) -> Response:
        if len(url_path_param) <= 1:
            return Response404()

        group_id = int(url_path_param[0])
        task_id = int(url_path_param[1])

        body = request.json

        validator = TaskDataValidator(body)
        if not validator.validate():
            return Response404()

        if not self._get_handler().update_task(task_id, group_id, user, validator.result):
            return Response404()

        return Response()

    def delete(self, request: Request, user: UserEntity, url_path_param: List, **kwargs) -> Response:
        if len(url_path_param) <= 1:
            return Response404()

        group_id = int(url_path_param[0])
        task_id = int(url_path_param[1])

        if not self._get_handler().delete_task(task_id, group_id, user.user_id.value):
            return Response404()

        return Response()

    def _get_handler(self) -> TaskHandler:
        return TaskHandler()
