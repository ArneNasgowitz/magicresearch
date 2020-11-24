from os import environ

# mturk environment
mturk_hit_settings = {
    'keywords': ['study','bonus'],
    'title': 'Academic study (1-2.5 USD for 15 min)',
    'description':'Do various tasks on economic behavior and earn between 1 and 2.5 USD, depending on your decisions',
    'template': 'global/MTurkPreview.html',
    'minutes_alotted_per_assignment': 60,
    'expiration_hours': 7*24, # a week, hopefully limit reached before!
    # requirements
    'grant_qualification_id': 'WCPSA2020XNOQR', # Prevent from taking the main study later
    'qualification_requirements': [
    # Only South Africa
        {
            'QualificationTypeId': "00000000000000000071",
            'Comparator': "EqualTo",
            'LocalValues': [{'Country':"ZA"}]
        },
        {
            'QualificationTypeId': "000000000000000000L0",
            'Comparator': "GreaterThanOrEqualTo",
            'IntegerValues': [95]
        },
    # So far no further requirements
    ]
}



SESSION_CONFIGS = [
    dict(
        name='AcademicStudy',
        display_name='Experiment',
        num_demo_participants=50,
        app_sequence=['intro','effortloop','questionnaire']
    )
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.125, participation_fee=1.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='testing',
        display_name='WC SA Testing',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

# don't share this with anybody.
SECRET_KEY = '=6n^jz=r1e5w6o@emim1*qq%1o%perxep!2ym#38@fgy*iu#3a'

INSTALLED_APPS = ['otree']
