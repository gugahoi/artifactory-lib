# Simple tests as this philosophy makes sense
# http://softwareengineering.stackexchange.com/questions/252748/is-it-actually-worth-unit-testing-an-api-client

import unittest
from mock import patch
from Artifactory import Artifactory

URL = {
    'USERS': '/security/users',
    'API': '/security/apiKey'
}

class ArtifactoryTestCase(unittest.TestCase):
    """ Tests for `Artifactory.py` """

    @classmethod
    def setUpClass(self):
        self.artifactory = Artifactory('admin','password', base_url='https://fake_url/artifactory')

    def test_get_users(self):
        with patch.object(Artifactory, 'get') as mock:
            self.artifactory.get_users()
            mock.assert_called_once_with(URL['USERS'])

    def test_get_user(self):
        with patch.object(Artifactory, 'get') as mock:
            self.artifactory.get_user('tim')
            mock.assert_called_once_with('/security/users/tim')

    def test_create_user(self):
        with patch.object(Artifactory, 'put') as mock:
            self.artifactory.create_user('tim', {
                'password': 'password',
                'email': 'tim@email.com'
            })

            mock.assert_called_once_with('/security/users/tim', {
                'password': 'password',
                'email': 'tim@email.com'
            })

    def test_create_user_failure(self):
        self.assertFalse(
            self.artifactory.create_user('tim', {
                'email': 'tim@email.com'
            }),
            msg='Expected no create_user to return early'
        )


    def test_delete_user(self):
        with patch.object(Artifactory, 'delete') as mock:
            self.artifactory.delete_user('tim')
            mock.assert_called_once_with('/security/users/tim')

    def test_get_api_key(self):
        with patch.object(Artifactory, 'get') as mock:
            self.artifactory.get_api_key()
            mock.assert_called_once_with(URL['API'])

    def test_create_api_key(self):
        with patch.object(Artifactory, 'post') as mock:
            self.artifactory.create_api_key()
            mock.assert_called_once_with(URL['API'])

    def test_regenerate_api_key(self):
        with patch.object(Artifactory, 'put') as mock:
            self.artifactory.regenerate_api_key()
            mock.assert_called_once_with(URL['API'])

    def test_revoke_api_key(self):
        with patch.object(Artifactory, 'delete') as mock:
            self.artifactory.revoke_api_key()
            mock.assert_called_once_with(URL['API'])

    def test_delete_item(self):
        item_path = '/somerepo/some-item/99.9/some-item.jar'
        with patch.object(Artifactory, 'delete') as mock:
            self.artifactory.delete_item(item_path)
            mock.assert_called_once_with(item_path)

    def test_get_storage_info(self):
        with patch.object(Artifactory, 'get') as mock:
            self.artifactory.get_storage_info()
            mock.assert_called_once_with('/storageinfo')

    def test_search_by_creation_date(self):
        start = 1479790359503
        end = 1479790373396
        repos = 'somerepo'
        params = {'from': start, 'to': end, 'repos': repos}
        with patch.object(Artifactory, 'get') as mock:
            self.artifactory.search_by_creation_date(start, end, repos)
            mock.assert_called_once_with('/search/creation', params=params)

if __name__ == '__main__':
    unittest.main()
