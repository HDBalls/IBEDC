import werkzeug
import werkzeug.exceptions
import werkzeug.utils
import werkzeug.wrappers
import werkzeug.wsgi
from collections import OrderedDict, defaultdict, Counter
from werkzeug.urls import url_encode, url_decode, iri_to_uri
from lxml import etree
import unicodedata
import odoo.addons.web.controllers.main as main

from ..utilitymethods.utility import Encryption
import odoo
import odoo.modules.registry
from odoo.tools.mimetypes import guess_mimetype
from odoo.tools.translate import _
from odoo import http
from odoo.http import content_disposition, dispatch_rpc, request, serialize_exception as _serialize_exception, Response


# def ensure_db(redirect='/web/database/selector'):
#     # This helper should be used in web client auth="none" routes
#     # if those routes needs a db to work with.
#     # If the heuristics does not find any database, then the users will be
#     # redirected to db selector or any url specified by `redirect` argument.
#     # If the db is taken out of a query parameter, it will be checked against
#     # `http.db_filter()` in order to ensure it's legit and thus avoid db
#     # forgering that could lead to xss attacks.
#     db = request.params.get('db') and request.params.get('db').strip()

#     # Ensure db is legit
#     if db and db not in http.db_filter([db]):
#         db = None

#     if db and not request.session.db:
#         # User asked a specific database on a new session.
#         # That mean the nodb router has been used to find the route
#         # Depending on installed module in the database, the rendering of the page
#         # may depend on data injected by the database route dispatcher.
#         # Thus, we redirect the user to the same page but with the session cookie set.
#         # This will force using the database route dispatcher...
#         r = request.httprequest
#         url_redirect = werkzeug.urls.url_parse(r.base_url)
#         if r.query_string:
#             # in P3, request.query_string is bytes, the rest is text, can't mix them
#             query_string = iri_to_uri(r.query_string)
#             url_redirect = url_redirect.replace(query=query_string)
#         request.session.db = db
#         abort_and_redirect(url_redirect)

#     # if db not provided, use the session one
#     if not db and request.session.db and http.db_filter([request.session.db]):
#         db = request.session.db

#     # if no database provided and no database in session, use monodb
#     if not db:
#         db = db_monodb(request.httprequest)

#     # if no db can be found til here, send to the database selector
#     # the database selector will redirect to database manager if needed
#     if not db:
#         werkzeug.exceptions.abort(werkzeug.utils.redirect(redirect, 303))

#     # always switch the session to the computed db
#     if db != request.session.db:
#         request.session.logout()
#         abort_and_redirect(request.httprequest.url)

#     request.session.db = db
class CmsLoginAuthentication(http.Controller):
    @http.route('/web/login/',website=True, type='http', auth="none")
    def web_login(self, redirect=None, **kw):
        main.ensure_db()
        request.params['login_success'] = False
        if request.httprequest.method == 'GET' and redirect and request.session.uid:
            url = f'/cms/{"dashboard/"}'
            return werkzeug.utils.redirect(url)

        if not request.uid:
            request.uid = odoo.SUPERUSER_ID

        values = request.params.copy()
        try:
            values['databases'] = http.db_list()
        except odoo.exceptions.AccessDenied:
            values['databases'] = None

        if request.httprequest.method == 'POST':
            old_uid = request.uid
            try:
                uid = request.session.authenticate(request.session.db, request.params['login'], request.params['password'])
                request.params['login_success'] = True
                current_user = request.env['res.users'].browse(request.session.uid)
                print(f"\n\nLogin sucessful ",current_user.name, current_user.id)
                current_user_id  = Encryption.encryptMessage(str(current_user.id))
                current_user_login  = Encryption.encryptMessage(str(current_user.login))
                url = f'/cms/dashboard/?view=dashboard&id={current_user_id}&user={current_user_login}'
                return werkzeug.utils.redirect(url)
            except odoo.exceptions.AccessDenied as e:
                request.uid = old_uid
                if e.args == odoo.exceptions.AccessDenied().args:
                    values['error'] = _("Wrong login/password")
                else:
                    values['error'] = e.args[0]
        else:
            if 'error' in request.params and request.params.get('error') == 'access':
                values['error'] = _('Only employees can access this database. Please contact the administrator.')

        if 'login' not in values and request.session.get('auth_login'):
            values['login'] = request.session.get('auth_login')

        if not odoo.tools.config['list_db']:
            values['disable_database_manager'] = True

        response = request.render('web.login', values)
        response.headers['X-Frame-Options'] = 'DENY'
        return response