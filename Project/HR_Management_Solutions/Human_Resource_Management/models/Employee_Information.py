# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class EmployeeInformation(models.Model):
    _name = 'employee.information'
    _inherit = 'mail.thread',
    _description = 'Thông tin nhân viên'

    name = fields.Char(string='Họ và tên', required=True, tracking=True)
    age = fields.Integer(string='Tuổi', required=True, tracking=True)
    gender = fields.Selection([('Male', 'Nam'), ('Female', 'Nữ'), ('Others', 'Khác')], string='Giới tính', required=True, tracking=True)
    address = fields.Text(string='Địa chỉ', required=True, tracking=True)
    date = fields.Date(string='Ngày sinh', required=True, tracking=True)
    email = fields.Char(string='Email', required=True, tracking=True)
    phone = fields.Char(string='Số điện thoại', required=True, tracking=True)
    job_position = fields.Char(string='Vị trí công việc', tracking=True)
    department = fields.Char(string='Phòng làm việc', tracking=True)
    salary = fields.Float(string='Mức lương hiện tại', tracking=True)
    education_level = fields.Char(string='Trình độ học vấn', tracking=True)
    marital_status = fields.Boolean(string='Tình trạng hôn nhân', default=False, tracking=True)

    @api.constrains('email')
    def _validate_email(self):
        for record in self:
            if record.email and '@' not in record.email:
                raise ValidationError("Địa chỉ email không hợp lệ!")

