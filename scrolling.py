for i in range(5):
    actions = ActionChains(driver)
    actions.w3c_actions = ActionBuilder(driver,    mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(374, 1177)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(374, 446)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    time.sleep(3)