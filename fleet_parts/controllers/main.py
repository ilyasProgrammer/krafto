# -*- coding: utf-8 -*-

from odoo import http
from collections import deque
import json
from odoo.http import request
from odoo.tools import ustr
from odoo.tools.misc import xlwt


class FleetPartsAPI(http.Controller):

    @http.route('/web/load_part', type='json', auth='none')
    def load_part(self, uid, db, vehicle_id, vin, data):
        print 'OK VERY GOOD'
