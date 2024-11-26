import enum


class UserRole(enum.Enum):
    GERENTE = "gerente"
    MESERO = "mesero"
    CAJERO = "cajero"
    SUPERVISOR = "supervisor"
    COCINERO = "cocinero"
    CLIENTE = "cliente"