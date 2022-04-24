
import typing as t
from todo_scratch.bk_base.core.router import Router
from todo_scratch.bk_base.http.request import Request
from todo_scratch.bk_base.http.response.response import Response
from todo_scratch.bk_base.middleware.http_log_middleware import HttpLogMiddleware
from todo_scratch.bk_base.core.middleware import Middleware, MiddlewareProcess
from todo_scratch.bk_base.middleware.test_middleware import TestMiddleware
from todo_scratch.bk_base.util.log.log_util import get_main_logger


class WsgiApp:
    """WSGIアプリケーションメインクラス
    """

    def __init__(self) -> None:
        self.router = Router()
        self.middleware = self._load_middleware()

    def wsgi_process(self, env: dict, start_response: t.Callable) -> t.Any:
        """WSGIアプリケーションメイン処理

        Args:
            env (dict): 環境変数
            start_response (t.Callable): HTTP応答メソッド

        Returns:
            t.Any: リクエストボディ
        """
        # レスポンスの取得
        request = Request(env)
        # メソッド、URLパスからコールバック、引数を取得
        callback, kwargs = self.router.match(request)
        # ミドルウェア処理を定義
        middleware_process: MiddlewareProcess = MiddlewareProcess(
            callback, self.middleware
        )
        # コールバックからレスポンスを取得
        response: Response = \
            middleware_process.get_response_with_middleware_chain(request, **kwargs)

        get_main_logger().info('success wsgi app')
        return self._create_wsgi_response(start_response, response)

    def _load_middleware(self,) -> Middleware:
        tmp_middleware = HttpLogMiddleware()
        tmp_middleware.set_next_middleware(TestMiddleware())
        return tmp_middleware

    def _create_wsgi_response(self, start_response: t.Callable, response: Response) -> t.Any:
        # レスポンスからステータス、ヘッダーを設定
        start_response(response.status, response.header_list)
        # レスポンスボディを返す
        return [response.body]

    def __call__(self, env: dict, start_response: t.Callable) -> t.Any:
        return self.wsgi_process(env, start_response)
