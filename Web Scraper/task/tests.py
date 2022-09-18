import requests
from hstest.check_result import CheckResult
from hstest.stage_test import StageTest
from hstest.test_case import TestCase


class WebScraperTest(StageTest):
    def generate(self):
        return [
            TestCase(stdin="http://api.quotable.io/quotes/-CzNrWMGIg8V",
                     check_function=self.check_valid_res),

            TestCase(stdin="http://api.quotable.io/asdfgh",
                     check_function=self.check_not_valid_res),

            TestCase(stdin="http://api.quotable.io/authors",
                     check_function=self.check_not_valid_res)
        ]

    def check_valid_res(self, reply, attach=None) -> CheckResult:
        try:
            qod = requests.get("http://api.quotable.io/quotes/-CzNrWMGIg8V").json()["content"]
        except Exception:
            return CheckResult.wrong("An error occurred when tests tried to connect to the Internet page.\n"
                                     "Please, try again.")
        if qod in reply:
            return CheckResult.correct()
        elif isinstance(reply, str):
            return CheckResult.wrong("Couldn't find the exact quote in the result.")
        elif isinstance(reply, (list, dict)):
            return CheckResult.wrong("Make sure you extracted the quote from the json body correctly.")
        else:
            return CheckResult.wrong("The result doesn't look like a quote... at all.")

    def check_not_valid_res(self, reply, attach=None):
        if all(x in reply.lower() for x in ("invalid", "resource")):
            return CheckResult.correct()
        else:
            return CheckResult.wrong("If the resource is invalid, the user should get informed exactly on this.")


if __name__ == '__main__':
    WebScraperTest().run_tests()
