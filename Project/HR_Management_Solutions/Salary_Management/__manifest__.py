# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Salary Management',
    'author': 'Phạm Sỹ Quang',
    'version': '1.0',
    'sequence': 11,
    'category': '',
    'summary': '',
    'depends': ['mail'],
    'website': 'https://github.com/JohnsonAudreyRalph?tab=repositories',
    "description": "Phần mềm quản lý tiền lương",
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'data/sequences.xml',
        'views/Salary_Information.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False
}
