from sqlalchemy.types import TypeDecorator, TEXT
import json

class JSONB(TypeDecorator):
    impl = TEXT

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            from sqlalchemy.dialects.postgresql import JSONB
            return dialect.type_descriptor(JSONB())
        else:
            return dialect.type_descriptor(TEXT())

    def process_bind_param(self, value, dialect):
        if dialect.name == 'postgresql':
            return value
        if value is not None:
            return json.dumps(value)
        return value

    def process_result_value(self, value, dialect):
        if dialect.name == 'postgresql':
            return value
        if value is not None:
            return json.loads(value)
        return value

class ARRAY(TypeDecorator):
    impl = TEXT

    def load_dialect_impl(self, dialect):
        if dialect.name == 'postgresql':
            from sqlalchemy.dialects.postgresql import ARRAY
            return dialect.type_descriptor(ARRAY(self.item_type))
        else:
            return dialect.type_descriptor(TEXT())

    def process_bind_param(self, value, dialect):
        if dialect.name == 'postgresql':
            return value
        if value is not None:
            return ",".join(map(str, value))
        return value

    def process_result_value(self, value, dialect):
        if dialect.name == 'postgresql':
            return value
        if value is not None:
            return [self.item_type(x) for x in value.split(',')]
        return value

    def __init__(self, item_type):
        super(ARRAY, self).__init__()
        self.item_type = item_type


def import_all_models():
    """Import model modules that are registered through this package."""
    from app.models import seminal  # noqa: F401
