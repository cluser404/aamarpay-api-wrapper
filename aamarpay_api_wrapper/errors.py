class AamarpayApiError(Exception):
    pass

class DuplicateTransactionIDError(AamarpayApiError):
    pass

class InvalidStoreIDError(AamarpayApiError):
    pass

class InvalidSignatureKeyError(AamarpayApiError):
    pass
