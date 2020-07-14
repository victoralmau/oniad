# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Survey Oniad',
    'version': '12.0.1.0.0',    
    'author': 'Odoo Nodriza Tech (ONT)',
    'website': 'https://nodrizatech.com/',
    'category': 'Tools',
    'license': 'AGPL-3',
    'depends': ['base', 'ont_base_survey', 'oniad_root', 'crm', 'crm_oniad', 'survey'],
    'data': [
        'views/survey_user_input.xml',
        'views/survey_survey.xml',
    ],        
    'installable': True,
    'auto_install': False,    
}