from src.core.auth.schema.token_decode import TokenDecode

class TokenMapper:
    @staticmethod
    def parseToTokenDecode(token: dict) -> TokenDecode:
        return TokenDecode(
            type = token.get("tyoe"),
            exp = token.get("exp"),
            iat = token.get("iat"),
            sub = token.get("sub")
        )