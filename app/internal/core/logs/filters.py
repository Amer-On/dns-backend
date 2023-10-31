from logging import Filter, LogRecord

from sanic import Request


class RequestIdFilter(Filter):
    def filter(self, record: LogRecord) -> bool:
        req_id = Request.get_current().id
        record.msg = f'{req_id} {record.msg}'
        return True


class AccessFilter(Filter):
    def filter(self, record: LogRecord) -> bool:
        request = Request.get_current()

        host = getattr(record, 'host', '-')
        method = request.method
        path = request.path
        status = getattr(record, 'status', '-')

        record.msg = f'{host} - {method} {path} {status}'
        return True
