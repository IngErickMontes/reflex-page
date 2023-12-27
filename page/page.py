"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
import reflex as rx



class State(rx.State):
    """The app statekdgjhdkjfgdlfhgldkhflghdlkfgldshflghleirhotherorheoiur."""

    pass


def index() -> rx.Component:
    return rx.fragment(
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
