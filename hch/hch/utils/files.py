import json
from datetime import datetime
from typing import Any, Dict


def write_json(fp: str, data: Dict[str, Any]) -> None:

    def default_serializer(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        raise TypeError(f"Type {type(obj)} not serializable")

    with open(fp, "w") as f:
        json.dump(data, f, default=default_serializer, indent=4)

    print(f"Data successfully written to {fp}")