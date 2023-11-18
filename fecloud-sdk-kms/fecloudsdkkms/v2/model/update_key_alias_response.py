# coding: utf-8

import six

from fecloudsdkcore.sdk_response import SdkResponse
from fecloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateKeyAliasResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_info': 'KeyAliasInfo'
    }

    attribute_map = {
        'key_info': 'key_info'
    }

    def __init__(self, key_info=None):
        """UpdateKeyAliasResponse

        The model defined in fecloud sdk

        :param key_info: The param of the UpdateKeyAliasResponse
        :type key_info: :class:`fecloudsdkkms.v2.KeyAliasInfo`
        """
        
        super(UpdateKeyAliasResponse, self).__init__()

        self._key_info = None
        self.discriminator = None

        if key_info is not None:
            self.key_info = key_info

    @property
    def key_info(self):
        """Gets the key_info of this UpdateKeyAliasResponse.

        :return: The key_info of this UpdateKeyAliasResponse.
        :rtype: :class:`fecloudsdkkms.v2.KeyAliasInfo`
        """
        return self._key_info

    @key_info.setter
    def key_info(self, key_info):
        """Sets the key_info of this UpdateKeyAliasResponse.

        :param key_info: The key_info of this UpdateKeyAliasResponse.
        :type key_info: :class:`fecloudsdkkms.v2.KeyAliasInfo`
        """
        self._key_info = key_info

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateKeyAliasResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
