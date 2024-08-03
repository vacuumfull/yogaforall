from appeal.models import Appeal

def add(name, phone, email=None, content=None, service=None):
    obj = {
        "name": name,
        "phone": phone,
        "email": email,
        "content": content,
        "service": service
    }
    return Appeal.objects.create(**obj)