def get_locator(page, locator):
    if isinstance(locator, str):
        return page.locator(locator)
    elif isinstance(locator, dict):
        role = locator.get("role")
        name = locator.get("name")
        return page.get_by_role(role, name=name)
    else:
        raise Exception("Invalid locator format")