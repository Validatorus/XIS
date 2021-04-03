# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/his/src/templates/header.pynml'
__tokens = {0: ('grf {\n\tgrfid: "\\JD\\88\\07";\n\tname: string(STR_GRF_NAME);\n\tdesc: string(STR_GRF_DESC);\n\turl: string(STR_GRF_URL);\n\tversion: ${repo_vars.repo_revision};\n\tmin_compatible_version: 5932;\n\tparam 0 {', 1, 0), 124: ('repo_vars.repo_revision', 6, 12), 317: ('economy_selection {\n\t\t\tname: string(STR_PARAM_NAME_ECONOMIES);\n\t\t\tdesc: string(STR_PARAM_DESC_ECONOMIES);\n\t\t\tmin_value: 0;\n\t\t\tmax_value: ${len(economies)-1};\n\t\t\tnames: {', 10, 2), 456: ('len(economies)-1', 14, 16), 531: ('economies', 16, 44), 563: ('${repeat.economy.index}: string(STR_PARAM_VALUE_ECONOMIES_${economy.id});', 17, 20), 565: ('repeat.economy.index', 17, 22), 623: ('economy.id', 17, 80), 1446: ('param 7 {\n\t\tprimary_level1_produced_percent {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL1_BONUS);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_BONUS);\n\t\t\tdef_value: 150;\n\t\t\tmin_value: 100;\n\t\t\tmax_value: 1000;\n\t\t}\n\t}\n\tparam 9 {\n\t\tprimary_level2_produced_percent {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL2_BONUS);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_BONUS);\n\t\t\tdef_value: 300;\n\t\t\tmin_value: 100;\n\t\t\tmax_value: 1000;\n\t\t}\n\t}\n\tparam 6 {\n\t\tprimary_level1_requirement {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL1_REQUIREMENT);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_REQUIREMENT);\n\t\t\tdef_value: ${global_constants.FARM_MINE_SUPPLY_REQUIREMENT};\n\t\t\tmin_value: 1;\n\t\t\tmax_value: 10000;\n\t\t}\n\t}\n\tparam 8 {\n\t\tprimary_level2_requirement {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL2_REQUIREMENT);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_REQUIREMENT);\n\t\t\tdef_value: ${5 * global_constants.FARM_MINE_SUPPLY_REQUIREMENT};\n\t\t\tmin_value: 1;\n\t\t\tmax_value: 10000;\n\t\t}\n\t}\n\tparam 4 {\n\t\tmarine_industry_max_coastal_distance {\n\t\t\tname: string(STR_PARAM_NAME_COAST_DISTANCE_MARINE_INDUSTRY);\n\t\t\tdesc: string(STR_PARAM_DESC_COAST_DISTANCE_MARINE_INDUSTRY);\n\t\t\ttype: int;\n\t\t\tdef_value: 0;\n\t\t\tmin_value: 0;\n\t\t\tmax_value: 255;\n\t\t\tnames: {\n\t\t\t\t0: string(STR_PARAM_VALUE_SECONDARY_NEVER_CLOSE_0);\n\t\t\t};\n\t\t}\n\t}\n}\n\nbasecost {\n\tPR_BUILD_INDUSTRY: 2;       // Industries are more expensive\n\tPR_BUILD_INDUSTRY_RAW : 2;  // Building primary industries is also expensive\n\tPR_CLEAR_INDUSTRY : 2;      // Deleting industries must also be expensive\n}', 52, 1), 2060: ('global_constants.FARM_MINE_SUPPLY_REQUIREMENT', 74, 16), 2330: ('5 * global_constants.FARM_MINE_SUPPLY_REQUIREMENT', 83, 16)}

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

            # <Interpolation value=<Substitution 'grf {\n\tgrfid: "\\JD\\88\\07";\n\tname: string(STR_GRF_NAME);\n\tdesc: string(STR_GRF_DESC);\n\turl: string(STR_GRF_URL);\n\tversion: ${repo_vars.repo_revision};\n\tmin_compatible_version: 5932;\n\tparam 0 {\n\t    ' (1:0)> braces_required=True translation=False at 7fbcbdca37b8> -> __content_140448632960200
            __token = 0
            __token = 124
            __content_140448632960200 = _lookup_attr(getitem('repo_vars'), 'repo_revision')
            __content_140448632960200 = __quote(__content_140448632960200, '\x00', '&#0;', None, False)
            __content_140448632960200 = ('%s%s%s' % ('grf {\n\tgrfid: "\\JD\\88\\07";\n\tname: string(STR_GRF_NAME);\n\tdesc: string(STR_GRF_DESC);\n\turl: string(STR_GRF_URL);\n\tversion: ', (__content_140448632960200 if (__content_140448632960200 is not None) else ''), ';\n\tmin_compatible_version: 5932;\n\tparam 0 {\n\t    ', ))
            if (__content_140448632960200 is None):
                pass
            else:
                if (__content_140448632960200 is False):
                    __content_140448632960200 = None
                else:
                    __tt = type(__content_140448632960200)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140448632960200 = str(__content_140448632960200)
                    else:
                        if (__tt is bytes):
                            __content_140448632960200 = decode(__content_140448632960200)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140448632960200 = __content_140448632960200.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140448632960200)
                                    __content_140448632960200 = (str(__content_140448632960200) if (__content_140448632960200 is __converted) else __converted)
                                else:
                                    __content_140448632960200 = __content_140448632960200()
            if (__content_140448632960200 is not None):
                __append(__content_140448632960200)

            # <Interpolation value=<Substitution '\n\t\teconomy_selection {\n\t\t\tname: string(STR_PARAM_NAME_ECONOMIES);\n\t\t\tdesc: string(STR_PARAM_DESC_ECONOMIES);\n\t\t\tmin_value: 0;\n\t\t\tmax_value: ${len(economies)-1};\n\t\t\tnames: {\n\t\t\t    ' (9:122)> braces_required=True translation=False at 7fbcbdca3898> -> __content_140448632960200
            __token = 317
            __token = 456
            __content_140448632960200 = (len(getitem('economies')) - 1)
            __content_140448632960200 = __quote(__content_140448632960200, '\x00', '&#0;', None, False)
            __content_140448632960200 = ('%s%s%s' % ('\n\t\teconomy_selection {\n\t\t\tname: string(STR_PARAM_NAME_ECONOMIES);\n\t\t\tdesc: string(STR_PARAM_DESC_ECONOMIES);\n\t\t\tmin_value: 0;\n\t\t\tmax_value: ', (__content_140448632960200 if (__content_140448632960200 is not None) else ''), ';\n\t\t\tnames: {\n\t\t\t    ', ))
            if (__content_140448632960200 is None):
                pass
            else:
                if (__content_140448632960200 is False):
                    __content_140448632960200 = None
                else:
                    __tt = type(__content_140448632960200)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140448632960200 = str(__content_140448632960200)
                    else:
                        if (__tt is bytes):
                            __content_140448632960200 = decode(__content_140448632960200)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140448632960200 = __content_140448632960200.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140448632960200)
                                    __content_140448632960200 = (str(__content_140448632960200) if (__content_140448632960200 is __converted) else __converted)
                                else:
                                    __content_140448632960200 = __content_140448632960200()
            if (__content_140448632960200 is not None):
                __append(__content_140448632960200)
            __backup_economy_140448640402432 = get('economy', __marker)

            # <Value 'economies' (16:44)> -> __iterator
            __token = 531
            __iterator = getitem('economies')
            (__iterator, ____index_140448614726232, ) = getitem('repeat')('economy', __iterator)
            econtext['economy'] = None
            for __item in __iterator:
                econtext['economy'] = __item

                # <Interpolation value=<Substitution '\n                    ${repeat.economy.index}: string(STR_PARAM_VALUE_ECONOMIES_${economy.id});\n\t\t\t    ' (16:55)> braces_required=True translation=False at 7fbcbdca3a90> -> __content_140448632960200
                __token = 563
                __token = 565
                __content_140448632960200 = _lookup_attr(_lookup_attr(getitem('repeat'), 'economy'), 'index')
                __content_140448632960200 = __quote(__content_140448632960200, '\x00', '&#0;', None, False)
                __token = 623
                __content_140448632960200_621 = _lookup_attr(getitem('economy'), 'id')
                __content_140448632960200_621 = __quote(__content_140448632960200_621, '\x00', '&#0;', None, False)
                __content_140448632960200 = ('%s%s%s%s%s' % ('\n                    ', (__content_140448632960200 if (__content_140448632960200 is not None) else ''), ': string(STR_PARAM_VALUE_ECONOMIES_', (__content_140448632960200_621 if (__content_140448632960200_621 is not None) else ''), ');\n\t\t\t    ', ))
                if (__content_140448632960200 is None):
                    pass
                else:
                    if (__content_140448632960200 is False):
                        __content_140448632960200 = None
                    else:
                        __tt = type(__content_140448632960200)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140448632960200 = str(__content_140448632960200)
                        else:
                            if (__tt is bytes):
                                __content_140448632960200 = decode(__content_140448632960200)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140448632960200 = __content_140448632960200.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140448632960200)
                                        __content_140448632960200 = (str(__content_140448632960200) if (__content_140448632960200 is __converted) else __converted)
                                    else:
                                        __content_140448632960200 = __content_140448632960200()
                if (__content_140448632960200 is not None):
                    __append(__content_140448632960200)
                ____index_140448614726232 -= 1
                if (____index_140448614726232 > 0):
                    __append('')
            if (__backup_economy_140448640402432 is __marker):
                del econtext['economy']
            else:
                econtext['economy'] = __backup_economy_140448640402432
            __append('\n\t\t\t};\n\t\t}\n\t}\n\tparam 2 {\n\t\t')
            __append('\n\t\t')
            __append('\n\t\tallow_close_secondary {\n\t\t\tname: string(STR_PARAM_NAME_SECONDARY_NEVER_CLOSE);\n\t\t\tdesc: string(STR_PARAM_DESC_SECONDARY_NEVER_CLOSE);\n\t\t\ttype: bool;\n\t\t\tbit: 1;\n\t\t}\n\t\trestrict_open_during_gameplay {\n\t\t\tname: string(STR_PARAM_NAME_NO_OPENINGS);\n\t\t\tdesc: string(STR_PARAM_DESC_NO_OPENINGS);\n\t\t\ttype: bool;\n\t\t\tbit: 2;\n\t\t}\n\t}\n\t')
            __append('\n\t')

            # <Interpolation value=<Substitution '\n\tparam 7 {\n\t\tprimary_level1_produced_percent {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL1_BONUS);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_BONUS);\n\t\t\tdef_value: 150;\n\t\t\tmin_value: 100;\n\t\t\tmax_value: 1000;\n\t\t}\n\t}\n\tparam 9 {\n\t\tprimary_level2_produced_percent {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL2_BONUS);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_BONUS);\n\t\t\tdef_value: 300;\n\t\t\tmin_value: 100;\n\t\t\tmax_value: 1000;\n\t\t}\n\t}\n\tparam 6 {\n\t\tprimary_level1_requirement {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL1_REQUIREMENT);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_REQUIREMENT);\n\t\t\tdef_value: ${global_constants.FARM_MINE_SUPPLY_REQUIREMENT};\n\t\t\tmin_value: 1;\n\t\t\tmax_value: 10000;\n\t\t}\n\t}\n\tparam 8 {\n\t\tprimary_level2_requirement {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL2_REQUIREMENT);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_REQUIREMENT);\n\t\t\tdef_value: ${5 * global_constants.FARM_MINE_SUPPLY_REQUIREMENT};\n\t\t\tmin_value: 1;\n\t\t\tmax_value: 10000;\n\t\t}\n\t}\n\tparam 4 {\n\t\tmarine_industry_max_coastal_distance {\n\t\t\tname: string(STR_PARAM_NAME_COAST_DISTANCE_MARINE_INDUSTRY);\n\t\t\tdesc: string(STR_PARAM_DESC_COAST_DISTANCE_MARINE_INDUSTRY);\n\t\t\ttype: int;\n\t\t\tdef_value: 0;\n\t\t\tmin_value: 0;\n\t\t\tmax_value: 255;\n\t\t\tnames: {\n\t\t\t\t0: string(STR_PARAM_VALUE_SECONDARY_NEVER_CLOSE_0);\n\t\t\t};\n\t\t}\n\t}\n}\n\nbasecost {\n\tPR_BUILD_INDUSTRY: 2;       // Industries are more expensive\n\tPR_BUILD_INDUSTRY_RAW : 2;  // Building primary industries is also expensive\n\tPR_CLEAR_INDUSTRY : 2;      // Deleting industries must also be expensive\n}\n\n' (51:6)> braces_required=True translation=False at 7fbcbdca3b00> -> __content_140448632960200
            __token = 1446
            __token = 2060
            __content_140448632960200 = _lookup_attr(getitem('global_constants'), 'FARM_MINE_SUPPLY_REQUIREMENT')
            __content_140448632960200 = __quote(__content_140448632960200, '\x00', '&#0;', None, False)
            __token = 2330
            __content_140448632960200_2328 = (5 * _lookup_attr(getitem('global_constants'), 'FARM_MINE_SUPPLY_REQUIREMENT'))
            __content_140448632960200_2328 = __quote(__content_140448632960200_2328, '\x00', '&#0;', None, False)
            __content_140448632960200 = ('%s%s%s%s%s' % ('\n\tparam 7 {\n\t\tprimary_level1_produced_percent {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL1_BONUS);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_BONUS);\n\t\t\tdef_value: 150;\n\t\t\tmin_value: 100;\n\t\t\tmax_value: 1000;\n\t\t}\n\t}\n\tparam 9 {\n\t\tprimary_level2_produced_percent {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL2_BONUS);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_BONUS);\n\t\t\tdef_value: 300;\n\t\t\tmin_value: 100;\n\t\t\tmax_value: 1000;\n\t\t}\n\t}\n\tparam 6 {\n\t\tprimary_level1_requirement {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL1_REQUIREMENT);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_REQUIREMENT);\n\t\t\tdef_value: ', (__content_140448632960200 if (__content_140448632960200 is not None) else ''), ';\n\t\t\tmin_value: 1;\n\t\t\tmax_value: 10000;\n\t\t}\n\t}\n\tparam 8 {\n\t\tprimary_level2_requirement {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL2_REQUIREMENT);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_REQUIREMENT);\n\t\t\tdef_value: ', (__content_140448632960200_2328 if (__content_140448632960200_2328 is not None) else ''), ';\n\t\t\tmin_value: 1;\n\t\t\tmax_value: 10000;\n\t\t}\n\t}\n\tparam 4 {\n\t\tmarine_industry_max_coastal_distance {\n\t\t\tname: string(STR_PARAM_NAME_COAST_DISTANCE_MARINE_INDUSTRY);\n\t\t\tdesc: string(STR_PARAM_DESC_COAST_DISTANCE_MARINE_INDUSTRY);\n\t\t\ttype: int;\n\t\t\tdef_value: 0;\n\t\t\tmin_value: 0;\n\t\t\tmax_value: 255;\n\t\t\tnames: {\n\t\t\t\t0: string(STR_PARAM_VALUE_SECONDARY_NEVER_CLOSE_0);\n\t\t\t};\n\t\t}\n\t}\n}\n\nbasecost {\n\tPR_BUILD_INDUSTRY: 2;       // Industries are more expensive\n\tPR_BUILD_INDUSTRY_RAW : 2;  // Building primary industries is also expensive\n\tPR_CLEAR_INDUSTRY : 2;      // Deleting industries must also be expensive\n}\n\n', ))
            if (__content_140448632960200 is None):
                pass
            else:
                if (__content_140448632960200 is False):
                    __content_140448632960200 = None
                else:
                    __tt = type(__content_140448632960200)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140448632960200 = str(__content_140448632960200)
                    else:
                        if (__tt is bytes):
                            __content_140448632960200 = decode(__content_140448632960200)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140448632960200 = __content_140448632960200.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140448632960200)
                                    __content_140448632960200 = (str(__content_140448632960200) if (__content_140448632960200 is __converted) else __converted)
                                else:
                                    __content_140448632960200 = __content_140448632960200()
            if (__content_140448632960200 is not None):
                __append(__content_140448632960200)
            __append('\nif (param[6] == 0) { param[6] = 100; }\nif (param[7] == 0) { param[7] = 100; }\nif (param[8] == 0) { param[8] = 400; }\nif (param[9] == 0) { param[9] = 300; }\n\n')
            __append('\ndisable_item(FEAT_INDUSTRIES, 0, 36);\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }