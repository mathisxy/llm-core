from pydantic import BaseModel

class RichReprMixin(BaseModel):

    MAX_TOTAL_CHARS = 200

    def __rich_repr__(self):

        for name in self.__class__.model_fields:
            value = getattr(self, name)
            length = len(str(value))

            if length > self.MAX_TOTAL_CHARS:
                yield name, f"<object of length: {len(str(value))}>"
            else:
                yield name, value