# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Human Resource Management',
    'author': 'Phạm Sỹ Quang',
    'version': '1.0',
    'sequence': 10,
    'category': '',
    'summary': '',
    'depends': ['mail'],
    'website': 'https://github.com/JohnsonAudreyRalph?tab=repositories',
    "description": "Đây là phần mềm quản lý nhân viên",
    'demo': [],
    'data': [
        'security/ir.model.access.csv',
        'views/Employee_Information.xml',
    ],
    'license': 'LGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False
}
