{
    'SAST': {
        'required': False,
        'type': 'dict',
        'schema': {
            'sonarqube': {
                'required': False,
                'type': 'dict',
                'schema': {
                    'repo': {
                        'required': True,
                        'type': 'dict',
                    },
                    'SONAR_HOST_URL': {
                        'type': 'dict',
                        'required': True,

                    },
                    'SONAR_PROJECT_KEY': {
                        'type': 'dict',
                        'required': True,

                    },
                },
            },
        },

        'DAST': {
            'required': False,
            'type': 'dict',
            'schema': {
                'zap': {
                    'required': False,
                    'type': 'dict',
                    'schema': {
                        'repo': {
                            'required': True,
                            'type': 'dict',
                        },
                        'typeofscan': {
                            'type': 'dict',
                            'required': True,

                        },
                        'target': {
                            'type': 'dict',
                            'required': True,

                        },
                        'format': {
                            'type': 'string',
                            'required': True,

                        },
                        'options': {
                            'type': 'string',
                            'required': True,

                        },
                    },
                },
            },
        },
        'Tekton-build-and-push': {
            'required': False,
            'type': 'dict',
            'schema': {
                'docker': {
                    'required': True,
                    'type': 'dict',
                    'schema': {
                        'repo': {
                            'required': True,
                            'type': 'dict',
                        },
                        'docker_username': {
                            'type': 'string',
                            'required': True,
                        },
                        'image_name': {
                            'type':'dict',
                            'required': True,
                        },
                        'revision': {
                            'type': 'string',
                            'required': True,
                        },
                        'url': {
                            'type': 'dict',
                            'required': True,
                        },
                             },
                         },
                },
        },
    },
}
