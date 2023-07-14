# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class SalaryInformation(models.Model):
    _name = 'salary.information'
    _inherit = 'mail.thread',
    _description = 'Thông tin lương'

    name = fields.Many2one("employee.information", string='Họ và tên', required=True, tracking=True)
    Basic_Salary = fields.Float(string='Mức lương cơ bản', requests=True, tracking=True)
    Allowances_Incentive = fields.Float(string='Lương phụ cấp, thưởng thêm', tracking=True)

    department = fields.Char(string='Phòng làm việc', tracking=True)
    ref = fields.Char(string='Mã bản ghi', default=lambda self: _('Tạo thông tin mới'))

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals['ref'] = self.env['ir.sequence'].next_by_code('employee.information')
        return super(SalaryInformation, self).create(vals_list)


