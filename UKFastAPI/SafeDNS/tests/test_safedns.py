""" Tests for the SafeDNS implementation. """
import pytest
# pylint:disable=unused-import, redefined-outer-name, no-self-use
from UKFastAPI.SafeDNS.tests.test_utils import (
    safedns, clear_safedns, get_safedns, generate_zone_name, create_zone)
from UKFastAPI.SafeDNS.safedns import SafeDns
from UKFastAPI.exceptions import UKFastAPIException
from UKFastAPI.SafeDNS import config

# pylint:disable=wildcard-import


@pytest.mark.usefixtures('clear_safedns')
class TestSafeDNS():
    """ Test class for the SafeDNS module. """

    def test_safedns_auth_blank(self):
        """ Tests SafeDNS when given no authentication token. """
        with pytest.raises(UKFastAPIException):
            SafeDns()

    def test_safedns_auth_invalid(self):
        """ Tests SafeDNS when given and invalid authentication token. """
        with pytest.raises(UKFastAPIException):
            SafeDns('invalid-token').auth_test()

    def test_safedns_auth_valid(self):
        """ Tests SafeDNS when given and valid authentication token. """
        assert get_safedns().auth_test()

    # @pytest.mark.skip(reason="Slows down testing, so turning off for now.")
    def test_safedns_pagination(self):
        """ Tests if pagination works in the API. """
        note_count = 50
        user_id = 0
        zone = create_zone()
        for _ in range(note_count):
            zone.notes.create(contact_id=user_id, notes=generate_zone_name())
        assert len(zone.notes.list(all=True)) >= note_count

    @pytest.mark.parametrize('safedns', [get_safedns], indirect=True)
    def test_safedns_managers(self, safedns):
        """ Tests that the SafeDNS managers are all valid. """
        assert safedns.settings
        assert safedns.zones
        assert safedns.templates