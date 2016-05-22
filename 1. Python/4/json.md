# JSON

[JavaScript Object Notation](http://www.json.org/) (JSON, pronounced like “Jason” not "Jaysawn") started out as a way of describing structured data within (not surprisingly) JavaScript. It has become the default way to share data within and between programs in most programming languages common to web development.

## What’s so great about JSON?

1. JSON allows you to make strings out of complex data structures (called ‘serialization’). This allows you to save data to a hard drive or send it over a network.
1. JSON strings are encoded in a standard way, so you can read in (‘deserialize’) a JSON string that was generated in any other programming language or environment.
1. JSON is way easier to read for humans and almost always more terse than older formats that were usually based on XML (e.g., [SOAP](http://www.tutorialspoint.com/soap/soap_examples.htm)).

## How is JSON structured?

The top level of any JSON object is always either a `list` or `dict` (an array or associative array in JavaScript). The top level object can contain any of the following Python types (listed here with their JSON equivalents):

    | Python      | JSON   |
    ------------------------
    | dict        | object |
    | list, tuple | array  |
    | str         | string |
    | int, float  | number |
    | True        | true   |
    | False       | false  |
    | None        | null   |

The following is an example of a simple JSON string:

    '{"foo": ["bar", "baz"], "quux": true, "qux": null}'

Python includes convenience methods for encoding (serializing) and decoding (deserializing) JSON in the `json` module.

Example:

    import json
    
    my_json_string = json.dumps({"foo": ["bar", "baz"], 'qux': None, 'quux': True})
    my_json_string  # > '{"foo": ["bar", "baz"], "quux": true, "qux": null}'
    
    my_obj = json.loads(my_json_string)
    my_obj  # > {'foo': ['bar', 'baz'], 'qux': None, 'quux': True}

Note: The order of dictionary keys is not guaranteed, so if you want to unit test results from the JSON encoding method, pass `sort_keys=True` to `json.dumps` to ensure keys are returned in alphabetical order.

Example:

    import json
    
    no_guaranteed_order = json.dumps({"c":3, "a":1, "b": 2})
    no_guaranteed_order  # > '{"c": 3, "a": 1, "b": 2}'
    
    alpha_order = json.dumps({"c":3, "a":1, "b": 2}, sort_keys=True)
    alpha_order  # > '{"a": 1, "b": 2, "c": 3}'

You can read more about [Python’s built-in JSON methods](https://docs.python.org/3/library/json.html) in the documentation.