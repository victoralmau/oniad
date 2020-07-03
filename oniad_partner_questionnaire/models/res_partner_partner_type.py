# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from openerp import api, models, fields

class ResPartnerPartnerType(models.Model):
    _name = 'res.partner.partner.type'

    name = fields.Char(
        string="Nombre"
    )
    stakeholder = fields.Boolean(
        string="Stakeholder"
    )
    user = fields.Boolean(
        string="Usuario"
    ) 