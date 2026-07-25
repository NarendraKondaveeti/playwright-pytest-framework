
import pytest
from pages.sortable_data_tables_page import SortableDataTablesPage

@pytest.mark.smoke
def test_sortable_data_tables(page):

    tables = SortableDataTablesPage(page)

    tables.open()

    actual_rows = tables.get_total_rows()

    expected_rows = 4

    assert actual_rows == expected_rows, (
        f"Row count mismatch.\n"
        f"Expected : {expected_rows}\n"
        f"Actual   : {actual_rows}"
    )

    actual_name = tables.get_last_name(1)

    expected_name = "Smith"

    assert actual_name == expected_name, (
        f"Last Name mismatch.\n"
        f"Expected : '{expected_name}'\n"
        f"Actual   : '{actual_name}'"
    )