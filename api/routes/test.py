from flask import Blueprint, jsonify, request, Response
from api import log
from api.logger import log
from api.schema import BaseSchema
from api.models import TestUser


test_blueprint = Blueprint("test", __name__, url_prefix="/test")


@test_blueprint.route("", methods=["GET"])
def tokenize() -> Response:
        # u = TestUser(username="test")
        log(log.INFO, "Successful tokenize")
        return jsonify(BaseSchema(status="success", message="Test)").model_dump()), 200
