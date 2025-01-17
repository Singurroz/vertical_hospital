# -*- coding: utf-8 -*-
{
    'name': "vertical_hospital",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail','utm'],

    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        "views/paciente_view.xml",
        "views/treatment_management_view.xml",
        "views/vertical_hospital_menus.xml",
        "report/patient_management_report.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
