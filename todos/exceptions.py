from django.http import Http404
from rest_framework import status
from rest_framework.exceptions import NotFound, ParseError, ValidationError
from rest_framework.response import Response
from rest_framework.views import exception_handler as default_exception_handler


def _first_message(detail):
    """Flatten a DRF error detail (dict, list or string) into one line."""
    if isinstance(detail, dict):
        for field, messages in detail.items():
            message = _first_message(messages)
            if field == "non_field_errors":
                return message
            return f"{field}: {message}"
        return "invalid"
    if isinstance(detail, (list, tuple)):
        return _first_message(detail[0]) if detail else "invalid"
    return str(detail)


def todos_exception_handler(exc, context):
    if isinstance(exc, ValidationError):
        return Response({"error": _first_message(exc.detail)}, status=status.HTTP_400_BAD_REQUEST)
    if isinstance(exc, (NotFound, Http404)):
        return Response({"error": "not found"}, status=status.HTTP_404_NOT_FOUND)
    if isinstance(exc, ParseError):
        return Response({"error": "invalid json"}, status=status.HTTP_400_BAD_REQUEST)

    response = default_exception_handler(exc, context)
    if response is not None and hasattr(exc, "detail"):
        response.data = {"error": _first_message(exc.detail)}
    return response
