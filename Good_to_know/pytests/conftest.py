import pytest


@pytest.fixture(autouse=True)
def clean_text_file():
    with open("new_file", mode ='w') as f_o:
        pass