import pytest

from cablemystreet import create_app
from cablemystreet.models import db


@pytest.fixture()
def testapp(request):
    app = create_app('cablemystreet.settings.TestConfig', env='dev')
    client = app.test_client()

    db.app = app
    db.create_all()

    def teardown():
        db.session.remove()
        db.drop_all()

    request.addfinalizer(teardown)

    return client
