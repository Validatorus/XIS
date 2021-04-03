# -*- coding: utf-8 -*-
__filename = '/home/jake/GRF/firs-3.0.10-source/bundle_dir/src/src/templates/industry_primary_no_supplies.pynml'
__tokens = {242: ('load: spritesets.pynml', 5, 30), 242: ('load: spritesets.pynml', 5, 30), 300: ('load: spritelayouts.pynml', 7, 30), 300: ('load: spritelayouts.pynml', 7, 30), 361: ('load: graphics_switches.pynml', 9, 30), 361: ('load: graphics_switches.pynml', 9, 30), 438: ('load: location_check_macros_tile.pynml', 11, 42), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 594: ('load: animation_macros.pynml', 14, 38), 654: ("animation_macros.macros['tile_animation']", 15, 30), 654: ("animation_macros.macros['tile_animation']", 15, 30), 731: ('load: properties_tile.pynml', 17, 30), 731: ('load: properties_tile.pynml', 17, 30), 933: ('load: layouts.pynml', 24, 30), 933: ('load: layouts.pynml', 24, 30), 988: ('load: availability.pynml', 26, 30), 988: ('load: availability.pynml', 26, 30), 1064: ('load: location_check_macros_industry.pynml', 28, 46), 1138: ("location_checks_industry.macros['render_tree']", 29, 30), 1138: ("location_checks_industry.macros['render_tree']", 29, 30), 1220: ('load: properties_industry.pynml', 31, 30), 1220: ('load: properties_industry.pynml', 31, 30), 1406: ('item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n\tgraphics {\n\t\tconstruction_probability:${industry.id}_check_availability;\n        build_prod_change:       randomise_primary_production_on_build;\n\t\tlocation_check:          ${industry.id}_check_location;\n\t\tmonthly_prod_change:     return CB_RESULT_IND_PROD_NO_CHANGE;\n\t\trandom_prod_change:      return CB_RESULT_IND_PROD_NO_CHANGE;\n//\t\textra_text_industry:     // no extra text. No production increase by means of FMSP\n\t\tcolour:                  switch_colour;\n\t}\n}', 35, 0), 1430: ('industry.id', 35, 24), 1446: ('industry.numeric_id', 35, 40), 1511: ('industry.id', 37, 29), 1645: ('industry.id', 39, 29)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

_static_140183230129656 = 'load: properties_industry.pynml'
_static_140183229122040 = "location_checks_industry.macros['render_tree']"
_static_140183229122208 = 'load: availability.pynml'
_static_140183229939048 = 'load: layouts.pynml'
_static_140183229938880 = 'load: properties_tile.pynml'
_static_140183229938152 = "animation_macros.macros['tile_animation']"
_static_140183229443208 = "location_checks_tile.macros['render_tree']"
_static_140183229442816 = 'load: graphics_switches.pynml'
_static_140183228906800 = 'load: spritelayouts.pynml'
_static_140183229938824 = 'load: spritesets.pynml'

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
            __append('/* ******************************************************************\n * Definition of the industry tile, its callbacks, and graphics chain\n * ******************************************************************/\n\n')
            __backup_macroname_140183229069704 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7ef39fbc88> name=None at 7f7ef39fbba8> -> __value
            __value = _static_140183229938824
            econtext['macroname'] = __value

            # <Value 'load: spritesets.pynml' (5:30)> -> __macro
            __token = 242
            __macro = ' spritesets.pynml'
            __macro = __loader(__macro)
            __token = 242
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140183229069704 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140183229069704
            __append('\n\n')
            __backup_macroname_140183228750088 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7ef38ffd30> name=None at 7f7ef38ff6d8> -> __value
            __value = _static_140183228906800
            econtext['macroname'] = __value

            # <Value 'load: spritelayouts.pynml' (7:30)> -> __macro
            __token = 300
            __macro = ' spritelayouts.pynml'
            __macro = __loader(__macro)
            __token = 300
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140183228750088 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140183228750088
            __append('\n\n')
            __backup_macroname_140183228751176 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7ef3982b00> name=None at 7f7ef3982e10> -> __value
            __value = _static_140183229442816
            econtext['macroname'] = __value

            # <Value 'load: graphics_switches.pynml' (9:30)> -> __macro
            __token = 361
            __macro = ' graphics_switches.pynml'
            __macro = __loader(__macro)
            __token = 361
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140183228751176 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140183228751176
            __append('\n\n')
            __backup_location_checks_tile_140183230372776 = get('location_checks_tile', __marker)

            # <Value 'load: location_check_macros_tile.pynml' (11:42)> -> __value
            __token = 438
            __value = ' location_check_macros_tile.pynml'
            __value = __loader(__value)
            econtext['location_checks_tile'] = __value
            __backup_macroname_140183228747848 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7ef3982c88> name=None at 7f7ef3982828> -> __value
            __value = _static_140183229443208
            econtext['macroname'] = __value

            # <Value "location_checks_tile.macros['render_tree']" (12:30)> -> __macro
            __token = 508
            __macro = _lookup_attr(getitem('location_checks_tile'), 'macros')['render_tree']
            __token = 508
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140183228747848 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140183228747848
            if (__backup_location_checks_tile_140183230372776 is __marker):
                del econtext['location_checks_tile']
            else:
                econtext['location_checks_tile'] = __backup_location_checks_tile_140183230372776
            __append('\n\n')
            __backup_animation_macros_140183229163336 = get('animation_macros', __marker)

            # <Value 'load: animation_macros.pynml' (14:38)> -> __value
            __token = 594
            __value = ' animation_macros.pynml'
            __value = __loader(__value)
            econtext['animation_macros'] = __value
            __backup_macroname_140183229706952 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7ef39fb9e8> name=None at 7f7ef39fb0f0> -> __value
            __value = _static_140183229938152
            econtext['macroname'] = __value

            # <Value "animation_macros.macros['tile_animation']" (15:30)> -> __macro
            __token = 654
            __macro = _lookup_attr(getitem('animation_macros'), 'macros')['tile_animation']
            __token = 654
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140183229706952 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140183229706952
            if (__backup_animation_macros_140183229163336 is __marker):
                del econtext['animation_macros']
            else:
                econtext['animation_macros'] = __backup_animation_macros_140183229163336
            __append('\n\n')
            __backup_macroname_140183229194376 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7ef39fbcc0> name=None at 7f7ef39fb940> -> __value
            __value = _static_140183229938880
            econtext['macroname'] = __value

            # <Value 'load: properties_tile.pynml' (17:30)> -> __macro
            __token = 731
            __macro = ' properties_tile.pynml'
            __macro = __loader(__macro)
            __token = 731
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140183229194376 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140183229194376
            __append('\n\n\n/* *************************************************\n * Definition of the industry\n * *************************************************/\n\n')
            __backup_macroname_140183229535880 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7ef39fbd68> name=None at 7f7ef39fbe80> -> __value
            __value = _static_140183229939048
            econtext['macroname'] = __value

            # <Value 'load: layouts.pynml' (24:30)> -> __macro
            __token = 933
            __macro = ' layouts.pynml'
            __macro = __loader(__macro)
            __token = 933
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140183229535880 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140183229535880
            __append('\n\n')
            __backup_macroname_140183229197064 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7ef39346a0> name=None at 7f7ef39343c8> -> __value
            __value = _static_140183229122208
            econtext['macroname'] = __value

            # <Value 'load: availability.pynml' (26:30)> -> __macro
            __token = 988
            __macro = ' availability.pynml'
            __macro = __loader(__macro)
            __token = 988
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140183229197064 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140183229197064
            __append('\n\n')
            __backup_location_checks_industry_140183230373728 = get('location_checks_industry', __marker)

            # <Value 'load: location_check_macros_industry.pynml' (28:46)> -> __value
            __token = 1064
            __value = ' location_check_macros_industry.pynml'
            __value = __loader(__value)
            econtext['location_checks_industry'] = __value
            __backup_macroname_140183231106760 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7ef39345f8> name=None at 7f7ef3934f98> -> __value
            __value = _static_140183229122040
            econtext['macroname'] = __value

            # <Value "location_checks_industry.macros['render_tree']" (29:30)> -> __macro
            __token = 1138
            __macro = _lookup_attr(getitem('location_checks_industry'), 'macros')['render_tree']
            __token = 1138
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140183231106760 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140183231106760
            if (__backup_location_checks_industry_140183230373728 is __marker):
                del econtext['location_checks_industry']
            else:
                econtext['location_checks_industry'] = __backup_location_checks_industry_140183230373728
            __append('\n\n')
            __backup_macroname_140183231105224 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x7f7ef3a2a5f8> name=None at 7f7ef3a2a208> -> __value
            __value = _static_140183230129656
            econtext['macroname'] = __value

            # <Value 'load: properties_industry.pynml' (31:30)> -> __macro
            __token = 1220
            __macro = ' properties_industry.pynml'
            __macro = __loader(__macro)
            __token = 1220
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140183231105224 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140183231105224
            __append('\n\n')
            __append('\n')

            # <Interpolation value=<Substitution '\nitem(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n\tgraphics {\n\t\tconstruction_probability:${industry.id}_check_availability;\n        build_prod_change:       randomise_primary_production_on_build;\n\t\tlocation_check:          ${industry.id}_check_location;\n\t\tmonthly_prod_change:     return CB_RESULT_IND_PROD_NO_CHANGE;\n\t\trandom_prod_change:      return CB_RESULT_IND_PROD_NO_CHANGE;\n//\t\textra_text_industry:     // no extra text. No production increase by means of FMSP\n\t\tcolour:                  switch_colour;\n\t}\n}\n' (34:38)> braces_required=True translation=False at 7f7ef3a2ac50> -> __content_140183249773656
            __token = 1406
            __token = 1430
            __content_140183249773656 = _lookup_attr(getitem('industry'), 'id')
            __content_140183249773656 = __quote(__content_140183249773656, '\x00', '&#0;', None, False)
            __token = 1446
            __content_140183249773656_1444 = _lookup_attr(getitem('industry'), 'numeric_id')
            __content_140183249773656_1444 = __quote(__content_140183249773656_1444, '\x00', '&#0;', None, False)
            __token = 1511
            __content_140183249773656_1509 = _lookup_attr(getitem('industry'), 'id')
            __content_140183249773656_1509 = __quote(__content_140183249773656_1509, '\x00', '&#0;', None, False)
            __token = 1645
            __content_140183249773656_1643 = _lookup_attr(getitem('industry'), 'id')
            __content_140183249773656_1643 = __quote(__content_140183249773656_1643, '\x00', '&#0;', None, False)
            __content_140183249773656 = ('%s%s%s%s%s%s%s%s%s' % ('\nitem(FEAT_INDUSTRIES, ', (__content_140183249773656 if (__content_140183249773656 is not None) else ''), ', ', (__content_140183249773656_1444 if (__content_140183249773656_1444 is not None) else ''), ') {\n\tgraphics {\n\t\tconstruction_probability:', (__content_140183249773656_1509 if (__content_140183249773656_1509 is not None) else ''), '_check_availability;\n        build_prod_change:       randomise_primary_production_on_build;\n\t\tlocation_check:          ', (__content_140183249773656_1643 if (__content_140183249773656_1643 is not None) else ''), '_check_location;\n\t\tmonthly_prod_change:     return CB_RESULT_IND_PROD_NO_CHANGE;\n\t\trandom_prod_change:      return CB_RESULT_IND_PROD_NO_CHANGE;\n//\t\textra_text_industry:     // no extra text. No production increase by means of FMSP\n\t\tcolour:                  switch_colour;\n\t}\n}\n', ))
            if (__content_140183249773656 is None):
                pass
            else:
                if (__content_140183249773656 is False):
                    __content_140183249773656 = None
                else:
                    __tt = type(__content_140183249773656)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_140183249773656 = str(__content_140183249773656)
                    else:
                        if (__tt is bytes):
                            __content_140183249773656 = decode(__content_140183249773656)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_140183249773656 = __content_140183249773656.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_140183249773656)
                                    __content_140183249773656 = (str(__content_140183249773656) if (__content_140183249773656 is __converted) else __converted)
                                else:
                                    __content_140183249773656 = __content_140183249773656()
            if (__content_140183249773656 is not None):
                __append(__content_140183249773656)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }