from odoo.exceptions import AccessError
from odoo.tests.common import SavepointCase


class TestPurchaseAccess(SavepointCase):

    @classmethod
    def setUpClass(cls):
        super(TestPurchaseAccess, cls).setUpClass()
        cls.purchase_user = cls.env['res.users'].with_context(
            no_reset_password=True).create({
                'name': 'Purchase without Forms',
                'login': 'formio_purchase_access_test',
                'groups_id': [(6, 0, [
                    cls.env.ref('purchase.group_purchase_user').id,
                ])],
            })
        cls.partner = cls.env['res.partner'].create({
            'name': 'Forms Purchase Test Vendor',
        })
        cls.orders = cls.env['purchase.order']
        for name in ('Forms Purchase A', 'Forms Purchase B'):
            cls.orders |= cls.env['purchase.order'].create({
                'name': name,
                'partner_id': cls.partner.id,
            })
        cls.builder = cls.env['formio.builder'].create({
            'name': 'purchase_access_test',
            'title': 'Purchase Access Test',
            'formio_version_id': cls.env.ref('formio.version_4_9_23').id,
            'formio_res_model_id': cls.env.ref(
                'formio_purchase.formio_res_model_purchase_order').id,
            'schema': '{"components": []}',
        })

    def _create_form(self, order):
        return self.env['formio.form'].with_context(
            active_model='purchase.order', active_id=order.id).create({
                'builder_id': self.builder.id,
                'title': 'Purchase Access Test',
                'user_id': self.purchase_user.id,
            })

    def test_read_orders_without_forms_access(self):
        self._create_form(self.orders[0])
        orders = self.orders.sudo(user=self.purchase_user)
        self.assertFalse(self.env['formio.form'].sudo(
            user=self.purchase_user).check_access_rights(
                'read', raise_exception=False))
        values = orders.read()
        self.assertEqual(len(values), 2)
        for value in values:
            self.assertNotIn('formio_forms', value)
            self.assertNotIn('formio_forms_count', value)
            self.assertEqual(
                value['formio_this_model_id'][0],
                self.env.ref('purchase.model_purchase_order').id)
        for field in ('formio_forms', 'formio_forms_count'):
            with self.assertRaises(AccessError):
                orders.read([field])
        with self.assertRaises(AccessError):
            self.env['formio.form'].sudo(
                user=self.purchase_user).search([])

    def test_write_orders_without_forms_access(self):
        form = self._create_form(self.orders[0])
        original_name = form.res_name
        self.orders.sudo(user=self.purchase_user).write({
            'notes': 'Updated by purchase user',
        })
        self.assertEqual(form.res_name, original_name)
        self.assertEqual(
            self.orders.mapped('notes'),
            ['Updated by purchase user', 'Updated by purchase user'])

    def test_rename_orders_without_forms_access(self):
        forms = self.env['formio.form']
        for order in self.orders:
            forms |= self._create_form(order)
        self.orders.sudo(user=self.purchase_user).write({
            'name': 'Renamed Purchase',
        })
        self.assertEqual(
            forms.mapped('res_name'),
            ['Renamed Purchase', 'Renamed Purchase'])
        with self.assertRaises(AccessError):
            forms.sudo(user=self.purchase_user).read(['res_name'])

    def test_forms_user_can_read_form_fields(self):
        form = self._create_form(self.orders[0])
        self.purchase_user.write({
            'groups_id': [(4, self.env.ref('formio.group_formio_user').id)],
        })
        values = self.orders[0].sudo(user=self.purchase_user).read([
            'formio_forms', 'formio_forms_count',
        ])[0]
        self.assertEqual(values['formio_forms'], form.ids)
        self.assertEqual(values['formio_forms_count'], 1)
