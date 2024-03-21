import pytest
import logging
import requests

from conftest_plugin import Cfg

_log = logging.getLogger('Main')

auth = {'username': 'admin', 'password': 'adminpassword'}
wrong_auth = {'username': 'admin', 'password': 'bad_password'}

base_url = Cfg.params.get('rest_base_url', 'http://localhost:8080')

FIRST_ELEMENT = 0


@pytest.mark.rest_api
class TestRestApiContent:

    @pytest.fixture(scope='class')
    def session(self):
        _log.info('Session login')
        session = requests.Session()
        response = session.post(f'{base_url}/login', json=auth)
        if response.status_code != 200:
            pytest.fail("Unsuccessful login")
        yield session
        _log.info('Session logout')
        response = session.get(f'{base_url}/logout')
        if response.status_code != 200:
            pytest.fail("Unsuccessful logout")

    @pytest.mark.login
    def test_passed_login(self):
        _log.info('Checking successful login...')
        response = requests.post(f'{base_url}/login', json=auth)
        assert response.status_code == 200, "Unsuccessful login"
        assert response.json().get('message') == "Logged in successfully!"

    @pytest.mark.login
    def test_wrong_login(self):
        _log.info('Checking wrong login...')
        response = requests.post(f'{base_url}/login', json=wrong_auth)
        assert response.status_code == 401, "Not expected code"
        assert response.json().get('message') == "Invalid credentials!"

    def test_add_content(self, session):
        _log.info('Checking content adding...')
        content = {'cars': ['Audi, VW', 'Toyota']}
        response_data = session.post(f'{base_url}/content', json=content)
        assert response_data.status_code == 200, "Content was not created"
        assert response_data.json().get('message') == 'Content created successfully!'

        response_get = session.get(f'{base_url}/content')
        assert response_get.status_code == 200, "Unable to get content"
        assert content in response_get.json().get('content')
        # _log.info(response_get.json().get('content'))

    def test_modify_content(self, session):
        _log.info('Checking content modification...')
        content2 = {'abc': 123}
        response_data = session.put(f'{base_url}/content/{FIRST_ELEMENT}', json=content2)
        assert response_data.status_code == 200, "Content was not modified"
        assert response_data.json().get('message') == 'Content updated successfully!'

        response_get = session.get(f'{base_url}/content')
        assert response_get.status_code == 200, "Unable to get content"
        assert content2 in response_get.json().get('content')

    def test_delete_content(self, session):
        _log.info('Checking content delete...')
        response_data = session.delete(f'{base_url}/content/{FIRST_ELEMENT}')
        assert response_data.status_code == 200, "Content was not deleted"
        assert response_data.json().get('message') == 'Content deleted successfully!'

        response_get = session.get(f'{base_url}/content')
        assert response_get.status_code == 200, "Unable to get content"
        assert not response_get.json().get('content'), 'Content still exist'

    # cleanup


# class TestRestApiContent2:
#
#     def test_fake(self):
#         pass
