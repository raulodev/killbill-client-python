# coding: utf-8

#
# Copyright 2010-2014 Ning, Inc.
# Copyright 2014-2020 Groupon, Inc
# Copyright 2020-2021 Equinix, Inc
# Copyright 2014-2021 The Billing Project, LLC
#
# The Billing Project, LLC licenses this file to you under the Apache License, version 2.0
# (the "License"); you may not use this file except in compliance with the
# License.  You may obtain a copy of the License at:
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the
# License for the specific language governing permissions and limitations
# under the License.
#

"""
    Kill Bill

    Kill Bill is an open-source billing and payments platform  # noqa: E501

    OpenAPI spec version: 0.24.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from killbill.api_client import ApiClient


class AdminApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_queue_entries(self, **kwargs):  # noqa: E501
        """Get queues entries  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.get_queue_entries(is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param Str account_id:
        :param Str queue_name:
        :param Str service_name:
        :param Bool with_history:
        :param Str min_date:
        :param Str max_date:
        :param Bool with_in_processing:
        :param Bool with_bus_events:
        :param Bool with_notifications:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('is_async'):
            return self.get_queue_entries_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_queue_entries_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_queue_entries_with_http_info(self, **kwargs):  # noqa: E501
        """Get queues entries  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.get_queue_entries_with_http_info(is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param Str account_id:
        :param Str queue_name:
        :param Str service_name:
        :param Bool with_history:
        :param Str min_date:
        :param Str max_date:
        :param Bool with_in_processing:
        :param Bool with_bus_events:
        :param Bool with_notifications:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id', 'queue_name', 'service_name', 'with_history', 'min_date', 'max_date', 'with_in_processing', 'with_bus_events', 'with_notifications']  # noqa: E501
        all_params.append('is_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_queue_entries" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'account_id' in params:
            query_params.append(('accountId', params['account_id']))  # noqa: E501
        if 'queue_name' in params:
            query_params.append(('queueName', params['queue_name']))  # noqa: E501
        if 'service_name' in params:
            query_params.append(('serviceName', params['service_name']))  # noqa: E501
        if 'with_history' in params:
            query_params.append(('withHistory', params['with_history']))  # noqa: E501
        if 'min_date' in params:
            query_params.append(('minDate', params['min_date']))  # noqa: E501
        if 'max_date' in params:
            query_params.append(('maxDate', params['max_date']))  # noqa: E501
        if 'with_in_processing' in params:
            query_params.append(('withInProcessing', params['with_in_processing']))  # noqa: E501
        if 'with_bus_events' in params:
            query_params.append(('withBusEvents', params['with_bus_events']))  # noqa: E501
        if 'with_notifications' in params:
            query_params.append(('withNotifications', params['with_notifications']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Killbill Api Key', 'Killbill Api Secret', 'basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0/kb/admin/queues', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def invalidates_cache(self, **kwargs):  # noqa: E501
        """Invalidates the given Cache if specified, otherwise invalidates all caches  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.invalidates_cache(is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param Str cache_name:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('is_async'):
            return self.invalidates_cache_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.invalidates_cache_with_http_info(**kwargs)  # noqa: E501
            return data

    def invalidates_cache_with_http_info(self, **kwargs):  # noqa: E501
        """Invalidates the given Cache if specified, otherwise invalidates all caches  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.invalidates_cache_with_http_info(is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param Str cache_name:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['cache_name']  # noqa: E501
        all_params.append('is_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method invalidates_cache" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'cache_name' in params:
            query_params.append(('cacheName', params['cache_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Killbill Api Key', 'Killbill Api Secret', 'basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0/kb/admin/cache', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def invalidates_cache_by_account(self, account_id=None, **kwargs):  # noqa: E501
        """Invalidates Caches per account level  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.invalidates_cache_by_account(account_id, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param Str account_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('is_async'):
            return self.invalidates_cache_by_account_with_http_info(account_id, **kwargs)  # noqa: E501
        else:
            (data) = self.invalidates_cache_by_account_with_http_info(account_id, **kwargs)  # noqa: E501
            return data

    def invalidates_cache_by_account_with_http_info(self, account_id=None, **kwargs):  # noqa: E501
        """Invalidates Caches per account level  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.invalidates_cache_by_account_with_http_info(account_id, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param Str account_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_id']  # noqa: E501
        all_params.append('is_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method invalidates_cache_by_account" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_id' is set
        if ('account_id' not in params or
                params['account_id'] is None):
            raise ValueError("Missing the required parameter `account_id` when calling `invalidates_cache_by_account`")  # noqa: E501

        if 'account_id' in params and not re.search('\\w+-\\w+-\\w+-\\w+-\\w+', params['account_id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `account_id` when calling `invalidates_cache_by_account`, must conform to the pattern `/\\w+-\\w+-\\w+-\\w+-\\w+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'account_id' in params:
            path_params['accountId'] = params['account_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Killbill Api Key', 'Killbill Api Secret', 'basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0/kb/admin/cache/accounts/{accountId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def invalidates_cache_by_tenant(self, **kwargs):  # noqa: E501
        """Invalidates Caches per tenant level  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.invalidates_cache_by_tenant(is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('is_async'):
            return self.invalidates_cache_by_tenant_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.invalidates_cache_by_tenant_with_http_info(**kwargs)  # noqa: E501
            return data

    def invalidates_cache_by_tenant_with_http_info(self, **kwargs):  # noqa: E501
        """Invalidates Caches per tenant level  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.invalidates_cache_by_tenant_with_http_info(is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('is_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method invalidates_cache_by_tenant" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Killbill Api Key', 'Killbill Api Secret', 'basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0/kb/admin/cache/tenants', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_in_rotation(self, **kwargs):  # noqa: E501
        """Put the host back into rotation  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.put_in_rotation(is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('is_async'):
            return self.put_in_rotation_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.put_in_rotation_with_http_info(**kwargs)  # noqa: E501
            return data

    def put_in_rotation_with_http_info(self, **kwargs):  # noqa: E501
        """Put the host back into rotation  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.put_in_rotation_with_http_info(is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('is_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_in_rotation" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Killbill Api Key', 'Killbill Api Secret', 'basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0/kb/admin/healthcheck', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_out_of_rotation(self, **kwargs):  # noqa: E501
        """Put the host out of rotation  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.put_out_of_rotation(is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('is_async'):
            return self.put_out_of_rotation_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.put_out_of_rotation_with_http_info(**kwargs)  # noqa: E501
            return data

    def put_out_of_rotation_with_http_info(self, **kwargs):  # noqa: E501
        """Put the host out of rotation  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.put_out_of_rotation_with_http_info(is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('is_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_out_of_rotation" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Killbill Api Key', 'Killbill Api Secret', 'basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0/kb/admin/healthcheck', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def trigger_invoice_generation_for_parked_accounts(self, created_by=None, **kwargs):  # noqa: E501
        """Trigger an invoice generation for all parked accounts  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.trigger_invoice_generation_for_parked_accounts(created_by, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param Str created_by: (required)
        :param Int offset:
        :param Int limit:
        :param List[Str] plugin_property:
        :param Str reason:
        :param Str comment:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('is_async'):
            return self.trigger_invoice_generation_for_parked_accounts_with_http_info(created_by, **kwargs)  # noqa: E501
        else:
            (data) = self.trigger_invoice_generation_for_parked_accounts_with_http_info(created_by, **kwargs)  # noqa: E501
            return data

    def trigger_invoice_generation_for_parked_accounts_with_http_info(self, created_by=None, **kwargs):  # noqa: E501
        """Trigger an invoice generation for all parked accounts  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.trigger_invoice_generation_for_parked_accounts_with_http_info(created_by, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param Str created_by: (required)
        :param Int offset:
        :param Int limit:
        :param List[Str] plugin_property:
        :param Str reason:
        :param Str comment:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['created_by', 'offset', 'limit', 'plugin_property', 'reason', 'comment']  # noqa: E501
        all_params.append('is_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method trigger_invoice_generation_for_parked_accounts" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'created_by' is set
        if ('created_by' not in params or
                params['created_by'] is None):
            raise ValueError("Missing the required parameter `created_by` when calling `trigger_invoice_generation_for_parked_accounts`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'plugin_property' in params:
            query_params.append(('pluginProperty', params['plugin_property']))  # noqa: E501
            collection_formats['pluginProperty'] = 'multi'  # noqa: E501

        header_params = {}
        if 'created_by' in params:
            header_params['X-Killbill-CreatedBy'] = params['created_by']  # noqa: E501
        if 'reason' in params:
            header_params['X-Killbill-Reason'] = params['reason']  # noqa: E501
        if 'comment' in params:
            header_params['X-Killbill-Comment'] = params['comment']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Killbill Api Key', 'Killbill Api Secret', 'basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0/kb/admin/invoices', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_payment_transaction_state(self, payment_id=None, payment_transaction_id=None, body=None, created_by=None, **kwargs):  # noqa: E501
        """Update existing paymentTransaction and associated payment state  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.update_payment_transaction_state(payment_id, payment_transaction_id, body, created_by, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param Str payment_id: (required)
        :param Str payment_transaction_id: (required)
        :param AdminPayment body: (required)
        :param Str created_by: (required)
        :param Str reason:
        :param Str comment:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('is_async'):
            return self.update_payment_transaction_state_with_http_info(payment_id, payment_transaction_id, body, created_by, **kwargs)  # noqa: E501
        else:
            (data) = self.update_payment_transaction_state_with_http_info(payment_id, payment_transaction_id, body, created_by, **kwargs)  # noqa: E501
            return data

    def update_payment_transaction_state_with_http_info(self, payment_id=None, payment_transaction_id=None, body=None, created_by=None, **kwargs):  # noqa: E501
        """Update existing paymentTransaction and associated payment state  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.update_payment_transaction_state_with_http_info(payment_id, payment_transaction_id, body, created_by, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param Str payment_id: (required)
        :param Str payment_transaction_id: (required)
        :param AdminPayment body: (required)
        :param Str created_by: (required)
        :param Str reason:
        :param Str comment:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['payment_id', 'payment_transaction_id', 'body', 'created_by', 'reason', 'comment']  # noqa: E501
        all_params.append('is_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_payment_transaction_state" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'payment_id' is set
        if ('payment_id' not in params or
                params['payment_id'] is None):
            raise ValueError("Missing the required parameter `payment_id` when calling `update_payment_transaction_state`")  # noqa: E501
        # verify the required parameter 'payment_transaction_id' is set
        if ('payment_transaction_id' not in params or
                params['payment_transaction_id'] is None):
            raise ValueError("Missing the required parameter `payment_transaction_id` when calling `update_payment_transaction_state`")  # noqa: E501
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_payment_transaction_state`")  # noqa: E501
        # verify the required parameter 'created_by' is set
        if ('created_by' not in params or
                params['created_by'] is None):
            raise ValueError("Missing the required parameter `created_by` when calling `update_payment_transaction_state`")  # noqa: E501

        if 'payment_id' in params and not re.search('\\w+-\\w+-\\w+-\\w+-\\w+', params['payment_id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `payment_id` when calling `update_payment_transaction_state`, must conform to the pattern `/\\w+-\\w+-\\w+-\\w+-\\w+/`")  # noqa: E501
        if 'payment_transaction_id' in params and not re.search('\\w+-\\w+-\\w+-\\w+-\\w+', params['payment_transaction_id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `payment_transaction_id` when calling `update_payment_transaction_state`, must conform to the pattern `/\\w+-\\w+-\\w+-\\w+-\\w+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'payment_id' in params:
            path_params['paymentId'] = params['payment_id']  # noqa: E501
        if 'payment_transaction_id' in params:
            path_params['paymentTransactionId'] = params['payment_transaction_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'created_by' in params:
            header_params['X-Killbill-CreatedBy'] = params['created_by']  # noqa: E501
        if 'reason' in params:
            header_params['X-Killbill-Reason'] = params['reason']  # noqa: E501
        if 'comment' in params:
            header_params['X-Killbill-Comment'] = params['comment']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Killbill Api Key', 'Killbill Api Secret', 'basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0/kb/admin/payments/{paymentId}/transactions/{paymentTransactionId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
