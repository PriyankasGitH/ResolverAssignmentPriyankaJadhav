from SeleniumTestA.utility import base
from SeleniumTestA.pages import TestPage
import os
import pytest


# Define the base URL using the saved path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_path = os.path.join(project_root, 'utility', 'QE-index.html')
base_url = f"file:///{file_path}"
browser = base.open_browser(base_url)
page = TestPage.TestPage_info(browser)

def test_sign_in_flows():
    """Test the sign-in flows: valid data, no data, and invalid email."""
    try:
        page.test_valid_data()
        page.test_no_data()
        page.test_invalid_email()
    finally:
        base.stop_browser(browser)

def test_items_list():
    """Test that verifies list items."""
    try:
        page.verifyListItems()
    finally:
        base.stop_browser(browser)


def test_dropdown_feature():
    """Test the dropdown feature."""
    try:
        page.check_default_value_and_select_option()
    finally:
        base.stop_browser(browser)


def test_button_state_check():
    """Test the state of buttons."""
    try:
        page.assert_buttons_state()
    finally:
        base.stop_browser(browser)


def test_button_appearance():
    """Test button appearance and success message."""
    try:
        page.test_button_display_and_message()
    finally:
        base.stop_browser(browser)


def test_get_the_cell_value_from_user():
    """Test getting cell value from the table."""
    try:
        page.get_cell_value(2, 2)
    finally:
        base.stop_browser(browser)
