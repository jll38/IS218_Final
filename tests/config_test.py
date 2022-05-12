def test_development_config(application):
    """test development config"""
    application.config.from_object('app.config.Development')
    assert application.config['DEBUG']
    assert not application.config['TESTING']


def test_testing_config(application):
    """test testing config"""
    application.config.from_object('app.config.Testing')
    assert application.config['DEBUG']
    assert application.config['TESTING']

def test_production_config(application):
    """test production config"""
    application.config.from_object('app.config.ProductionConfig')

    log.info("inside test_config / test production config")
    log.info(application.config['SQLALCHEMY_DATABASE_URI'])

    assert not application.config['DEBUG']
    assert not application.config['TESTING']