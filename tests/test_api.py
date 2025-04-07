import json

import pytest

from tests import utils


def test_valid_data():
    """Test valid data should have no errors"""
    errors, ctx = utils.test_fixture("example-data.json")

    assert errors == [], "Validation errors found"


def test_invalid_data():
    """Test valid data but with no useful fields"""
    errors, ctx = utils.test_fixture("rubbish.json")

    assert len(errors) == 5, "Expecting 5 validation errors"


def test_validation_errors():
    """Check that the validation errors are the ones we are expecting"""
    errors, ctx = utils.test_fixture("validation-errors-package.json")

    invalid_code = []
    invalid_uri = []
    invalid_number = []
    invalid_date = []
    invalid_string = []
    invalid_array = []
    invalid_object = []
    invalid_int = []

    missing_value = []
    invalid_length = []
    bad_match = []

    for error in errors:
        err = json.loads(error[0])["message"]

        if "Invalid code found in" in err:
            invalid_code.append(err)

        elif "Invalid 'uri' found" in err:
            invalid_uri.append(err)

        elif "Date is not in the correct format" in err:
            invalid_date.append(err)

        elif "is not a string" in err:
            invalid_string.append(err)

        elif "is not a integer" in err:
            invalid_int.append(err)

        elif "is not a JSON object" in err:
            invalid_object.append(err)

        elif "is not a JSON array" in err:
            invalid_array.append(err)

        elif "is not a number" in err:
            invalid_number.append(err)

        elif "is too short" in err or "does not have enough properties" in err or "should be non-empty" in err:
            invalid_length.append(err)

        elif "is missing but required" in err:
            missing_value.append(err)

        elif "does not match" in err:
            bad_match.append(err)

        else:
            # We shouldn't reach here if we have sorted all the validation
            # errors
            raise AssertionError(f"Validation error '{err}' not captured")

    assert len(ctx["additional_closed_codelist_values"]) == 5

    assert len(invalid_code) == 0
    assert len(invalid_uri) == 1
    assert len(invalid_date) == 4
    assert len(invalid_string) == 17
    assert len(invalid_int) == 1
    assert len(invalid_object) == 3
    assert len(invalid_array) == 9
    assert len(invalid_number) == 4
    assert len(invalid_length) == 6
    assert len(missing_value) == 7
    assert len(bad_match) == 1

    assert len(errors) == 53


def test_additional_fields():
    """Test that the additional fields have been parsed"""
    _, ctx = utils.test_fixture("rubbish.json")

    assert ctx["additional_fields_count"] == 2, "Expecting two additional fields"


def test_invalid_json():
    """Should cause an exception on broken json file"""
    with pytest.raises(json.decoder.JSONDecodeError):
        utils.test_fixture("invalid-json.json")


def _validate_check_result_object(check_result):
    """Check the common attributes of the result object"""
    # Tests to make sure we have the right dictionary created
    assert "check_id" in check_result, "Check result has no check_id field"
    assert "message" in check_result, "Check result has no message field"

    assert type(check_result["check_id"] is str), "Type additional check check_id is not a string"
    assert type(check_result["message"] is str), "Type additional check message is not a string"


def test_additional_checks():
    """Test the additional checks to make sure each expected one is present in test data"""
    _, ctx = utils.test_fixture("example-additional-checks.json")
    checked = 0
    check_results = ctx["additional_checks"]

    assert len(check_results) == 3, "Additional checks are incomplete"

    for check_result in check_results:
        _validate_check_result_object(check_result)

        assert len(check_result["paths"]) > 0, "Check result has no paths"

        if check_result["check_id"] in {"missing-currency", "missing-values", "missing-org-refs"}:
            checked += 1

    assert checked == len(check_results), f"Checks tested not expected total for this test data {check_results}"


def test_additional_checks_no_parties():
    """Extra check on missing-org-refs by removing all the parties definitions and thus"""
    """ triggering for every possible path"""

    _, ctx = utils.test_fixture("example-additional-checks-no-parties.json")

    assert len(ctx["additional_checks"][0]["paths"]) == 15, (
        "The number of paths where organisation refs are missing is not correct"
    )


def test_additional_checks_no_projects():
    _, ctx = utils.test_fixture("example-additional-checks-no-projects.json")

    assert len(ctx["additional_checks"][0]["paths"]) == 1


def test_codelist_checks():
    _, ctx = utils.test_fixture("example-additional-codes.json")

    assert ctx["additional_open_codelist_values"]["projects/sector"]["values"][0] == "extraSector"
    assert ctx["additional_open_codelist_values"]["projects/parties/roles"]["values"][0] == "extraRole"
    assert (
        ctx["additional_open_codelist_values"]["projects/documents/documentType"]["values"][0]
        == "x_consultationResponses"
    )

    assert ctx["additional_closed_codelist_values"]["projects/budget/amount/currency"]["values"][0] == "X_GBP"


def test_conformance_tests():
    """Test the additional checks to make sure each expected one is present in test data"""
    _, ctx = utils.test_fixture("example-additional-checks.json")
    checked = 0
    check_results = ctx["conformance_checks"]

    assert len(check_results) == 1, "Conformance checks are incomplete"

    for check_result in check_results:
        _validate_check_result_object(check_result)
        # Tests to make sure we have the right dictionary created
        assert "path_values" in check_result, "Check result has no path values"

        assert len(check_result["path_values"]) > 0, "Check result has no path values"

        if check_result["check_id"] == "invalid-project-ids":
            checked += 1

    assert checked == len(check_results), f"Checks tested not expected total for this test data {check_results}"
