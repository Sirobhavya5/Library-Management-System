from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, phone_number, password, role, street, city, state, zip_code):
        if not first_name:
            raise ValueError("Users must have an first_name. ")
        if not last_name:
            raise ValueError("Users must have an last_name. ")
        if not email:
            raise ValueError("Users must have an email address. ")
        if not phone_number:
            raise ValueError("Users must have a phone number. ")
        if not street:
            raise ValueError("Users must have a complete address. ")
        if not city:
            raise ValueError("Users must have a complete address. ")
        if not state:
            raise ValueError("Users must have a complete address. ")
        if not zip_code:
            raise ValueError("Users must have a complete address. ")
        if not password:
            raise ValueError("Users must set a password. ")
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            street=street,
            city=city,
            state=state,
            zip_code=zip_code,
            role=role,
            is_admin=False
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, phone_number, password, role, street, city, state, zip_code):
        if not first_name:
            raise ValueError("Users must have an first_name. ")
        if not last_name:
            raise ValueError("Users must have an last_name. ")
        if not email:
            raise ValueError("Users must have an email address. ")
        if not phone_number:
            raise ValueError("Users must have a phone number. ")
        if not street:
            raise ValueError("Users must have a complete address. ")
        if not city:
            raise ValueError("Users must have a complete address. ")
        if not state:
            raise ValueError("Users must have a complete address. ")
        if not zip_code:
            raise ValueError("Users must have a complete address. ")
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            street=street,
            city=city,
            state=state,
            zip_code=zip_code,
            role=role,
            is_admin=True
        )
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_admin=True
        )
        user.set_password(password)
        user.save(using=self._db)
        return user