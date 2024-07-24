from logging_config import log
import json


def build_requests_headers(access_token, content_type="application/json", **kwargs):
    """
    This function generates a dictionary to be used as headers for HTTP requests.
    It takes an access token and an optional content type (defaults to "application/json")
    as parameters, and also accepts any additional keyword arguments. The function constructs
    an "Authorization" field with a "Bearer" scheme using the provided access token, and a
    "Content-Type" field with the provided content type or overridden by kwargs if provided.
    """
    log.info("build request headers")
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": content_type
    }
    if "content_type" in kwargs:
        headers["Content-Type"] = kwargs["content_type"]

    log.debug(f"Request headers: {json.dumps(headers, indent=4)}")
    return headers

