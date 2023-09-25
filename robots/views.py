import json

from django.core import serializers
from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from .models import Robot


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
