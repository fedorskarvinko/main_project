from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(mask_card_number):
    assert get_mask_card_number(7000792289606361) == mask_card_number


def test_get_mask_account(mask_account):
    assert get_mask_account(73654108430135874305) == mask_account
