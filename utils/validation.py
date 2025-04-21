def validate_fields(data, field_list):
    """
    Validates if all required fields are present in the given data.

    :param data: Dictionary containing input data.
    :param field_list: List of required fields.
    :return: Dictionary containing error messages (if any).
    """
    if not isinstance(data, dict):
        return {"error": "Invalid data format, expected a dictionary."}

    errors = {}
    for key in field_list:
        if key not in data or data[key] is None or data[key] == "":
            errors[key] = f"{key} is required"

    return errors

def validate_required_fields(data, field_list):
    """
    Ensures that all specified fields are present and not None.

    :param data: Dictionary containing input data.
    :param field_list: List of required fields.
    :return: Dictionary containing missing field errors (if any).
    """
    errors = {}
    for key in field_list:
        if data.get(key) is None:
            errors[key] = f"{key} is required"

    return errors
