from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailBackend(ModelBackend):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print("EmailBackend foi inicializado")  

    def authenticate(self, request, email=None , password=None, **kwargs):
        print("Método authenticate chamado com:", request, password, kwargs) 
        email = email or kwargs.get('email')
        
        if email is None:
            return None
        try:
            user = User.objects.get(email=email)
            print("Usuário encontrado:", user)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
        return None
