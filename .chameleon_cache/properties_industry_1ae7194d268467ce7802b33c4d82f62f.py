# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/his/src/templates/properties_industry.pynml'
__tokens = {37: ('economies', 1, 37), 88: ("industry.get_property('enabled', economy) == True", 2, 39), 148: ('if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                property {', 3, 8), 163: ('economy.numeric_id', 3, 23), 222: ('industry.id', 4, 36), 238: ('industry.numeric_id', 4, 52), 389: ("${industry.get_property_declaration('substitute')}\n                    ${industry.get_property_declaration('override')}\n                    ${industry.get_property_declaration('map_colour')}\n                    ${industry.get_property_declaration('life_type')}\n                    ${industry.get_property_declaration('closure_msg')}\n                    ${industry.get_property_declaration('prod_increase_msg')}\n                    ${industry.get_property_declaration('prod_decrease_msg')}\n                    ${industry.get_property_declaration('new_ind_msg')}\n                    ${industry.get_property_declaration('min_cargo_distr')}\n                    ${industry.get_property_declaration('spec_flags')}\n                    ${industry.get_industry_layouts_as_property()}\n                    conflicting_ind_types: []; // set this prop empty, FIRS has it's own better checks for this\n                    random_sound_effects: []; // set this empty to avoid spurious default industry sounds (as of May 2017 FIRS does not yet use sound effects)", 7, 20), 391: ("industry.get_property_declaration('substitute')", 7, 22), 462: ("industry.get_property_declaration('override')", 8, 22), 531: ("industry.get_property_declaration('map_colour')", 9, 22), 602: ("industry.get_property_declaration('life_type')", 10, 22), 672: ("industry.get_property_declaration('closure_msg')", 11, 22), 744: ("industry.get_property_declaration('prod_increase_msg')", 12, 22), 822: ("industry.get_property_declaration('prod_decrease_msg')", 13, 22), 900: ("industry.get_property_declaration('new_ind_msg')", 14, 22), 972: ("industry.get_property_declaration('min_cargo_distr')", 15, 22), 1048: ("industry.get_property_declaration('spec_flags')", 16, 22), 1119: ('industry.get_industry_layouts_as_property()', 17, 22), 1558: ("${industry.get_property_declaration('name', economy)}\n                    ${industry.get_property_declaration('prod_multiplier', economy)}\n                    ${industry.get_property_declaration('input_multiplier_1', economy)}\n                    ${industry.get_property_declaration('input_multiplier_2', economy)}\n                    ${industry.get_property_declaration('input_multiplier_3', economy)}\n                    ${industry.get_property_declaration('prob_random', economy)}\n                    ${industry.get_property_declaration('prob_in_game', economy)}\n                    ${industry.get_property_declaration('prospect_chance', economy)}\n                    ${industry.get_property_declaration('fund_cost_multiplier', economy)}\n                    ${industry.get_property_declaration('remove_cost_multiplier', economy)}\n                    ${industry.get_property_declaration('remove_cost_multiplier', economy)}", 21, 20), 1560: ("industry.get_property_declaration('name', economy)", 21, 22), 1634: ("industry.get_property_declaration('prod_multiplier', economy)", 22, 22), 1719: ("industry.get_property_declaration('input_multiplier_1', economy)", 23, 22), 1807: ("industry.get_property_declaration('input_multiplier_2', economy)", 24, 22), 1895: ("industry.get_property_declaration('input_multiplier_3', economy)", 25, 22), 1983: ("industry.get_property_declaration('prob_random', economy)", 26, 22), 2064: ("industry.get_property_declaration('prob_in_game', economy)", 27, 22), 2146: ("industry.get_property_declaration('prospect_chance', economy)", 28, 22), 2231: ("industry.get_property_declaration('fund_cost_multiplier', economy)", 29, 22), 2321: ("industry.get_property_declaration('remove_cost_multiplier', economy)", 30, 22), 2413: ("industry.get_property_declaration('remove_cost_multiplier', economy)", 31, 22), 2550: ('${industry.get_accept_cargo_types_declaration(economy)}\n                    ${industry.get_prod_cargo_types_declaration(economy)}\n                    ${industry.get_nearby_station_name_declaration()}\n                }\n            }\n        }', 33, 20), 2552: ('industry.get_accept_cargo_types_declaration(economy)', 33, 22), 2628: ('industry.get_prod_cargo_types_declaration(economy)', 34, 22), 2702: ('industry.get_nearby_station_name_declaration()', 35, 22)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

import re
import functools
from itertools import chain as __chain
__marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
__re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def initialize(__loader, macros, nothing, template):

    def render(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
        __append = __stream.append
        __re_amp = g_re_amp
        __token = None
        __re_needs_escape = g_re_needs_escape

        def __convert(target):
            if (target is None):
                return
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except AttributeError:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            target = target()
            return target

        def __quote(target, quote, quote_entity, default, default_marker):
            if (target is None):
                return
            if (target is default_marker):
                return default
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            return target()
                if (target is not None):
                    try:
                        escape = (__re_needs_escape(target) is not None)
                    except TypeError:
                        pass
                    else:
                        if escape:
                            if ('&' in target):
                                target = target.replace('&', '&amp;')
                            if ('<' in target):
                                target = target.replace('<', '&lt;')
                            if ('>' in target):
                                target = target.replace('>', '&gt;')
                            if ((quote is not None) and (quote in target)):
                                target = target.replace(quote, quote_entity)
            return target
        translate = econtext['__translate']
        decode = econtext['__decode']
        convert = econtext['__convert']
        on_error_handler = econtext['__on_error_handler']
        try:
            getitem = econtext.__getitem__
            get = econtext.get
            __backup_economy_140302362814952 = get('economy', __marker)

            # <Value 'economies' (1:37)> -> __iterator
            __token = 37
            __iterator = getitem('economies')
            (__iterator, ____index_140302362783248, ) = getitem('repeat')('economy', __iterator)
            econtext['economy'] = None
            for __item in __iterator:
                econtext['economy'] = __item
                __append('\n    ')

                # <Value "industry.get_property('enabled', economy) == True" (2:39)> -> __condition
                __token = 88
                __condition = (_lookup_attr(getitem('industry'), 'get_property')('enabled', getitem('economy')) == True)
                if __condition:

                    # <Interpolation value=<Substitution '\n        if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                property {\n                    ' (2:90)> braces_required=True translation=False at 7f9ab07ea0f0> -> __content_140302383355024
                    __token = 148
                    __token = 163
                    __content_140302383355024 = _lookup_attr(getitem('economy'), 'numeric_id')
                    __content_140302383355024 = __quote(__content_140302383355024, '\x00', '&#0;', None, False)
                    __token = 222
                    __content_140302383355024_220 = _lookup_attr(getitem('industry'), 'id')
                    __content_140302383355024_220 = __quote(__content_140302383355024_220, '\x00', '&#0;', None, False)
                    __token = 238
                    __content_140302383355024_236 = _lookup_attr(getitem('industry'), 'numeric_id')
                    __content_140302383355024_236 = __quote(__content_140302383355024_236, '\x00', '&#0;', None, False)
                    __content_140302383355024 = ('%s%s%s%s%s%s%s' % ('\n        if (economy==', (__content_140302383355024 if (__content_140302383355024 is not None) else ''), ') {\n            item(FEAT_INDUSTRIES, ', (__content_140302383355024_220 if (__content_140302383355024_220 is not None) else ''), ', ', (__content_140302383355024_236 if (__content_140302383355024_236 is not None) else ''), ') {\n                property {\n                    ', ))
                    if (__content_140302383355024 is None):
                        pass
                    else:
                        if (__content_140302383355024 is False):
                            __content_140302383355024 = None
                        else:
                            __tt = type(__content_140302383355024)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_140302383355024 = str(__content_140302383355024)
                            else:
                                if (__tt is bytes):
                                    __content_140302383355024 = decode(__content_140302383355024)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_140302383355024 = __content_140302383355024.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_140302383355024)
                                            __content_140302383355024 = (str(__content_140302383355024) if (__content_140302383355024 is __converted) else __converted)
                                        else:
                                            __content_140302383355024 = __content_140302383355024()
                    if (__content_140302383355024 is not None):
                        __append(__content_140302383355024)

                    # <Interpolation value=<Substitution "\n                    ${industry.get_property_declaration('substitute')}\n                    ${industry.get_property_declaration('override')}\n                    ${industry.get_property_declaration('map_colour')}\n                    ${industry.get_property_declaration('life_type')}\n                    ${industry.get_property_declaration('closure_msg')}\n                    ${industry.get_property_declaration('prod_increase_msg')}\n                    ${industry.get_property_declaration('prod_decrease_msg')}\n                    ${industry.get_property_declaration('new_ind_msg')}\n                    ${industry.get_property_declaration('min_cargo_distr')}\n                    ${industry.get_property_declaration('spec_flags')}\n                    ${industry.get_industry_layouts_as_property()}\n                    conflicting_ind_types: []; // set this prop empty, FIRS has it's own better checks for this\n                    random_sound_effects: []; // set this empty to avoid spurious default industry sounds (as of May 2017 FIRS does not yet use sound effects)\n                    " (6:79)> braces_required=True translation=False at 7f9ab07ea978> -> __content_140302383355024
                    __token = 389
                    __token = 391
                    __content_140302383355024 = _lookup_attr(getitem('industry'), 'get_property_declaration')('substitute')
                    __content_140302383355024 = __quote(__content_140302383355024, '\x00', '&#0;', None, False)
                    __token = 462
                    __content_140302383355024_460 = _lookup_attr(getitem('industry'), 'get_property_declaration')('override')
                    __content_140302383355024_460 = __quote(__content_140302383355024_460, '\x00', '&#0;', None, False)
                    __token = 531
                    __content_140302383355024_529 = _lookup_attr(getitem('industry'), 'get_property_declaration')('map_colour')
                    __content_140302383355024_529 = __quote(__content_140302383355024_529, '\x00', '&#0;', None, False)
                    __token = 602
                    __content_140302383355024_600 = _lookup_attr(getitem('industry'), 'get_property_declaration')('life_type')
                    __content_140302383355024_600 = __quote(__content_140302383355024_600, '\x00', '&#0;', None, False)
                    __token = 672
                    __content_140302383355024_670 = _lookup_attr(getitem('industry'), 'get_property_declaration')('closure_msg')
                    __content_140302383355024_670 = __quote(__content_140302383355024_670, '\x00', '&#0;', None, False)
                    __token = 744
                    __content_140302383355024_742 = _lookup_attr(getitem('industry'), 'get_property_declaration')('prod_increase_msg')
                    __content_140302383355024_742 = __quote(__content_140302383355024_742, '\x00', '&#0;', None, False)
                    __token = 822
                    __content_140302383355024_820 = _lookup_attr(getitem('industry'), 'get_property_declaration')('prod_decrease_msg')
                    __content_140302383355024_820 = __quote(__content_140302383355024_820, '\x00', '&#0;', None, False)
                    __token = 900
                    __content_140302383355024_898 = _lookup_attr(getitem('industry'), 'get_property_declaration')('new_ind_msg')
                    __content_140302383355024_898 = __quote(__content_140302383355024_898, '\x00', '&#0;', None, False)
                    __token = 972
                    __content_140302383355024_970 = _lookup_attr(getitem('industry'), 'get_property_declaration')('min_cargo_distr')
                    __content_140302383355024_970 = __quote(__content_140302383355024_970, '\x00', '&#0;', None, False)
                    __token = 1048
                    __content_140302383355024_1046 = _lookup_attr(getitem('industry'), 'get_property_declaration')('spec_flags')
                    __content_140302383355024_1046 = __quote(__content_140302383355024_1046, '\x00', '&#0;', None, False)
                    __token = 1119
                    __content_140302383355024_1117 = _lookup_attr(getitem('industry'), 'get_industry_layouts_as_property')()
                    __content_140302383355024_1117 = __quote(__content_140302383355024_1117, '\x00', '&#0;', None, False)
                    __content_140302383355024 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n                    ', (__content_140302383355024 if (__content_140302383355024 is not None) else ''), '\n                    ', (__content_140302383355024_460 if (__content_140302383355024_460 is not None) else ''), '\n                    ', (__content_140302383355024_529 if (__content_140302383355024_529 is not None) else ''), '\n                    ', (__content_140302383355024_600 if (__content_140302383355024_600 is not None) else ''), '\n                    ', (__content_140302383355024_670 if (__content_140302383355024_670 is not None) else ''), '\n                    ', (__content_140302383355024_742 if (__content_140302383355024_742 is not None) else ''), '\n                    ', (__content_140302383355024_820 if (__content_140302383355024_820 is not None) else ''), '\n                    ', (__content_140302383355024_898 if (__content_140302383355024_898 is not None) else ''), '\n                    ', (__content_140302383355024_970 if (__content_140302383355024_970 is not None) else ''), '\n                    ', (__content_140302383355024_1046 if (__content_140302383355024_1046 is not None) else ''), '\n                    ', (__content_140302383355024_1117 if (__content_140302383355024_1117 is not None) else ''), "\n                    conflicting_ind_types: []; // set this prop empty, FIRS has it's own better checks for this\n                    random_sound_effects: []; // set this empty to avoid spurious default industry sounds (as of May 2017 FIRS does not yet use sound effects)\n                    ", ))
                    if (__content_140302383355024 is None):
                        pass
                    else:
                        if (__content_140302383355024 is False):
                            __content_140302383355024 = None
                        else:
                            __tt = type(__content_140302383355024)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_140302383355024 = str(__content_140302383355024)
                            else:
                                if (__tt is bytes):
                                    __content_140302383355024 = decode(__content_140302383355024)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_140302383355024 = __content_140302383355024.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_140302383355024)
                                            __content_140302383355024 = (str(__content_140302383355024) if (__content_140302383355024 is __converted) else __converted)
                                        else:
                                            __content_140302383355024 = __content_140302383355024()
                    if (__content_140302383355024 is not None):
                        __append(__content_140302383355024)

                    # <Interpolation value=<Substitution "\n                    ${industry.get_property_declaration('name', economy)}\n                    ${industry.get_property_declaration('prod_multiplier', economy)}\n                    ${industry.get_property_declaration('input_multiplier_1', economy)}\n                    ${industry.get_property_declaration('input_multiplier_2', economy)}\n                    ${industry.get_property_declaration('input_multiplier_3', economy)}\n                    ${industry.get_property_declaration('prob_random', economy)}\n                    ${industry.get_property_declaration('prob_in_game', economy)}\n                    ${industry.get_property_declaration('prospect_chance', economy)}\n                    ${industry.get_property_declaration('fund_cost_multiplier', economy)}\n                    ${industry.get_property_declaration('remove_cost_multiplier', economy)}\n                    ${industry.get_property_declaration('remove_cost_multiplier', economy)}\n                    " (20:102)> braces_required=True translation=False at 7f9ab07ea160> -> __content_140302383355024
                    __token = 1558
                    __token = 1560
                    __content_140302383355024 = _lookup_attr(getitem('industry'), 'get_property_declaration')('name', getitem('economy'))
                    __content_140302383355024 = __quote(__content_140302383355024, '\x00', '&#0;', None, False)
                    __token = 1634
                    __content_140302383355024_1632 = _lookup_attr(getitem('industry'), 'get_property_declaration')('prod_multiplier', getitem('economy'))
                    __content_140302383355024_1632 = __quote(__content_140302383355024_1632, '\x00', '&#0;', None, False)
                    __token = 1719
                    __content_140302383355024_1717 = _lookup_attr(getitem('industry'), 'get_property_declaration')('input_multiplier_1', getitem('economy'))
                    __content_140302383355024_1717 = __quote(__content_140302383355024_1717, '\x00', '&#0;', None, False)
                    __token = 1807
                    __content_140302383355024_1805 = _lookup_attr(getitem('industry'), 'get_property_declaration')('input_multiplier_2', getitem('economy'))
                    __content_140302383355024_1805 = __quote(__content_140302383355024_1805, '\x00', '&#0;', None, False)
                    __token = 1895
                    __content_140302383355024_1893 = _lookup_attr(getitem('industry'), 'get_property_declaration')('input_multiplier_3', getitem('economy'))
                    __content_140302383355024_1893 = __quote(__content_140302383355024_1893, '\x00', '&#0;', None, False)
                    __token = 1983
                    __content_140302383355024_1981 = _lookup_attr(getitem('industry'), 'get_property_declaration')('prob_random', getitem('economy'))
                    __content_140302383355024_1981 = __quote(__content_140302383355024_1981, '\x00', '&#0;', None, False)
                    __token = 2064
                    __content_140302383355024_2062 = _lookup_attr(getitem('industry'), 'get_property_declaration')('prob_in_game', getitem('economy'))
                    __content_140302383355024_2062 = __quote(__content_140302383355024_2062, '\x00', '&#0;', None, False)
                    __token = 2146
                    __content_140302383355024_2144 = _lookup_attr(getitem('industry'), 'get_property_declaration')('prospect_chance', getitem('economy'))
                    __content_140302383355024_2144 = __quote(__content_140302383355024_2144, '\x00', '&#0;', None, False)
                    __token = 2231
                    __content_140302383355024_2229 = _lookup_attr(getitem('industry'), 'get_property_declaration')('fund_cost_multiplier', getitem('economy'))
                    __content_140302383355024_2229 = __quote(__content_140302383355024_2229, '\x00', '&#0;', None, False)
                    __token = 2321
                    __content_140302383355024_2319 = _lookup_attr(getitem('industry'), 'get_property_declaration')('remove_cost_multiplier', getitem('economy'))
                    __content_140302383355024_2319 = __quote(__content_140302383355024_2319, '\x00', '&#0;', None, False)
                    __token = 2413
                    __content_140302383355024_2411 = _lookup_attr(getitem('industry'), 'get_property_declaration')('remove_cost_multiplier', getitem('economy'))
                    __content_140302383355024_2411 = __quote(__content_140302383355024_2411, '\x00', '&#0;', None, False)
                    __content_140302383355024 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n                    ', (__content_140302383355024 if (__content_140302383355024 is not None) else ''), '\n                    ', (__content_140302383355024_1632 if (__content_140302383355024_1632 is not None) else ''), '\n                    ', (__content_140302383355024_1717 if (__content_140302383355024_1717 is not None) else ''), '\n                    ', (__content_140302383355024_1805 if (__content_140302383355024_1805 is not None) else ''), '\n                    ', (__content_140302383355024_1893 if (__content_140302383355024_1893 is not None) else ''), '\n                    ', (__content_140302383355024_1981 if (__content_140302383355024_1981 is not None) else ''), '\n                    ', (__content_140302383355024_2062 if (__content_140302383355024_2062 is not None) else ''), '\n                    ', (__content_140302383355024_2144 if (__content_140302383355024_2144 is not None) else ''), '\n                    ', (__content_140302383355024_2229 if (__content_140302383355024_2229 is not None) else ''), '\n                    ', (__content_140302383355024_2319 if (__content_140302383355024_2319 is not None) else ''), '\n                    ', (__content_140302383355024_2411 if (__content_140302383355024_2411 is not None) else ''), '\n                    ', ))
                    if (__content_140302383355024 is None):
                        pass
                    else:
                        if (__content_140302383355024 is False):
                            __content_140302383355024 = None
                        else:
                            __tt = type(__content_140302383355024)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_140302383355024 = str(__content_140302383355024)
                            else:
                                if (__tt is bytes):
                                    __content_140302383355024 = decode(__content_140302383355024)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_140302383355024 = __content_140302383355024.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_140302383355024)
                                            __content_140302383355024 = (str(__content_140302383355024) if (__content_140302383355024 is __converted) else __converted)
                                        else:
                                            __content_140302383355024 = __content_140302383355024()
                    if (__content_140302383355024 is not None):
                        __append(__content_140302383355024)

                    # <Interpolation value=<Substitution '\n                    ${industry.get_accept_cargo_types_declaration(economy)}\n                    ${industry.get_prod_cargo_types_declaration(economy)}\n                    ${industry.get_nearby_station_name_declaration()}\n                }\n            }\n        }\n    ' (32:46)> braces_required=True translation=False at 7f9ab07ea940> -> __content_140302383355024
                    __token = 2550
                    __token = 2552
                    __content_140302383355024 = _lookup_attr(getitem('industry'), 'get_accept_cargo_types_declaration')(getitem('economy'))
                    __content_140302383355024 = __quote(__content_140302383355024, '\x00', '&#0;', None, False)
                    __token = 2628
                    __content_140302383355024_2626 = _lookup_attr(getitem('industry'), 'get_prod_cargo_types_declaration')(getitem('economy'))
                    __content_140302383355024_2626 = __quote(__content_140302383355024_2626, '\x00', '&#0;', None, False)
                    __token = 2702
                    __content_140302383355024_2700 = _lookup_attr(getitem('industry'), 'get_nearby_station_name_declaration')()
                    __content_140302383355024_2700 = __quote(__content_140302383355024_2700, '\x00', '&#0;', None, False)
                    __content_140302383355024 = ('%s%s%s%s%s%s%s' % ('\n                    ', (__content_140302383355024 if (__content_140302383355024 is not None) else ''), '\n                    ', (__content_140302383355024_2626 if (__content_140302383355024_2626 is not None) else ''), '\n                    ', (__content_140302383355024_2700 if (__content_140302383355024_2700 is not None) else ''), '\n                }\n            }\n        }\n    ', ))
                    if (__content_140302383355024 is None):
                        pass
                    else:
                        if (__content_140302383355024 is False):
                            __content_140302383355024 = None
                        else:
                            __tt = type(__content_140302383355024)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_140302383355024 = str(__content_140302383355024)
                            else:
                                if (__tt is bytes):
                                    __content_140302383355024 = decode(__content_140302383355024)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_140302383355024 = __content_140302383355024.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_140302383355024)
                                            __content_140302383355024 = (str(__content_140302383355024) if (__content_140302383355024 is __converted) else __converted)
                                        else:
                                            __content_140302383355024 = __content_140302383355024()
                    if (__content_140302383355024 is not None):
                        __append(__content_140302383355024)
                __append('\n')
                ____index_140302362783248 -= 1
                if (____index_140302362783248 > 0):
                    __append('')
            if (__backup_economy_140302362814952 is __marker):
                del econtext['economy']
            else:
                econtext['economy'] = __backup_economy_140302362814952
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }