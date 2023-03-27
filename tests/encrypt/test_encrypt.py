from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message('Vamo que vamo', 1) == 'V_omav euq oma'
    assert encrypt_message('Vamo que vamo', 2) == 'omav euq om_aV'
    assert encrypt_message('Vamo que vamo', 3) == 'maV_omav euq o'
    assert encrypt_message('Vamo que vamo', 4) == 'omav euq _omaV'
    assert encrypt_message('Vamo que vamo', 999) == 'omav euq omaV'
    with pytest.raises(TypeError):
        encrypt_message('Vamo que vamo', '999')
    with pytest.raises(TypeError):
        encrypt_message(None, 4)
