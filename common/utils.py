from rest_framework import status
from rest_framework.response import Response


def success_response(data=None, message=None, status=status.HTTP_200_OK, extra_data={}):
    result = {"status": {"code": status, "message": message}, "data": data}
    result.update(extra_data)
    return Response(result, status=status)
