""" Tests for SafeDNS Records """
import pytest
# pylint:disable=redefined-outer-name, unused-import, no-self-use
from UKFastAPI.SafeDNS.tests import config
from UKFastAPI import exceptions
from UKFastAPI.utils import decorate_funcs
from UKFastAPI.SafeDNS.tests.test_utils import (
    parent, clear_safedns, create_zone, vcr_decorator)


@pytest.mark.parametrize('parent', [create_zone], indirect=True)
@pytest.mark.usefixtures('clear_safedns')
@decorate_funcs(vcr_decorator)
class TestNotes():
    """ Test class for the Note module. """

    def test_note_create_minimum(self, parent):
        """ Tests Note creation within a Zone. """
        assert parent.notes.create(
            notes=config.TEST_NOTE_CONTENTS
        )

    def test_note_create_optionals(self, parent):
        """ Tests Note creation within a Zone. """
        assert parent.notes.create(
            contact_id=config.TEST_NOTE_USER,
            notes=config.TEST_NOTE_CONTENTS
        )

    def test_note_get(self, parent):
        """ Tests a Note can be retrieved. """
        note = parent.notes.create(
            contact_id=config.TEST_NOTE_USER,
            notes=config.TEST_NOTE_CONTENTS
        )
        assert parent.notes.get(note.id)

    def test_note_list(self, parent):
        """ Test listing all notes. """
        assert parent.notes.list(all=True)
