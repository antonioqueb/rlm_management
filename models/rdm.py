from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class RdmSolicitud(models.Model):
    _name = 'rdm.solicitud'
    _description = 'Solicitud RDM'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'mail.activity']

    name = fields.Char(string='Folio del RDM', required=True, copy=False, index=True, default='Nuevo', readonly=True)
    fecha_solicitud = fields.Date(string='Fecha de Solicitud', default=fields.Date.context_today, required=True)
    fecha_requerida = fields.Date(string='Fecha Requerida', required=True)
    almacen_id = fields.Many2one('stock.warehouse', string='Almacén', required=True)
    solicitante_id = fields.Many2one('res.users', string='Solicitante', default=lambda self: self.env.user, required=True)
    autorizado = fields.Selection([('si', 'Sí'), ('no', 'No')], string='¿Está autorizado?', default='no', tracking=True)

    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('revision', 'En Revisión'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
        ('enviado_compras', 'Enviado a compras'),
        ('recibido', 'Recibido')],
        string='Estado del RDM', default='borrador', tracking=True)

    linea_ids = fields.One2many('rdm.solicitud.linea', 'solicitud_id', string='Líneas de solicitud', required=True)
    prioridad = fields.Selection([('baja', 'Baja'), ('media', 'Media'), ('alta', 'Alta')], string='Prioridad', default='media')
    fecha_critica = fields.Date(string='Fecha crítica (opcional)')
    autorizado_por_id = fields.Many2one('res.users', string='Autorizado por')
    comentario_autorizador = fields.Text(string='Comentario del Autorizador')
    metodo_surtido = fields.Selection([('stock', 'Stock'), ('compras', 'Compras')], string='Método de Surtido', required=True)
    justificacion = fields.Text(string='Justificación')
    archivo_adjunto = fields.Binary(string='Archivo Adjunto', attachment=True)

    @api.model
    def create(self, vals):
        if vals.get('name', 'Nuevo') == 'Nuevo':
            vals['name'] = self.env['ir.sequence'].next_by_code('rdm.solicitud') or 'Nuevo'
        return super(RdmSolicitud, self).create(vals)

class RdmSolicitudLinea(models.Model):
    _name = 'rdm.solicitud.linea'
    _description = 'Línea de solicitud RDM'

    solicitud_id = fields.Many2one('rdm.solicitud', string='Solicitud RDM', required=True)
    product_id = fields.Many2one('product.product', string='Producto Solicitado', required=True)
    cantidad_solicitada = fields.Float(string='Cantidad Solicitada', required=True)
    uom_id = fields.Many2one('uom.uom', string='Unidad de Medida', related='product_id.uom_id', readonly=True)
