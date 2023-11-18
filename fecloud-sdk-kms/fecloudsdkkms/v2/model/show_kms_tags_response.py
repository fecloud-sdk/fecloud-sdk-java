# coding: utf-8

import six

from fecloudsdkcore.sdk_response import SdkResponse
from fecloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKmsTagsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[TagItem]',
        'exist_tags_num': 'int'
    }

    attribute_map = {
        'tags': 'tags',
        'exist_tags_num': 'existTagsNum'
    }

    def __init__(self, tags=None, exist_tags_num=None):
        """ShowKmsTagsResponse

        The model defined in fecloud sdk

        :param tags: The param of the ShowKmsTagsResponse
        :type tags: list[:class:`fecloudsdkkms.v2.TagItem`]
        :param exist_tags_num: The param of the ShowKmsTagsResponse
        :type exist_tags_num: int
        """
        
        super(ShowKmsTagsResponse, self).__init__()

        self._tags = None
        self._exist_tags_num = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if exist_tags_num is not None:
            self.exist_tags_num = exist_tags_num

    @property
    def tags(self):
        """Gets the tags of this ShowKmsTagsResponse.

        :return: The tags of this ShowKmsTagsResponse.
        :rtype: list[:class:`fecloudsdkkms.v2.TagItem`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowKmsTagsResponse.

        :param tags: The tags of this ShowKmsTagsResponse.
        :type tags: list[:class:`fecloudsdkkms.v2.TagItem`]
        """
        self._tags = tags

    @property
    def exist_tags_num(self):
        """Gets the exist_tags_num of this ShowKmsTagsResponse.

        :return: The exist_tags_num of this ShowKmsTagsResponse.
        :rtype: int
        """
        return self._exist_tags_num

    @exist_tags_num.setter
    def exist_tags_num(self, exist_tags_num):
        """Sets the exist_tags_num of this ShowKmsTagsResponse.

        :param exist_tags_num: The exist_tags_num of this ShowKmsTagsResponse.
        :type exist_tags_num: int
        """
        self._exist_tags_num = exist_tags_num

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
        if not isinstance(other, ShowKmsTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other