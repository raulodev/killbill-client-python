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


class TagDefinitionApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_tag_definition(self, body=None, created_by=None, **kwargs):  # noqa: E501
        """Create a tag definition  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.create_tag_definition(body, created_by, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param TagDefinition body: (required)
        :param Str created_by: (required)
        :param Str reason:
        :param Str comment:
        :return: TagDefinition
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('is_async'):
            return self.create_tag_definition_with_http_info(body, created_by, **kwargs)  # noqa: E501
        else:
            (data) = self.create_tag_definition_with_http_info(body, created_by, **kwargs)  # noqa: E501
            return data

    def create_tag_definition_with_http_info(self, body=None, created_by=None, **kwargs):  # noqa: E501
        """Create a tag definition  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.create_tag_definition_with_http_info(body, created_by, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param TagDefinition body: (required)
        :param Str created_by: (required)
        :param Str reason:
        :param Str comment:
        :return: TagDefinition
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'created_by', 'reason', 'comment']  # noqa: E501
        all_params.append('is_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_tag_definition" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_tag_definition`")  # noqa: E501
        # verify the required parameter 'created_by' is set
        if ('created_by' not in params or
                params['created_by'] is None):
            raise ValueError("Missing the required parameter `created_by` when calling `create_tag_definition`")  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            '/1.0/kb/tagDefinitions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TagDefinition',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_tag_definition(self, tag_definition_id=None, created_by=None, **kwargs):  # noqa: E501
        """Delete a tag definition  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.delete_tag_definition(tag_definition_id, created_by, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param Str tag_definition_id: (required)
        :param Str created_by: (required)
        :param Str reason:
        :param Str comment:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('is_async'):
            return self.delete_tag_definition_with_http_info(tag_definition_id, created_by, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_tag_definition_with_http_info(tag_definition_id, created_by, **kwargs)  # noqa: E501
            return data

    def delete_tag_definition_with_http_info(self, tag_definition_id=None, created_by=None, **kwargs):  # noqa: E501
        """Delete a tag definition  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.delete_tag_definition_with_http_info(tag_definition_id, created_by, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param Str tag_definition_id: (required)
        :param Str created_by: (required)
        :param Str reason:
        :param Str comment:
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag_definition_id', 'created_by', 'reason', 'comment']  # noqa: E501
        all_params.append('is_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_tag_definition" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag_definition_id' is set
        if ('tag_definition_id' not in params or
                params['tag_definition_id'] is None):
            raise ValueError("Missing the required parameter `tag_definition_id` when calling `delete_tag_definition`")  # noqa: E501
        # verify the required parameter 'created_by' is set
        if ('created_by' not in params or
                params['created_by'] is None):
            raise ValueError("Missing the required parameter `created_by` when calling `delete_tag_definition`")  # noqa: E501

        if 'tag_definition_id' in params and not re.search('\\w+-\\w+-\\w+-\\w+-\\w+', params['tag_definition_id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `tag_definition_id` when calling `delete_tag_definition`, must conform to the pattern `/\\w+-\\w+-\\w+-\\w+-\\w+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'tag_definition_id' in params:
            path_params['tagDefinitionId'] = params['tag_definition_id']  # noqa: E501

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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Killbill Api Key', 'Killbill Api Secret', 'basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/1.0/kb/tagDefinitions/{tagDefinitionId}', 'DELETE',
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

    def get_tag_definition(self, tag_definition_id=None, **kwargs):  # noqa: E501
        """Retrieve a tag definition  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.get_tag_definition(tag_definition_id, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param Str tag_definition_id: (required)
        :param Str audit:
        :return: TagDefinition
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('is_async'):
            return self.get_tag_definition_with_http_info(tag_definition_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tag_definition_with_http_info(tag_definition_id, **kwargs)  # noqa: E501
            return data

    def get_tag_definition_with_http_info(self, tag_definition_id=None, **kwargs):  # noqa: E501
        """Retrieve a tag definition  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.get_tag_definition_with_http_info(tag_definition_id, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param Str tag_definition_id: (required)
        :param Str audit:
        :return: TagDefinition
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag_definition_id', 'audit']  # noqa: E501
        all_params.append('is_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tag_definition" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag_definition_id' is set
        if ('tag_definition_id' not in params or
                params['tag_definition_id'] is None):
            raise ValueError("Missing the required parameter `tag_definition_id` when calling `get_tag_definition`")  # noqa: E501

        if 'tag_definition_id' in params and not re.search('\\w+-\\w+-\\w+-\\w+-\\w+', params['tag_definition_id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `tag_definition_id` when calling `get_tag_definition`, must conform to the pattern `/\\w+-\\w+-\\w+-\\w+-\\w+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'tag_definition_id' in params:
            path_params['tagDefinitionId'] = params['tag_definition_id']  # noqa: E501

        query_params = []
        if 'audit' in params:
            query_params.append(('audit', params['audit']))  # noqa: E501

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
            '/1.0/kb/tagDefinitions/{tagDefinitionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TagDefinition',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tag_definition_audit_logs_with_history(self, tag_definition_id=None, **kwargs):  # noqa: E501
        """Retrieve tag definition audit logs with history by id  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.get_tag_definition_audit_logs_with_history(tag_definition_id, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param Str tag_definition_id: (required)
        :return: List[AuditLog]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('is_async'):
            return self.get_tag_definition_audit_logs_with_history_with_http_info(tag_definition_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tag_definition_audit_logs_with_history_with_http_info(tag_definition_id, **kwargs)  # noqa: E501
            return data

    def get_tag_definition_audit_logs_with_history_with_http_info(self, tag_definition_id=None, **kwargs):  # noqa: E501
        """Retrieve tag definition audit logs with history by id  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.get_tag_definition_audit_logs_with_history_with_http_info(tag_definition_id, is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param Str tag_definition_id: (required)
        :return: List[AuditLog]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tag_definition_id']  # noqa: E501
        all_params.append('is_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tag_definition_audit_logs_with_history" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tag_definition_id' is set
        if ('tag_definition_id' not in params or
                params['tag_definition_id'] is None):
            raise ValueError("Missing the required parameter `tag_definition_id` when calling `get_tag_definition_audit_logs_with_history`")  # noqa: E501

        if 'tag_definition_id' in params and not re.search('\\w+-\\w+-\\w+-\\w+-\\w+', params['tag_definition_id']):  # noqa: E501
            raise ValueError("Invalid value for parameter `tag_definition_id` when calling `get_tag_definition_audit_logs_with_history`, must conform to the pattern `/\\w+-\\w+-\\w+-\\w+-\\w+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'tag_definition_id' in params:
            path_params['tagDefinitionId'] = params['tag_definition_id']  # noqa: E501

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
            '/1.0/kb/tagDefinitions/{tagDefinitionId}/auditLogsWithHistory', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='List[AuditLog]',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tag_definitions(self, **kwargs):  # noqa: E501
        """List tag definitions  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.get_tag_definitions(is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param Str audit:
        :return: List[TagDefinition]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('is_async'):
            return self.get_tag_definitions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_tag_definitions_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_tag_definitions_with_http_info(self, **kwargs):  # noqa: E501
        """List tag definitions  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass is_async=True
        >>> thread = api.get_tag_definitions_with_http_info(is_async=True)
        >>> result = thread.get()

        :param is_async bool
        :param Str audit:
        :return: List[TagDefinition]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['audit']  # noqa: E501
        all_params.append('is_async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tag_definitions" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'audit' in params:
            query_params.append(('audit', params['audit']))  # noqa: E501

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
            '/1.0/kb/tagDefinitions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='List[TagDefinition]',  # noqa: E501
            auth_settings=auth_settings,
            is_async=params.get('is_async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
