import pytest
from app import create_app
from app import db as _db
import os
from sqlalchemy import event
from app.product.factories import ProductFactory
from config.settings import APP_NAME, BASE_DIR
import importlib


# Fetch all factories to attach db session afterwards
factories = []
for subd, directory, files in os.walk(os.path.join(BASE_DIR, APP_NAME)):
    for file in files:
        if file == 'factories.py':
            module = importlib.import_module('{}.{}.factories'.format(APP_NAME, os.path.basename(subd)))
            factories += [getattr(module, a) for a in dir(module) if a[-7:] == 'Factory']


@pytest.fixture(scope="session")
def app(request):
    """
    Returns session-wide application.
    """
    os.environ['APP_ENV'] = 'testing'
    return create_app()


@pytest.fixture(scope="session")
def db(app, request):
    """
    Returns session-wide initialised database.
    """
    with app.app_context():
        _db.drop_all()
        _db.create_all()


@pytest.fixture(scope="function", autouse=True)
def session(app, db, request):
    """
    Returns function-scoped session.
    """
    with app.app_context():
        conn = _db.engine.connect()
        txn = conn.begin()

        options = dict(bind=conn, binds={})
        sess = _db.create_scoped_session(options=options)

        # establish  a SAVEPOINT just before beginning the test
        # (http://docs.sqlalchemy.org/en/latest/orm/session_transaction.html#using-savepoint)
        sess.begin_nested()

        @event.listens_for(sess(), 'after_transaction_end')
        def restart_savepoint(sess2, trans):
            # Detecting whether this is indeed the nested transaction of the test
            if trans.nested and not trans._parent.nested:
                # The test should have normally called session.commit(),
                # but to be safe we explicitly expire the session
                sess2.expire_all()
                sess.begin_nested()

        _db.session = sess
        # Extend session to all factories
        for factory in factories:
            factory._meta.sqlalchemy_session = sess

        yield sess

        # Cleanup
        sess.remove()
        # This instruction rollsback any commit that were executed in the tests.
        txn.rollback()
        conn.close()
