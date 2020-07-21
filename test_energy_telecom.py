
import pytest
@pytest.fixture
def visit_site(py):
    py.visit("http://energy-telecom.portnov.com/qa/")

def test_contact_information(py,visit_site):
    field_name = py.getx("//input[@id='firstName']").type("Jack")
