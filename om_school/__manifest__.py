# -*- coding: utf-8 -*-
{
    'name': "School Management",
    'version': '13.0.1.0.0',
    'category': 'Extra Tools',
    'author': 'Odoo Mates',
    'website': 'odoomates.com',
    #'license': 'AGPL-3',
    'summary': 'School Management Software',
    'sequence': 15,
    'description': """
        Open Academy module for managing trainings:
            - training courses
            - training sessions
            - attendees registration
    """,
    'depends': ['base','mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/student.xml',
    ],
    # only loaded in demonstration mode
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False
}