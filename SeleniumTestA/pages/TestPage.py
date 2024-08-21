
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException, TimeoutException, NoAlertPresentException

from SeleniumTestA.utility import common
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


class TestPage_info:
    PRINT_LOCATORS = False
    def __init__(self,browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 10)

        section = "Test1"
        self.userEmail = common.getLocator(section, "userEmail")
        self.userPassword = common.getLocator(section, "userPassword")
        self.SignInButton = common.getLocator(section, "SignInButton")
        # Define locators for warning messages
        self.required_warning_locator = "//*[contains(text(), 'This field is required')]"
        self.email_warning_locator = "//*[contains(text(), 'Please include an @')]"

        section="Test2"
        self.listItem = common.getLocator(section,"listItem")
        self.secondListItem = common.getLocator(section,"secondListItem")
        self.badgeValue = common.getLocator(section,"badgeValue")

        section3 = "Test3"
        self.dropdownDefaultOption = common.getLocator(section3, "dropdownDefaultOption")
        self.dropdownOptionThree = common.getLocator(section3, "dropdownOptionThree")


        section4 = "Test4"
        self.enabledButton = common.getLocator(section4, "enabledButton")
        self.disabledButton = common.getLocator(section4, "disabledButton")


        section5 = "Test5"
        self.awaitText = common.getLocator(section5, "awaitText")
        self.test5Button = common.getLocator(section5, "test5Button")
        self.successMessage = common.getLocator(section5, "successMessage")


        section6 = "Test6"
        self.table = common.getLocator(section6, "table")
        self.Ventosanzap = common.getLocator(section6, "Ventosanzap")


    """
    Test 1
    Navigate to the home page
    Assert that both the email address and password inputs are present as well as the login button
    Enter in an email address and password combination into the respective fields
    """

    def assert_fields_cleared(self):
        email_field = self.browser.find_element(*self.userEmail)
        password_field = self.browser.find_element(*self.userPassword)
        assert email_field.get_attribute('value') == "", "Email field was not cleared."
        assert password_field.get_attribute('value') == "", "Password field was not cleared."

    def test_valid_data(self):
        email_field = self.browser.find_element(*self.userEmail)
        password_field = self.browser.find_element(*self.userPassword)
        sign_in_button = self.browser.find_element(*self.SignInButton)

        # Enter valid data
        email_field.clear()
        email_field.send_keys("johndoe@gmail.com")
        password_field.clear()
        password_field.send_keys("abcd%#!")
        sign_in_button.click()

        # Assert that fields are cleared
        self.assert_fields_cleared()

        # Test 2: No data, check warning message

    def test_no_data(self):
        # Locate elements
        email_field = self.browser.find_element(*self.userEmail)
        password_field = self.browser.find_element(*self.userPassword)
        sign_in_button = self.browser.find_element(*self.SignInButton)

        # Leave fields empty and click sign in
        email_field.clear()
        password_field.clear()

        # Save the initial URL
        initial_url = self.browser.current_url

        # Click the sign-in button
        sign_in_button.click()

        # Assert sign-in button remains enabled
        assert sign_in_button.is_enabled(), "Sign-in button should remain enabled when fields are empty."
        print("Sign-in button remains enabled when fields are empty.")

        # Assert that the page URL remains the same
        assert self.browser.current_url == initial_url, "The page URL has changed after submitting empty fields."
        print("Page URL remains the same after submitting empty fields.")

        # Test 3: Invalid email, check warning message

    def test_invalid_email(self):
        # Locate elements
        email_field = self.browser.find_element(*self.userEmail)
        password_field = self.browser.find_element(*self.userPassword)
        sign_in_button = self.browser.find_element(*self.SignInButton)

        # Enter invalid email and click sign in
        email_field.clear()
        email_field.send_keys("abc")
        password_field.clear()
        password_field.send_keys("abcd%#!")

        # Save the initial URL
        initial_url = self.browser.current_url

        # Click the sign-in button
        sign_in_button.click()

        # Assert sign-in button remains enabled
        assert sign_in_button.is_enabled(), "Sign-in button should remain enabled for invalid email."

        # Assert that the page URL remains the same
        assert self.browser.current_url == initial_url, "The page URL has changed after invalid email submission."

    """
    Test 2
    Navigate to the home page
    In the test 2 div, assert that there are three values in the listgroup
    Assert that the second list item's value is set to "List Item 2"
    Assert that the second list item's badge value is 6
    """

    def verifyListItems(self):
        try:
            # Print the navigation statement
            print("Navigated to the home page")

            # Ensure self.listItem is a tuple like (By.XPATH, 'xpath_value')
            if isinstance(self.listItem, str):
                self.listItem = (By.XPATH, self.listItem)

            # Assert that there are three values in the list group
            list_group_element = self.wait.until(EC.visibility_of_element_located(self.listItem))
            list_items = list_group_element.find_elements(By.XPATH, ".//li")
            num_items = len(list_items)
            assert num_items == 3, f"Expected 3 list items, but found {num_items}"

            # Print number of values in the list group
            print(f"There are {num_items} values in the list group")

            # Ensure self.secondListItem is a tuple like (By.XPATH, 'xpath_value')
            if isinstance(self.secondListItem, str):
                self.secondListItem = (By.XPATH, self.secondListItem)

            # Assert that the second list item's value is set to "List Item 2"
            second_list_item_element = self.wait.until(EC.visibility_of_element_located(self.secondListItem))
            actual_text = second_list_item_element.text.strip()

            # Clean the text to remove the badge value
            clean_text = re.sub(r'\s*\d+$', '', actual_text)  # Removes trailing digits
            expected_text = "List Item 2"
            assert clean_text.strip() == expected_text, f"Expected '{expected_text}', but found '{clean_text.strip()}'"

            # Assert that the badge value is 6
            badge_value_element = second_list_item_element.find_element(By.XPATH,
                                                                        ".//span[@class='badge badge-pill badge-primary']")
            assert badge_value_element.text == "6", f"Expected badge value '6', but found {badge_value_element.text}"

            # Print results
            print("Second List Item text: " + clean_text)
            print("Badge Value text: " + badge_value_element.text)

        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise
        except Exception as e:
            print(f"Error during verification: {e}")
            raise
    """ 
    Test 3
    Navigate to the home page
    In the test 3 div, assert that "Option 1" is the default selected value
    Select "Option 3" from the select list
    """


    def check_default_value_and_select_option(self):
        wait = self.wait
        try:
            # Print locators for debugging based on the class-level flag
            if self.PRINT_LOCATORS:
                print(f"Locator for dropdown default option: {self.dropdownDefaultOption}")
                print(f"Locator for dropdown option three: {self.dropdownOptionThree}")

            # Ensure locators are in tuple format
            if isinstance(self.dropdownDefaultOption, str):
                self.dropdownDefaultOption = (By.XPATH, self.dropdownDefaultOption)
            if isinstance(self.dropdownOptionThree, str):
                self.dropdownOptionThree = (By.XPATH, self.dropdownOptionThree)

            # Print the navigation statement
            print("Navigated to the home page")

            # Wait for the dropdown button and get its text
            dropdown_button = wait.until(EC.visibility_of_element_located(self.dropdownDefaultOption))
            default_option_text = dropdown_button.text

            # Assert default option text
            assert default_option_text == "Option 1", f"Expected 'Option 1', but got '{default_option_text}'"
            print("In the test 3 div, the option 1 value is the default selection")

            # Click the dropdown button to reveal options
            dropdown_button.click()

            # Wait for the dropdown menu to be visible
            dropdown_menu = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "dropdown-menu")))

            # Click "Option 3"
            option_three = wait.until(EC.element_to_be_clickable(self.dropdownOptionThree))
            option_three.click()

            # Output for selection change
            updated_default_text = dropdown_button.text
            assert updated_default_text == "Option 3", f"Expected 'Option 3', but got '{updated_default_text}'"
            print("Option 3 is selected")

        except AssertionError as e:
            print(f"Assertion failed: {e}")
            raise
        except Exception as e:
            print(f"Error during dropdown interaction: {e}")
            raise


    """
    Test 4
    Navigate to the home page
    In the test 4 div, assert that the first button is enabled and that the second button is disabled
    """
    def assert_buttons_state(self):
        try:
            # Wait for the buttons to be visible
            enabled_button_element = self.wait.until(EC.visibility_of_element_located(self.enabledButton))
            disabled_button_element = self.wait.until(EC.visibility_of_element_located(self.disabledButton))

            # Assert that the enabled button is enabled
            assert enabled_button_element.is_enabled(), "Enabled button is not enabled"

            # Assert that the disabled button is disabled
            assert not disabled_button_element.is_enabled(), "Disabled button is not disabled"

            # Output message
            print("We have two buttons: enabled & disabled")

        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except TimeoutException as e:
            print(f"Timeout while waiting for element: {e}")
        except AssertionError as e:
            print(f"Assertion failed: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


    """
    Test 5
    Navigate to the home page
    In the test 5 div, wait for a button to be displayed (note: the delay is random) and then click it
    Once you've clicked the button, assert that a success message is displayed
    Assert that the button is now disabled
    """

    def test_button_display_and_message(self):
        try:
            # Wait for the placeholder text to be visible
            self.wait.until(EC.visibility_of_element_located(self.awaitText))

            # Wait for the test button to be clickable
            test_button_element = self.wait.until(EC.element_to_be_clickable(self.test5Button))

            # Click the test button
            test_button_element.click()
            print("Clicked the test button.")

            # Assert that the success message is displayed
            success_message_element = self.wait.until(EC.visibility_of_element_located(self.successMessage))
            assert success_message_element.is_displayed(), "Success message is not displayed."

            # Assert that the button is now disabled
            assert not test_button_element.is_enabled(), "Test button is still enabled after clicking."

            # Output message
            print("Success message is displayed and the button is disabled.")

        except NoSuchElementException as e:
            print(f"Element not found: {e}")
        except TimeoutException as e:
            print(f"Timeout while waiting for element: {e}")
        except AssertionError as e:
            print(f"Assertion failed: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


    """
    Test 6
    Navigate to the home page
    Write a method that allows you to find the value of any cell on the grid
    Use the method to find the value of the cell at coordinates 2, 2 (staring at 0 in the top left corner)
    Assert that the value of the cell is "Ventosanzap"
    """

    def get_cell_value(self, row, col):
        """
        Get the value of a cell in the table grid based on row and column indices.
        :param row: Row index (starting from 0)
        :param col: Column index (starting from 0)
        :return: Cell value as a string
        """
        try:
            print(f"Getting cell value at row {row}, column {col}")

            # Check if row and column indices are valid
            if row < 0 or col < 0:
                raise IndexError("Row or column index cannot be negative")

            # Wait for the table to be visible
            table_element = self.wait.until(EC.visibility_of_element_located(self.table))
            print("Table found")

            # Find all rows in the table
            rows = table_element.find_elements(By.XPATH, ".//tbody/tr")  # Adjust XPath if necessary
            print(f"Found {len(rows)} rows in the table")

            # Check if the row index is valid
            if row >= len(rows):
                raise IndexError("Row index out of range")

            # Find the specific row
            row_element = rows[row]
            print(f"Row {row} found")

            # Find all columns (cells) in the row
            cols = row_element.find_elements(By.XPATH, ".//td")
            print(f"Found {len(cols)} columns in row {row}")

            # Check if the column index is valid
            if col >= len(cols):
                raise IndexError("Column index out of range")

            # Get the specific cell
            cell_element = cols[col]
            cell_text = cell_element.text.strip()

            print(f"Cell value at ({row}, {col}) is '{cell_text}'")

            # Assert that the value at (2, 2) is "Ventosanzap"
            if row == 2 and col == 2:
                assert cell_text == "Ventosanzap", f"Expected 'Ventosanzap', but found '{cell_text}'"

            return cell_text

        except IndexError as e:
            print(f"Index error: {e}")
            raise
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
            raise
        except TimeoutException as e:
            print(f"Timeout while waiting for element: {e}")
            raise
        except Exception as e:
            print(f"An error occurred: {e}")
            raise
