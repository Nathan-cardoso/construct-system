from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    available_permissions = {
        'cadastrar_produtos': True,
        'liberar_descontos': True,
        'cadastrar_vendedores': True
    }


class Vendedor(AbstractUserRole):

    available_permissions = {
        'realizar_vendas': True
    }
