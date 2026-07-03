from django.http import HttpRequest


def get_guest_id(request: HttpRequest):
    guest_id = request.session.session_key
    if guest_id is None:
        request.session.create()
        guest_id = request.session.session_key
    return guest_id
