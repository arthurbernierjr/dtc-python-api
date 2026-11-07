from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET
from rest_framework import permissions, viewsets

from .models import Todo
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by("id")
    serializer_class = TodoSerializer
    permission_classes = [permissions.AllowAny]


@require_GET
def health(request):
    return JsonResponse({"ok": True})


HOME_HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Todos</title>
<style>
  body { margin: 0; padding: 48px 24px; background: #08080A; color: #EAE6E1;
         font-family: system-ui, -apple-system, "Segoe UI", sans-serif; line-height: 1.5; }
  main { max-width: 640px; margin: 0 auto; }
  .stack { color: #8A8A94; font-size: 14px; letter-spacing: 0.04em; text-transform: uppercase; }
  h1 { font-size: 40px; margin: 8px 0 16px; }
  code { color: #E8D800; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
  a { color: #2FD48F; }
</style>
</head>
<body>
<main>
  <p class="stack">Python &middot; Django REST framework</p>
  <h1>Todos</h1>
  <p>JSON lives at <code>/todos</code></p>
  <p><a href="https://github.com/arthurbernierjr/dtc-python-api">Source on GitHub</a></p>
</main>
</body>
</html>
"""


@require_GET
def home(request):
    return HttpResponse(HOME_HTML, content_type="text/html; charset=utf-8")
