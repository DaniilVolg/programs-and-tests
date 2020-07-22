
import pytest
@pytest.fixture
def visit_site(py):
    py.visit("http://energy-telecom.portnov.com/qa/")
  #Contact_information part
def test_contact_information(py,visit_site):
    field_name = py.getx("//input[@id='firstName']").type("Jack")
    field_last_name = py.getx("//input[@name='lastName']").type("Black")
    street_adress = py.getx("//input[@name='address']").type("1235 67 street ")
    sity_field = py.getx("//input[@name='city']").type("Brooklyn")
    state_dropbox= py.getx("//select[@name='state']").select("NY")
    index_field = py.getx("//input[@name='zip']").type("11235")
    email_field = py.getx("//input[@name='email']").type("jackblack@gmail.com")
    phone_field_1 = py.getx("//input[@id='phone1']").type("347")
    phone_field_2 = py.getx("//input[@id='phone2']").type("225")
    phone_field_3 = py.getx("//input[@id='phone3']").type("5056")
    best_way_to_contact_field = py.getx("//select[@name='bestWayToContact']").select("Phone")
    refferd_by_field = py.getx("//input[@name='refferedBy']").type("Racoon")



 #Cell Phone Service field
    current_provider_field = py.getx("//select[@name='cellPhoneCurrentProvider']").select("Verizon")
    im_happy_with_current_provider_field = py.webdriver.find_element_by_name("cellPhoneSatisfiedWithProvider[]").click()
    my_monthly_payment_field = py.getx("//input[@name='cellPhoneMonthlyBill']").type("150")
    minutes_to_plan_field = py.getx("//select[@name='cellPhoneMinutesOnPlan']").select("200")
    month_left_on_current_contract_field = py.getx("//select[@name='cellPhoneMonthsOnCurrent']").select("4")
    numbers_of_phones_plan_field = py.getx("//select[@name='cellPhoneNumberOfPhones']").select("3")
    last_upgraded_phone = py.getx("//select[@name='cellPhoneLastUpgradeMonths']").select("6")
    im_interested_in_wireless_radio_button = py.webdriver.find_element_by_name("cellPhoneWirelessCard[]").click()
