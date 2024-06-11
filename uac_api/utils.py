import json, re
import requests
import os
from datetime import datetime

def append_if_not_none(list_name, variable, format, exclude_empty=True):
    if "{}" in format:
        format = format.replace("{}", "{var}")

    if variable is not None:
        if exclude_empty: # we don't want empty records
            if len(variable) == 0:
                return
        _value = format.format(var=requests.utils.quote(variable, safe='()'))
        list_name.append(_value)


def set_if_not_none(_dict, field, value, format="{}", exclude_empty=True):
    if value is None:
        return
    
    if exclude_empty: # we don't want empty records
        if len(value) == 0:
            return
    set_if_not_equal(_dict, field, value, None, format=format)


def set_if_not_equal(_dict, field, value, default, format="{}"):
    if value != default:
        if "{}" in format:
            format = format.replace("{}", "{var}")
        _value = format.format(var=value)

        _dict[field] = _value


def format_json(json_obj):
    json_string = json.dumps(json_obj, indent=4, sort_keys=True)
    json_string = re.sub(r"\n\s*\{", " {", json_string)
    json_string = re.sub(r"\n\s*\]", " ]", json_string)
    json_string = re.sub(r"\[\],", "[ ],", json_string)
    json_string = re.sub(r"\":(\s*[^\n]+)", "\" :\\1", json_string)
    return json_string


def strip_url(url):
    return url.strip('/').strip(' ')


def get_first_element(_list, default=None):
    if len(_list) == 0:
        return default
    else:
        return _list[0]


def is_xml(response):
    content_type = response.headers.get("Content-Type")
    if content_type is None:
        return False
    return "xml" in content_type


def is_json(response):
    content_type = response.headers.get("Content-Type")
    if content_type is None:
        return False
    return "json" in content_type

def remove_sysid_tag(json_structure):
    """Removes the "sysId" tag from all list objects in a JSON structure.

    Args:
        json_structure: The JSON structure to be modified.

    Returns:
        The modified JSON structure.
    """

    for list_object in json_structure["actions"].values():
        if isinstance(list_object, list):
            for list_object_item in list_object:
                if isinstance(list_object_item, dict) and "sysId" in list_object_item:
                    del list_object_item["sysId"]
    
    return json_structure

def convert_to_variable_name(string):
    """Converts a string to a Python variable name format.

    Args:
        string: The string to be converted.

    Returns:
        A string in Python variable name format.
    """

    # Remove all spaces and special characters.
    string = re.sub(r"[^\w]", "_", string)

    # Make the first character lowercase.
    string = string[0].lower() + string[1:]

    return string


def snake_to_camel(snake_case_str):
    """Converts a snake_case string to camelCase.

    Args:
        snake_case_str: The string in snake_case format.

    Returns:
        The converted string in camelCase format.
    """
    components = snake_case_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])
    
def prepare_payload(payload, field_mapping, args):
    _payload = None
    if payload is not None:
        _payload = payload
    else:
        _payload = { }
    
    # Process additional arguments (**args)
    for arg_key, arg_value in args.items():
        if arg_key in field_mapping:
            _payload[field_mapping[arg_key]] = arg_value
        elif snake_to_camel(arg_key) in field_mapping:
            _payload[field_mapping[snake_to_camel(arg_key)]] = arg_value
        else:
            for key, value in field_mapping.items():
                if key.lower() == snake_to_camel(arg_key).lower():
                    _payload[key] = arg_value
    return _payload

def prepare_query_params(query, field_mapping, args):
    if query is not None:
        parameters = query
    else:
        parameters = []
        
        for field, var in args.items():
            if field in field_mapping:
                append_if_not_none(parameters, var, field_mapping[field] + "={var}")
            elif snake_to_camel(field) in field_mapping:
                append_if_not_none(parameters, var, field_mapping[snake_to_camel(field)] + "={var}")
            else:
                for key, value in field_mapping.items():
                    if key.lower() == snake_to_camel(field).lower():
                        append_if_not_none(parameters, var, key + "={var}")
        
    return parameters

def prepare_query_payload(query, query_fields, payload, payload_fields, args):
    _query = prepare_query_params(query, query_fields, args)
    _payload = prepare_payload(payload, payload_fields, args)
    return _query, _payload

def safe_str_to_int(s):
    """
    Attempts to convert a string to an integer safely. This version also handles
    strings containing '.' or ',' by removing these characters before conversion,
    assuming they are used as decimal points or thousand separators.

    Parameters:
    - s (str): The string to convert.

    Returns:
    - int: The integer value of the string if conversion is successful.
    - None: If the string cannot be converted to an integer.
    """
    # Remove thousand separators (commas)
    s = s.replace(',', '')
    # Handle decimal points by splitting and taking the integer part
    if '.' in s:
        s = s.split('.')[0]
    try:
        return int(s)
    except ValueError:
        # Return None or handle the error as needed
        return None
    
def filter_secrets(output, secrets, placeholder='***'):
    """
    Replaces occurrences of secrets within the output string with a placeholder.
    
    :param output: The output string that may contain secrets.
    :param secrets: A list of secret strings to be filtered out.
    :param placeholder: The placeholder text to replace secrets with. Defaults to '<secret>'.
    :return: The output string with secrets replaced by the placeholder.
    """
    for secret in secrets:
        if secret in output:
            output = output.replace(secret, placeholder)
    return output

    