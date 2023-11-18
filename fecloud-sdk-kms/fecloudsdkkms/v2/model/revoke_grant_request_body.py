# coding: utf-8

import six

from fecloudsdkcore.utils.http_utils import sanitize_for_serialization


class RevokeGrantRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_id': 'str',
        'grant_id': 'str',
        'sequence': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'grant_id': 'grant_id',
        'sequence': 'sequence'
    }

    def __init__(self, key_id=None, grant_id=None, sequence=None):
        """RevokeGrantRequestBody

        The model defined in fecloud sdk

        :param key_id: The param of the RevokeGrantRequestBody
        :type key_id: str
        :param grant_id: The param of the RevokeGrantRequestBody
        :type grant_id: str
        :param sequence: The param of the RevokeGrantRequestBody
        :type sequence: str
        """
        
        

        self._key_id = None
        self._grant_id = None
        self._sequence = None
        self.discriminator = None

        self.key_id = key_id
        self.grant_id = grant_id
        if sequence is not None:
            self.sequence = sequence

    @property
    def key_id(self):
        """Gets the key_id of this RevokeGrantRequestBody.

        :return: The key_id of this RevokeGrantRequestBody.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this RevokeGrantRequestBody.

        :param key_id: The key_id of this RevokeGrantRequestBody.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def grant_id(self):
        """Gets the grant_id of this RevokeGrantRequestBody.

        :return: The grant_id of this RevokeGrantRequestBody.
        :rtype: str
        """
        return self._grant_id

    @grant_id.setter
    def grant_id(self, grant_id):
        """Sets the grant_id of this RevokeGrantRequestBody.

        :param grant_id: The grant_id of this RevokeGrantRequestBody.
        :type grant_id: str
        """
        self._grant_id = grant_id

    @property
    def sequence(self):
        """Gets the sequence of this RevokeGrantRequestBody.

        :return: The sequence of this RevokeGrantRequestBody.
        :rtype: str
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        """Sets the sequence of this RevokeGrantRequestBody.

        :param sequence: The sequence of this RevokeGrantRequestBody.
        :type sequence: str
        """
        self._sequence = sequence

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
        if not isinstance(other, RevokeGrantRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
