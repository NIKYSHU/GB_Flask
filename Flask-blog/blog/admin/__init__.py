def register_views():
    from blog import models
    from blog.admin.views import TagAdminView, ArticleAdminView, UserAdminView
    from blog.extensions import admin, db
    from flask_admin.menu import MenuLink

    admin.add_view(ArticleAdminView(models.Article, db.session, category='Models'))
    admin.add_view(TagAdminView(models.Tag, db.session, category='Models'))
    admin.add_view(UserAdminView(models.User, db.session, category='Models'))
    admin.add_link(MenuLink(name='Home Page', url='/users'))
