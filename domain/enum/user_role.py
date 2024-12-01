import enum


class UserRole(enum.Enum):
    GERENTE = "gerente"
    MESERO = "mesero"
    CAJERO = "cajero"
    SUPERVISOR = "supervisor"
    RECEPCIONISTA = "recepcionista"
    COCINERO = "cocinero"
    CLIENTE = "cliente"