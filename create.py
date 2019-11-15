import json

config = json.loads(
"""
{
    "global": {
        "check_for_updates_on_startup": true,
        "show_in_menu_bar": true,
        "show_profile_name_in_menu_bar": true
    },
    "profiles": [
        {
            "complex_modifications": {
                "parameters": {
                    "basic.simultaneous_threshold_milliseconds": 50,
                    "basic.to_delayed_action_delay_milliseconds": 500,
                    "basic.to_if_alone_timeout_milliseconds": 1000,
                    "basic.to_if_held_down_threshold_milliseconds": 500,
                    "mouse_motion_to_scroll.speed": 100
                },
                "rules": [
                    {
                        "description": "CapsLock to Hyper/Escape",
                        "manipulators": [
                            {
                                "from": {
                                    "key_code": "caps_lock",
                                    "modifiers": {
                                        "optional": [
                                            "any"
                                        ]
                                    }
                                },
                                "to": [
                                    {
                                        "key_code": "right_shift",
                                        "modifiers": [
                                            "right_command",
                                            "right_control",
                                            "right_option"
                                        ]
                                    }
                                ],
                                "to_if_alone": [
                                    {
                                        "key_code": "escape"
                                    }
                                ],
                                "type": "basic"
                            }
                        ]
                    }
                ]
            },
            "devices": [
                {
                    "disable_built_in_keyboard_if_exists": false,
                    "fn_function_keys": [],
                    "identifiers": {
                        "is_keyboard": true,
                        "is_pointing_device": false,
                        "product_id": 1957,
                        "vendor_id": 1118
                    },
                    "ignore": false,
                    "manipulate_caps_lock_led": false,
                    "simple_modifications": [
                        {
                            "from": {
                                "key_code": "left_command"
                            },
                            "to": {
                                "key_code": "left_option"
                            }
                        },
                        {
                            "from": {
                                "key_code": "left_option"
                            },
                            "to": {
                                "key_code": "left_command"
                            }
                        }
                    ]
                },
                {
                    "disable_built_in_keyboard_if_exists": false,
                    "fn_function_keys": [],
                    "identifiers": {
                        "is_keyboard": true,
                        "is_pointing_device": false,
                        "product_id": 2071,
                        "vendor_id": 1118
                    },
                    "ignore": false,
                    "manipulate_caps_lock_led": false,
                    "simple_modifications": [
                        {
                            "from": {
                                "key_code": "left_command"
                            },
                            "to": {
                                "key_code": "left_option"
                            }
                        },
                        {
                            "from": {
                                "key_code": "left_option"
                            },
                            "to": {
                                "key_code": "left_command"
                            }
                        }
                    ]
                },
                {
                    "disable_built_in_keyboard_if_exists": false,
                    "fn_function_keys": [],
                    "identifiers": {
                        "is_keyboard": true,
                        "is_pointing_device": false,
                        "product_id": 628,
                        "vendor_id": 1452
                    },
                    "ignore": false,
                    "manipulate_caps_lock_led": true,
                    "simple_modifications": []
                },
                {
                    "disable_built_in_keyboard_if_exists": false,
                    "fn_function_keys": [],
                    "identifiers": {
                        "is_keyboard": true,
                        "is_pointing_device": false,
                        "product_id": 87,
                        "vendor_id": 9494
                    },
                    "ignore": false,
                    "manipulate_caps_lock_led": false,
                    "simple_modifications": []
                }
            ],
            "fn_function_keys": [
                {
                    "from": {
                        "key_code": "f1"
                    },
                    "to": {
                        "consumer_key_code": "display_brightness_decrement"
                    }
                },
                {
                    "from": {
                        "key_code": "f2"
                    },
                    "to": {
                        "consumer_key_code": "display_brightness_increment"
                    }
                },
                {
                    "from": {
                        "key_code": "f3"
                    },
                    "to": {
                        "key_code": "mission_control"
                    }
                },
                {
                    "from": {
                        "key_code": "f4"
                    },
                    "to": {
                        "key_code": "launchpad"
                    }
                },
                {
                    "from": {
                        "key_code": "f5"
                    },
                    "to": {
                        "key_code": "illumination_decrement"
                    }
                },
                {
                    "from": {
                        "key_code": "f6"
                    },
                    "to": {
                        "key_code": "illumination_increment"
                    }
                },
                {
                    "from": {
                        "key_code": "f7"
                    },
                    "to": {
                        "consumer_key_code": "rewind"
                    }
                },
                {
                    "from": {
                        "key_code": "f8"
                    },
                    "to": {
                        "consumer_key_code": "play_or_pause"
                    }
                },
                {
                    "from": {
                        "key_code": "f9"
                    },
                    "to": {
                        "consumer_key_code": "fastforward"
                    }
                },
                {
                    "from": {
                        "key_code": "f10"
                    },
                    "to": {
                        "consumer_key_code": "mute"
                    }
                },
                {
                    "from": {
                        "key_code": "f11"
                    },
                    "to": {
                        "consumer_key_code": "volume_decrement"
                    }
                },
                {
                    "from": {
                        "key_code": "f12"
                    },
                    "to": {
                        "consumer_key_code": "volume_increment"
                    }
                }
            ],
            "name": "Carter",
            "parameters": {
                "delay_milliseconds_before_open_device": 1000
            },
            "selected": true,
            "simple_modifications": [],
            "virtual_hid_keyboard": {
                "country_code": 0,
                "mouse_key_xy_scale": 100
            }
        }
    ]
}
"""
)

