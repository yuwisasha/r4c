import json

from django.core import serializers
from django.http import FileResponse, HttpRequest, HttpResponse, JsonResponse
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.csrf import csrf_exempt

from robots.models import Robot
from robots.reports import create_report


@require_POST
@csrf_exempt
def create_robot(request: HttpRequest) -> JsonResponse:
    """Create a Robot database instace by given JSON"""

    data = json.loads(request.body.decode("utf-8"))
    model = data.get("model")
    version = data.get("version")
    robot = Robot(serial=f"{model}-{version}", **data)
    robot.clean_fields()
    robot.save()
    serialized_robot = serializers.serialize("json", [robot])
    return JsonResponse(json.loads(serialized_robot)[0]["fields"])


@require_GET
@csrf_exempt
def get_report(request: HttpRequest) -> FileResponse:
    """Create a report on robots"""

    report = create_report()
    try:
        return FileResponse(open(report, "rb"))
    except FileNotFoundError:
        return HttpResponse("Report not found", status=404)
