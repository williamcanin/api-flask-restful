

def init_app(app):

    @app.errorhandler(404)
    def page_not_found(e):
        return {
            "message": "Route not found",
            "status_code": 404
        }
