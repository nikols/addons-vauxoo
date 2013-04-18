#!/usr/bin/python
# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) OpenERP Venezuela (<http://openerp.com.ve>).
#    All Rights Reserved
# Credits######################################################
#    Coded by: Vauxoo C.A.
#    Planified by: Nhomar Hernandez
#    Audited by: Vauxoo C.A.
#############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
##########################################################################

import time
from openerp.osv import osv, fields
import decimal_precision as dp
from openerp.tools.translate import _

import openerp.netsvc as netsvc


class account_invoice(osv.Model):
    _inherit = 'account.invoice'

    _columns = {
        'cancel_true': fields.boolean('Invoice Cancel', help="Field that indicates whether the invoice was canceled earlier, to generate actions automatically")

    }

    _defaults = {
        'cancel_true': False,

    }

    def invoice_cancel(self, cr, uid, ids, context=None):

        if context is None:
            context = {}
        wizard_obj = self.pool.get('account.move.cancel')
        wizard_obj.cancel_account_move(
            cr, uid, ids, context=context, invoice_ids=ids)

        return True
