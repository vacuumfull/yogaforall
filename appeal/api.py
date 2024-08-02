from appeal.models import Appeal

def add(name, phone, email=None, content=None):
    obj = {
        "name": name,
        "phone": phone,
        "email": email,
        "content": content,
    }
    return Appeal.objects.create(**obj)