HYPER_LAYER_1 = [
    "right_command",
    "right_shift",
    "right_option",
    "right_control"
]

HYPER_LAYER_2 = [
    "left_command",
    "right_command",
    "right_shift",
    "right_option",
    "right_control"
]

HYPER_LAYER_3 = [
    "left_option",
    "right_command",
    "right_shift",
    "right_option",
    "right_control"
]

KEY_ABBREVIATIONS = {
    "rcmd": "right_command",
    "lcmd": "left_command",
    "ropt": "right_option",
    "lopt": "left_option",
    "rctrl": "right_control",
    "lctrl": "left_control",
    "rshift": "right_shift",
    "lshift": "left_shift",
    "fn": "fn",
    "1yper": HYPER_LAYER_1,
    "2yper": HYPER_LAYER_2,
    "3yper": HYPER_LAYER_3
}

def add_rule(mapping):
    mapping = mapping.strip().split("::")
    mapping[0] = mapping[0].split(" ")
    mapping[1] = mapping[1].split("|")
    if mapping[1][0] == 'code':
        mapping[1][1] = mapping[1][1].split(",")
        template = """
        {
            "from": {
                "key_code": "%s",
                "modifiers": {
                    "mandatory": [
                    ]
                }
            },
            "to": [
                {
                    "key_code": "%s",
                    "modifiers": [
                    ]
                }
            ],
            "type": "basic"
        }
        """ % (mapping[0][1],mapping[1][1][0])
        template = json.loads(template)

        for modifier in KEY_ABBREVIATIONS[mapping[0][0]]:
            template['from']['modifiers']['mandatory'].append(modifier)

        for modifier in mapping[1][1][1:]:
            template['to'][0]['modifiers'].append(KEY_ABBREVIATIONS[modifier])

        return template

    if mapping[1][0] == 'shell':
        template = """
        {
            "from": {
                "key_code": "%s",
                "modifiers": {
                    "mandatory": [
                    ]
                }
            },
            "to": [
                {
                    "shell_command": "%s"
                }
            ],
            "type": "basic"
        }
        """ % (mapping[0][1],mapping[1][1])
        template = json.loads(template)

        for modifier in KEY_ABBREVIATIONS[mapping[0][0]]:
            template['from']['modifiers']['mandatory'].append(modifier)

        return template

with open("mappings.txt", 'r') as mappings_file:
    mappings = [mapping.rstrip() for mapping in mappings_file.readlines() if mapping[0].rstrip() not in ("#", None, "")]
    for index, mapping in enumerate(mappings):
        mapping = mapping.rstrip()
        if mapping[0] is not "#" and mapping is not None:
            config['profiles'][0]['complex_modifications']['rules'][0]['manipulators'].append(add_rule(mapping))

with open("../../../.config/karabiner/karabiner.json", "r") as config_file:
    with open("karabiner_backup.json", "w") as backup_file:
        backup_file.writelines(config_file.readlines())

with open("../../../.config/karabiner/karabiner.json", "w") as config_file:
    config_file.write(json.dumps(config, indent=4))

