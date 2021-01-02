# -*- coding: utf-8 -*-

from odoo import models, fields, api

duration = fields.Float(digits=(6, 2), help="Duration in days")
seats = fields.Integer(string="Number of seats")

instructor_id = fields.Many2one('res.partner', string="Instructor",
    domain=[('instructor', '=', True)])

course_id = fields.Many2one('openacademy.course',
        ondelete='cascade', string="Course", required=True)
attendee_ids = fields.Many2many('res.partner', string="Attendees")

    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')

@api.depends('seats', 'attendee_ids')
def _taken_seats(self):
    for r in self:
        if not r.seats:
            r.taken_seats = 0.0
        else:
            r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats


_description = "OpenAcademy Sessions"

name = fields.Char(required=True)
start_date = fields.Date(default=fields.Date.today)
active = fields.Boolean(default=True)


class MinimalModel(models.Model):
    _name = 'test.model'


class LessMinimalModel(models.Model):
    _name = 'test.model2'

    name = fields.Char()


class openacademy(models.Model):
    _name = 'openacademy.openacademy'

    name = fields.Char()