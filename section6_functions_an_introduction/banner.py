def banner_text(text: str = " ", screen_width: int = 80) -> None: # " " og 80 er i dette tilfelle default verdiene, men hvis vi gir parametrene andre verdier når vi printer er det disse nye som gjelder
    """
    Get text sentered text with stars surrounding it
    :param text: the string to print
    :param screen_width: the overall width to print within with two stars on both sides
    :return: None
    """
    if len(text) > screen_width - 4:
        raise ValueError("String {0} is larger than the specified width {1}"
                         .format(text, screen_width))
        # print("EEK!!")
        # print("THE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH")

    if text == "*":
        print("*" * screen_width)
    else:
        centered_text = text.center(screen_width - 4)
        output_string = "**{}**".format(centered_text)
        print(output_string)


banner_text("*")
banner_text("Always look on the bright side of life...")
banner_text("If life seems jolly rotten,")
banner_text("There is something you have forgotten!")
banner_text("And that is to laugh and smile and dance and sing,")
banner_text()
banner_text("When you are feeling in the dumps,")
banner_text("Don't be silly chumps,")
banner_text("Just purse your lips and whistle - that's the thing!")
banner_text("And... always look on the bright side of life...")
banner_text("*")



