class ProdutoInfoException(Exception):
    ...


class ProdutoInfoNotFoundError(ProdutoInfoException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Produto Info Not Found"


class ProdutoInfoInfoAlreadyExistError(ProdutoInfoException):
    def __init__(self):
        self.status_code = 409
        self.detail = "Produto Info Already Exists"