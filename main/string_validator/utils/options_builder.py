from main.shared.types import Options


def options_builder(options: Options | None, default_message: str) -> Options:
    new_options: Options = (options or {"error": default_message}).copy()
    new_options["error"] = new_options.get("error") or default_message

    return new_options
