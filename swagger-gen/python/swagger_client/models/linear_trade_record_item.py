# coding: utf-8

"""
    Bybit API

    ## REST API for the Bybit Exchange. Base URI: [https://api-testnet.bybit.com]    # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@bybit.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class LinearTradeRecordItem(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'closed_size': 'float',
        'exec_fee': 'float',
        'exec_id': 'str',
        'exec_price': 'float',
        'exec_qty': 'float',
        'exec_type': 'str',
        'exec_value': 'float',
        'fee_rate': 'float',
        'last_liquidity_ind': 'str',
        'leaves_qty': 'float',
        'order_id': 'str',
        'order_link_id': 'str',
        'order_price': 'float',
        'order_qty': 'float',
        'order_type': 'str',
        'price': 'float',
        'side': 'str',
        'symbol': 'str',
        'trade_time': 'int',
        'trade_time_ms': 'int'
    }

    attribute_map = {
        'closed_size': 'closed_size',
        'exec_fee': 'exec_fee',
        'exec_id': 'exec_id',
        'exec_price': 'exec_price',
        'exec_qty': 'exec_qty',
        'exec_type': 'exec_type',
        'exec_value': 'exec_value',
        'fee_rate': 'fee_rate',
        'last_liquidity_ind': 'last_liquidity_ind',
        'leaves_qty': 'leaves_qty',
        'order_id': 'order_id',
        'order_link_id': 'order_link_id',
        'order_price': 'order_price',
        'order_qty': 'order_qty',
        'order_type': 'order_type',
        'price': 'price',
        'side': 'side',
        'symbol': 'symbol',
        'trade_time': 'trade_time',
        'trade_time_ms': 'trade_time_ms'
    }

    def __init__(self, closed_size=None, exec_fee=None, exec_id=None, exec_price=None, exec_qty=None, exec_type=None, exec_value=None, fee_rate=None, last_liquidity_ind=None, leaves_qty=None, order_id=None, order_link_id=None, order_price=None, order_qty=None, order_type=None, price=None, side=None, symbol=None, trade_time=None, trade_time_ms=None):  # noqa: E501
        """LinearTradeRecordItem - a model defined in Swagger"""  # noqa: E501

        self._closed_size = None
        self._exec_fee = None
        self._exec_id = None
        self._exec_price = None
        self._exec_qty = None
        self._exec_type = None
        self._exec_value = None
        self._fee_rate = None
        self._last_liquidity_ind = None
        self._leaves_qty = None
        self._order_id = None
        self._order_link_id = None
        self._order_price = None
        self._order_qty = None
        self._order_type = None
        self._price = None
        self._side = None
        self._symbol = None
        self._trade_time = None
        self._trade_time_ms = None
        self.discriminator = None

        if closed_size is not None:
            self.closed_size = closed_size
        if exec_fee is not None:
            self.exec_fee = exec_fee
        if exec_id is not None:
            self.exec_id = exec_id
        if exec_price is not None:
            self.exec_price = exec_price
        if exec_qty is not None:
            self.exec_qty = exec_qty
        if exec_type is not None:
            self.exec_type = exec_type
        if exec_value is not None:
            self.exec_value = exec_value
        if fee_rate is not None:
            self.fee_rate = fee_rate
        if last_liquidity_ind is not None:
            self.last_liquidity_ind = last_liquidity_ind
        if leaves_qty is not None:
            self.leaves_qty = leaves_qty
        if order_id is not None:
            self.order_id = order_id
        if order_link_id is not None:
            self.order_link_id = order_link_id
        if order_price is not None:
            self.order_price = order_price
        if order_qty is not None:
            self.order_qty = order_qty
        if order_type is not None:
            self.order_type = order_type
        if price is not None:
            self.price = price
        if side is not None:
            self.side = side
        if symbol is not None:
            self.symbol = symbol
        if trade_time is not None:
            self.trade_time = trade_time
        if trade_time_ms is not None:
            self.trade_time_ms = trade_time_ms

    @property
    def closed_size(self):
        """Gets the closed_size of this LinearTradeRecordItem.  # noqa: E501


        :return: The closed_size of this LinearTradeRecordItem.  # noqa: E501
        :rtype: float
        """
        return self._closed_size

    @closed_size.setter
    def closed_size(self, closed_size):
        """Sets the closed_size of this LinearTradeRecordItem.


        :param closed_size: The closed_size of this LinearTradeRecordItem.  # noqa: E501
        :type: float
        """

        self._closed_size = closed_size

    @property
    def exec_fee(self):
        """Gets the exec_fee of this LinearTradeRecordItem.  # noqa: E501


        :return: The exec_fee of this LinearTradeRecordItem.  # noqa: E501
        :rtype: float
        """
        return self._exec_fee

    @exec_fee.setter
    def exec_fee(self, exec_fee):
        """Sets the exec_fee of this LinearTradeRecordItem.


        :param exec_fee: The exec_fee of this LinearTradeRecordItem.  # noqa: E501
        :type: float
        """

        self._exec_fee = exec_fee

    @property
    def exec_id(self):
        """Gets the exec_id of this LinearTradeRecordItem.  # noqa: E501


        :return: The exec_id of this LinearTradeRecordItem.  # noqa: E501
        :rtype: str
        """
        return self._exec_id

    @exec_id.setter
    def exec_id(self, exec_id):
        """Sets the exec_id of this LinearTradeRecordItem.


        :param exec_id: The exec_id of this LinearTradeRecordItem.  # noqa: E501
        :type: str
        """

        self._exec_id = exec_id

    @property
    def exec_price(self):
        """Gets the exec_price of this LinearTradeRecordItem.  # noqa: E501


        :return: The exec_price of this LinearTradeRecordItem.  # noqa: E501
        :rtype: float
        """
        return self._exec_price

    @exec_price.setter
    def exec_price(self, exec_price):
        """Sets the exec_price of this LinearTradeRecordItem.


        :param exec_price: The exec_price of this LinearTradeRecordItem.  # noqa: E501
        :type: float
        """

        self._exec_price = exec_price

    @property
    def exec_qty(self):
        """Gets the exec_qty of this LinearTradeRecordItem.  # noqa: E501


        :return: The exec_qty of this LinearTradeRecordItem.  # noqa: E501
        :rtype: float
        """
        return self._exec_qty

    @exec_qty.setter
    def exec_qty(self, exec_qty):
        """Sets the exec_qty of this LinearTradeRecordItem.


        :param exec_qty: The exec_qty of this LinearTradeRecordItem.  # noqa: E501
        :type: float
        """

        self._exec_qty = exec_qty

    @property
    def exec_type(self):
        """Gets the exec_type of this LinearTradeRecordItem.  # noqa: E501


        :return: The exec_type of this LinearTradeRecordItem.  # noqa: E501
        :rtype: str
        """
        return self._exec_type

    @exec_type.setter
    def exec_type(self, exec_type):
        """Sets the exec_type of this LinearTradeRecordItem.


        :param exec_type: The exec_type of this LinearTradeRecordItem.  # noqa: E501
        :type: str
        """

        self._exec_type = exec_type

    @property
    def exec_value(self):
        """Gets the exec_value of this LinearTradeRecordItem.  # noqa: E501


        :return: The exec_value of this LinearTradeRecordItem.  # noqa: E501
        :rtype: float
        """
        return self._exec_value

    @exec_value.setter
    def exec_value(self, exec_value):
        """Sets the exec_value of this LinearTradeRecordItem.


        :param exec_value: The exec_value of this LinearTradeRecordItem.  # noqa: E501
        :type: float
        """

        self._exec_value = exec_value

    @property
    def fee_rate(self):
        """Gets the fee_rate of this LinearTradeRecordItem.  # noqa: E501


        :return: The fee_rate of this LinearTradeRecordItem.  # noqa: E501
        :rtype: float
        """
        return self._fee_rate

    @fee_rate.setter
    def fee_rate(self, fee_rate):
        """Sets the fee_rate of this LinearTradeRecordItem.


        :param fee_rate: The fee_rate of this LinearTradeRecordItem.  # noqa: E501
        :type: float
        """

        self._fee_rate = fee_rate

    @property
    def last_liquidity_ind(self):
        """Gets the last_liquidity_ind of this LinearTradeRecordItem.  # noqa: E501


        :return: The last_liquidity_ind of this LinearTradeRecordItem.  # noqa: E501
        :rtype: str
        """
        return self._last_liquidity_ind

    @last_liquidity_ind.setter
    def last_liquidity_ind(self, last_liquidity_ind):
        """Sets the last_liquidity_ind of this LinearTradeRecordItem.


        :param last_liquidity_ind: The last_liquidity_ind of this LinearTradeRecordItem.  # noqa: E501
        :type: str
        """

        self._last_liquidity_ind = last_liquidity_ind

    @property
    def leaves_qty(self):
        """Gets the leaves_qty of this LinearTradeRecordItem.  # noqa: E501


        :return: The leaves_qty of this LinearTradeRecordItem.  # noqa: E501
        :rtype: float
        """
        return self._leaves_qty

    @leaves_qty.setter
    def leaves_qty(self, leaves_qty):
        """Sets the leaves_qty of this LinearTradeRecordItem.


        :param leaves_qty: The leaves_qty of this LinearTradeRecordItem.  # noqa: E501
        :type: float
        """

        self._leaves_qty = leaves_qty

    @property
    def order_id(self):
        """Gets the order_id of this LinearTradeRecordItem.  # noqa: E501


        :return: The order_id of this LinearTradeRecordItem.  # noqa: E501
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this LinearTradeRecordItem.


        :param order_id: The order_id of this LinearTradeRecordItem.  # noqa: E501
        :type: str
        """

        self._order_id = order_id

    @property
    def order_link_id(self):
        """Gets the order_link_id of this LinearTradeRecordItem.  # noqa: E501


        :return: The order_link_id of this LinearTradeRecordItem.  # noqa: E501
        :rtype: str
        """
        return self._order_link_id

    @order_link_id.setter
    def order_link_id(self, order_link_id):
        """Sets the order_link_id of this LinearTradeRecordItem.


        :param order_link_id: The order_link_id of this LinearTradeRecordItem.  # noqa: E501
        :type: str
        """

        self._order_link_id = order_link_id

    @property
    def order_price(self):
        """Gets the order_price of this LinearTradeRecordItem.  # noqa: E501


        :return: The order_price of this LinearTradeRecordItem.  # noqa: E501
        :rtype: float
        """
        return self._order_price

    @order_price.setter
    def order_price(self, order_price):
        """Sets the order_price of this LinearTradeRecordItem.


        :param order_price: The order_price of this LinearTradeRecordItem.  # noqa: E501
        :type: float
        """

        self._order_price = order_price

    @property
    def order_qty(self):
        """Gets the order_qty of this LinearTradeRecordItem.  # noqa: E501


        :return: The order_qty of this LinearTradeRecordItem.  # noqa: E501
        :rtype: float
        """
        return self._order_qty

    @order_qty.setter
    def order_qty(self, order_qty):
        """Sets the order_qty of this LinearTradeRecordItem.


        :param order_qty: The order_qty of this LinearTradeRecordItem.  # noqa: E501
        :type: float
        """

        self._order_qty = order_qty

    @property
    def order_type(self):
        """Gets the order_type of this LinearTradeRecordItem.  # noqa: E501


        :return: The order_type of this LinearTradeRecordItem.  # noqa: E501
        :rtype: str
        """
        return self._order_type

    @order_type.setter
    def order_type(self, order_type):
        """Sets the order_type of this LinearTradeRecordItem.


        :param order_type: The order_type of this LinearTradeRecordItem.  # noqa: E501
        :type: str
        """

        self._order_type = order_type

    @property
    def price(self):
        """Gets the price of this LinearTradeRecordItem.  # noqa: E501


        :return: The price of this LinearTradeRecordItem.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this LinearTradeRecordItem.


        :param price: The price of this LinearTradeRecordItem.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def side(self):
        """Gets the side of this LinearTradeRecordItem.  # noqa: E501


        :return: The side of this LinearTradeRecordItem.  # noqa: E501
        :rtype: str
        """
        return self._side

    @side.setter
    def side(self, side):
        """Sets the side of this LinearTradeRecordItem.


        :param side: The side of this LinearTradeRecordItem.  # noqa: E501
        :type: str
        """

        self._side = side

    @property
    def symbol(self):
        """Gets the symbol of this LinearTradeRecordItem.  # noqa: E501


        :return: The symbol of this LinearTradeRecordItem.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this LinearTradeRecordItem.


        :param symbol: The symbol of this LinearTradeRecordItem.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def trade_time(self):
        """Gets the trade_time of this LinearTradeRecordItem.  # noqa: E501


        :return: The trade_time of this LinearTradeRecordItem.  # noqa: E501
        :rtype: int
        """
        return self._trade_time

    @trade_time.setter
    def trade_time(self, trade_time):
        """Sets the trade_time of this LinearTradeRecordItem.


        :param trade_time: The trade_time of this LinearTradeRecordItem.  # noqa: E501
        :type: int
        """

        self._trade_time = trade_time

    @property
    def trade_time_ms(self):
        """Gets the trade_time_ms of this LinearTradeRecordItem.  # noqa: E501


        :return: The trade_time_ms of this LinearTradeRecordItem.  # noqa: E501
        :rtype: int
        """
        return self._trade_time_ms

    @trade_time_ms.setter
    def trade_time_ms(self, trade_time_ms):
        """Sets the trade_time_ms of this LinearTradeRecordItem.


        :param trade_time_ms: The trade_time_ms of this LinearTradeRecordItem.  # noqa: E501
        :type: int
        """

        self._trade_time_ms = trade_time_ms

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
                result[attr] = value
        if issubclass(LinearTradeRecordItem, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, LinearTradeRecordItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
