from flask_admin.contrib.sqla import ModelView
from flask_admin import expose


class UserView(ModelView):
        can_delete = False  # disable model deletion
        can_create = False
        can_edit = False
        can_view_details = True
        column_searchable_list = ['username', 'email']
        inline_models = []

        details_template = 'detail.html'

        @expose('/details/', methods=('GET', 'POST'))
        def details_view(self):
                self._template_args['image_src'] = "images/upload/songoku.png"
                return super(UserView, self).details_view()