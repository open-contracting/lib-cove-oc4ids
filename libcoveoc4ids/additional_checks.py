import gettext
import re

from libcoveoc4ids.additional_check import AdditionalCheck

_ = gettext.gettext


class CurrencyCheck(AdditionalCheck):
    def process(self, data, flat_data):
        amount_path = re.compile(".*amount$")

        expected_currency_paths = []
        missing = []

        for path in flat_data.keys():
            if amount_path.match(path):
                expected_currency_paths.append(path[: -len("amount")] + "currency")

        for expected in expected_currency_paths:
            if expected not in flat_data:
                missing.append(expected[: -len("currency")])

        if len(missing) == 0:
            return True

        return self.result(
            "missing-currency",
            _(
                "There are %(count)d values without a currency, Currencies should be published for all values"
            )
            % {"count": len(missing)},
            missing,
        )


class EmptyValueCheck(AdditionalCheck):
    def process(self, data, flat_data):
        missing = []

        # Similar check to libcoveocds EmptyFieldCheck
        for path, value in flat_data.items():
            if isinstance(value, str) and len(value.strip()) == 0:
                missing.append(path)
            elif isinstance(value, dict) and len(value) == 0:
                missing.append(path)
            elif isinstance(value, list) and len(value) == 0:
                missing.append(path)

        if len(missing) == 0:
            return True

        return self.result(
            "missing-values",
            _("There are %(count)d fields without values") % {"count": len(missing)},
            missing,
        )


additional_checks = [
    EmptyValueCheck(),
    CurrencyCheck(),
]
