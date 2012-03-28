"""
API for working with Authorize.net's Transaction Details API

http://developer.authorize.net/api/transaction_details/

To use the TransactionDetails Api you must have the setting turned
on in your authorize.net account:
 - https://account.authorize.net
 - Account > Settings
   - Transaction Details API
     - Enable Transaction Details API


"""

from authorize import gen_xml as xml, base, responses as resp
from authorize.util import request


class Api(base.BaseApi):
    """
    Main Transaction Detail api object.

    Each api call will return a response dictionary in formats similar
    to:

    {'messages': {'message': {'code': {'text_': u'I00001'},
                              'text': {'text_': u'Successful.'}},
                  'result_code': {'text_': u'Ok'}}}

    with all the possible variations and arguments depending on the
    format specified by Authorize.net at:

        http://www.authorize.net/support/ReportingGuide_XML.pdf

    a field in the response can be accesses by using either dictionary
    access methods:

        response['messages']['message']['code']['text_']

    or object dot-notation:

        response.messages.message.code.text_

    NOTE:
    It's important that you make sure that your Authorize dashboard
    uses the same delimiter and encapsulator that you are using in
    your API objects. If you don't check this it could happen that the
    direct_response cannot be parsed even in those cases where it's
    absolutely necessary, like in the AIM API.
    """
    responses = resp.trans_map

    @request
    def get_settled_batch_list(**kw):
        """
        create request to get settled batch list

        arguments:
            REQUIRED:
                None


            OPTIONAL or CONDITIONAL:
                include_statistics: boolean
                first_settlement_date: date of first settlement to include in search
                last_settlement_date: date of last settlement to include in search
        """
        return ('getSettledBatchListRequest', kw) + xml.settled_batch_request(**kw)

    @request
    def get_batch_statistics(**kw):
        """
        create request to get batch statistics

        arguments:
            REQUIRED:
                batch_id: the settled batch id
        """
        return 'getBatchStatisticsRequest', kw, xml.batch_statistics(**kw)

    @request
    def get_transaction_list(**kw):
        """
        create request to get transaction list by batch id

        arguments:
            REQUIRED:
                batch_id: the batch id of transactions to obtain.
        """
        return 'getTransactionListRequest', kw, xml.transaction_list(**kw)

    @request
    def get_unsettled_transaction_list(**kw):
        """
        create request to get unsettled transaction list (returns up to 1000)
        of the most recent transactions.

        arguments: None
        """
        return 'getUnsettledTransactionListRequest', kw

    @request
    def get_transaction_details(**kw):
        """
        create request to get transaction details by transaction id

        arguments:
            REQUIRED:
                trans_id: the transaction id of payment detail requested.
        """
        return 'getTransactionDetailsRequest', kw, xml.transaction_details(**kw)
