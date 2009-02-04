from authorize import gen_xml as xml, util, base, responses as resp

from authorize.gen_xml import INDIVIDUAL, BUSINESS, ECHECK_CCD, ECHECK_PPD, ECHECK_TEL, ECHECK_WEB
from authorize.gen_xml import BANK, CREDIT_CARD, DAYS_INTERVAL, MONTHS_INTERVAL
from authorize.gen_xml import ACCOUNT_CHECKING, ACCOUNT_SAVINGS
from authorize.gen_xml import ACCOUNT_BUSINESS_CHECKING

class Api(base.BaseApi):
    """
    Main ARB api object.
    
    It implements the following api calls:
    
        create_subscription: create a payment subscription
            arguments:
                REQUIRED:
                    interval_unit: L{DAYS_INTERVAL} or L{MONTHS_INTERVAL}
                    interval_length: up to 3 digits, 1-12 for months, 7-365 for days
                    start_date: YYYY-MM-DD of type L{unicode}
                    amount: L{float} or L{decimal.Decimal}
                    profile_type: L{CREDIT_CARD} (default) or L{BANK}
                    card_number: L{unicode} or L{int}, required with CREDIT_CARD
                    expiration_date: YYYY-MM, required with CREDIT_CARD
                    routing_number: 9 digits, required with BANK
                    account_number: 5 to 17 digits, required with BANK
                    name_on_account: required with BANK

                OPTIONAL or CONDITIONAL:
                    subscription_name: unique name for the subscription
                    total_occurrences: up to 4 digits, default 9999
                    trial_occurrences: up to 4 digits
                    trial_amount: L{float} or L{decimal.Decimal}, must
                                  be provided when trial_occurrences is set
                    invoice_number:
                    description:
                    customer_type: L{INDIVIDUAL} or L{BUSINESS}
                    customer_id:
                    customer_email:
                    phone:
                    fax:
                    driver_number: customer driving license number
                    driver_state: license state
                    driver_birth: date of birth on the license
                    tax_id:
                    account_type: L{ACCOUNT_CHECKING} or L{ACCOUNT_SAVINGS}
                            or L{ACCOUNT_BUSINESS_CHECKING}, only with BANK
                    bank_name:
                    echeck_type: L{ECHECK_CCD} or L{ECHECK_TEL} or
                        L{ECHECK_PPD} or L{ECHECK_WEB}, only with BANK
                    bill_first_name, ship_first_name:
                    bill_last_name, ship_last_name:
                    bill_company, ship_company:
                    bill_address, ship_address:
                    bill_city, ship_city:
                    bill_state, ship_state:
                    bill_zip, ship_zip:
                    bill_country, ship_country:
                    ship_phone:
                    ship_fax:
                
        update_subscription: update a payment subscription
            arguments: everything above plus
                subscription_id: required
                
            
        cancel_subscription: cancel subscription
            arguments:
                subscription_id: required

    Each of them will return a response dictionary in formats similar
    to:
    
    {'messages': {'message': {'code': {'text_': u'I00001'},
                              'text': {'text_': u'Successful.'}},
                  'result_code': {'text_': u'Ok'}}}
    
    with all the possible variations and arguments depending on the
    format specified by Authorize.net at:
    
        http://www.authorize.net/support/ARB_guide.pdf
    
    a field in the response can be accesses by using either dictionary
    access methods:
        
        response['messages']['message']['code']['text_']
    
    or object dot-notation:
    
        response.messages.message.code.text_
    """
    responses = resp.arb_map

util.populate(Api, xml, 'arb_')