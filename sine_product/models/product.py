# -*- coding: utf-8 -*-
##############################################################################
#
#   @ Sinergiainformatica.net  . David Hernández
#   2016
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api, exceptions


class ProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    short_description = fields.Char(string='Short Description', size=160)


ProductTemplate()
