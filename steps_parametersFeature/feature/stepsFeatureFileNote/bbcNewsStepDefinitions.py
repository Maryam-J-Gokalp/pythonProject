from behave import *


def use_step_matcher(param):
    pass


use_step_matcher("re")


@given("user is on the homePage")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given user is on the homePage')


@when("user see England, N\.Ireland and Scotland \(sub sections of Home\)")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When user see England, N.Ireland and Scotland (sub sections of Home)')


@when("user clicks sign in button at the top of the screen")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When user clicks sign in button at the top of the screen')


@step('user enters "<email or username>"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And user enters "<email or username>"')


@step("user clicks to sign in button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And user clicks to sign in button')


@then(
    'user should see message "Need help signing in\? \(Enter a password of @@££@@££ in the password field and click Sign In\) "')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Then user should see message "Need help signing in? (Enter a password of @@££@@££ in the password field and click Sign In) "')


@when('user enters username "<username>"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When user enters username "<username>"')


@step('user enters password "<password>"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And user enters password "<password>"')


@step('user should not see dashboard instead this notice message : "Incorrect sign in or password\."')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: And user should not see dashboard instead this notice message : "Incorrect sign in or password."')


@then("Sorry, that password is too short\. It needs to be eight characters or more")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Sorry, that password is too short. It needs to be eight characters or more')


@step('user enters "<password>"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And user enters "<password>"')