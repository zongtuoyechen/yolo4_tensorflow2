# =============================================
# -*- coding: utf-8 -*-           
# @Time    : 2020/4/25 下午4:02    
# @Author  : xiao9616           
# @Email   : 749935253@qq.com   
# @File    : Mish.py         
# @Software: PyCharm
# ============================================
import tensorflow as tf
from tensorflow.keras.layers import Activation
from tensorflow.keras.utils import get_custom_objects
from tensorflow.math import tanh, softplus


class Mish(Activation):
    '''
    Mish Activation Function.
    .. math::
        mish(x) = x * tanh(softplus(x)) = x * tanh(ln(1 + e^{x}))
    Shape:
        - Input: Arbitrary. Use the keyword argument `input_shape`
        (tuple of integers, does not include the samples axis)
        when using this layer as the first layer in a model.
        - Output: Same shape as the input.
    Examples:
        >>> X = Activation('Mish', name="conv1_act")(X_input)
    '''

    def __init__(self, activation, **kwargs):
        super(Mish, self).__init__(activation, **kwargs)
        self.__name__ = 'Mish'


def mish(inputs):
    return inputs * tanh(softplus(inputs))


get_custom_objects().update({'Mish': Mish(mish)})
