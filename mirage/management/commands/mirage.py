from django.core.management.base import BaseCommand

from mirage.tools import Migrator


class Command(BaseCommand):
    help = "encrypt/decrypt data use Mirage ~"

    def add_arguments(self, parser):
        parser.add_argument("--app", type=str, required=True)
        parser.add_argument("--model", type=str, required=True)
        parser.add_argument("--field", type=str, required=True)
        parser.add_argument("--method", type=str, required=True)
        parser.add_argument("--offset", type=int, required=False)
        parser.add_argument("--total", type=int, required=False)
        parser.add_argument("--limit", type=int, required=False)
        parser.add_argument("--tofield", type=str, required=False)
        parser.add_argument("--idfield", type=str, required=False)

    def handle(self, *args, **options):
        app = options["app"]
        model = options["model"]
        field = options["field"]
        method = options["method"]
        offset = options["offset"] or 0
        total = options["total"]
        limit = options["limit"] or 1000
        tofield = options["tofield"]
        idfield = options["idfield"] or "id"

        if method == "encrypt":
            Migrator(app, model, field, idfield=idfield).encrypt(
                offset=offset, total=total, limit=limit
            )
        elif method == "decrypt":
            Migrator(app, model, field, idfield=idfield).decrypt(
                offset=offset, total=total, limit=limit
            )
        elif method == "copy_to":
            assert tofield is not None
            Migrator(app, model, field, tofield=tofield, idfield=idfield).copy_to(
                offset=offset, total=total, limit=limit
            )
        elif method == "decrypt_to":
            assert tofield is not None
            Migrator(app, model, field, tofield=tofield, idfield=idfield).decrypt_to(
                offset=offset, total=total, limit=limit
            )
        elif method == "encrypt_to":
            assert tofield is not None
            Migrator(app, model, field, tofield=tofield, idfield=idfield).encrypt_to(
                offset=offset, total=total, limit=limit
            )
        else:
            return
