import logging
import traceback

from django.core.exceptions import ObjectDoesNotExist
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from rest_framework import serializers
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed, NotAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import InvalidToken

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    logger.error({"exception": str(exc)})
    logger.info({"exception type": type(exc)})
    logger.info(traceback.format_exc())

    code = status.HTTP_400_BAD_REQUEST
    detail = None
    message = str(exc)

    if isinstance(exc, ObjectDoesNotExist):
        code = status.HTTP_404_NOT_FOUND
        message = "Please correct the errors below."
        detail = {"error": ["Not Found"]}

    if isinstance(exc, IntegrityError):
        message = "Please correct the errors below."
        detail = {"error": ["Invalid request"]}

    if isinstance(exc, serializers.ValidationError):
        message = "Please correct the errors below."
        detail = exc.detail

    if isinstance(exc, ValidationError):
        message = "Please correct the errors below."
        detail = {"error": str(exc)}

    if isinstance(exc, PermissionError):
        message = "Please correct the errors below."
        detail = {"error": ["Forbidden"]}

    if isinstance(exc, KeyError):
        message = "Please correct the errors below."
        detail = {exc.__str__(): ["This field is required."]}

    if isinstance(exc, (AuthenticationFailed, NotAuthenticated)):
        code = status.HTTP_401_UNAUTHORIZED
        message = "Please correct the errors below."
        if isinstance(exc, InvalidToken):
            detail = {"error": exc.detail}
        else:
            detail = {"error": exc.__str__()}

    result = {"status": {"code": code, "message": message, "detail": detail}}
    return Response(result, status=code)
