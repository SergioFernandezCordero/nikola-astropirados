# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1471276965.9174452
_enable_loop = True
_template_filename = '/home/sergio/Programas/python-venv/local/lib/python3.5/site-packages/nikola/data/themes/base/templates/post_helper.tmpl'
_template_uri = 'post_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['mathjax_script', 'open_graph_metadata', 'meta_translations', 'html_tags', 'twitter_card_information', 'html_pager']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_mathjax_script(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_katex = context.get('use_katex', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.is_mathjax:
            if use_katex:
                __M_writer('            <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.5.1/katex.min.js"></script>\n            <script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.5.1/contrib/auto-render.min.js"></script>\n            <script>\n                renderMathInElement(document.body);\n            </script>\n')
            else:
                __M_writer('            <script type="text/javascript" src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"> </script>\n')
                if mathjax_config:
                    __M_writer('            ')
                    __M_writer(str(mathjax_config))
                    __M_writer('\n')
                else:
                    __M_writer('            <script type="text/x-mathjax-config">\n            MathJax.Hub.Config({tex2jax: {inlineMath: [[\'$latex \',\'$\'], [\'\\\\(\',\'\\\\)\']]}});\n            </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_open_graph_metadata(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        url_replacer = context.get('url_replacer', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_open_graph:
            __M_writer('    <meta property="og:site_name" content="')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('">\n    <meta property="og:title" content="')
            __M_writer(filters.html_escape(str(post.title()[:70])))
            __M_writer('">\n    <meta property="og:url" content="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
            if post.description():
                __M_writer('    <meta property="og:description" content="')
                __M_writer(filters.html_escape(str(post.description()[:200])))
                __M_writer('">\n')
            else:
                __M_writer('    <meta property="og:description" content="')
                __M_writer(filters.html_escape(str(post.text(strip_html=True)[:200])))
                __M_writer('">\n')
            if post.previewimage:
                __M_writer('    <meta property="og:image" content="')
                __M_writer(str(url_replacer(permalink, post.previewimage, lang, 'absolute')))
                __M_writer('">\n')
            __M_writer('    <meta property="og:type" content="article">\n')
            if post.date.isoformat():
                __M_writer('    <meta property="article:published_time" content="')
                __M_writer(str(post.formatted_date('webiso')))
                __M_writer('">\n')
            if post.tags:
                for tag in post.tags:
                    __M_writer('           <meta property="article:tag" content="')
                    __M_writer(filters.html_escape(str(tag)))
                    __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_meta_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if len(translations) > 1:
            for langname in sorted(translations):
                if langname != lang and ((not post.skip_untranslated) or post.is_translation_available(langname)):
                    __M_writer('                <link rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('" href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        hidden_tags = context.get('hidden_tags', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.tags:
            __M_writer('        <ul itemprop="keywords" class="tags">\n')
            for tag in post.tags:
                if tag not in hidden_tags:
                    __M_writer('            <li><a class="tag p-category" href="')
                    __M_writer(str(_link('tag', tag)))
                    __M_writer('" rel="tag">')
                    __M_writer(filters.html_escape(str(tag)))
                    __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_twitter_card_information(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        twitter_card = context.get('twitter_card', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if twitter_card and twitter_card['use_twitter_cards']:
            __M_writer('    <meta name="twitter:card" content="')
            __M_writer(filters.html_escape(str(twitter_card.get('card', 'summary'))))
            __M_writer('">\n')
            if 'site:id' in twitter_card:
                __M_writer('    <meta name="twitter:site:id" content="')
                __M_writer(str(twitter_card['site:id']))
                __M_writer('">\n')
            elif 'site' in twitter_card:
                __M_writer('    <meta name="twitter:site" content="')
                __M_writer(str(twitter_card['site']))
                __M_writer('">\n')
            if 'creator:id' in twitter_card:
                __M_writer('    <meta name="twitter:creator:id" content="')
                __M_writer(str(twitter_card['creator:id']))
                __M_writer('">\n')
            elif 'creator' in twitter_card:
                __M_writer('    <meta name="twitter:creator" content="')
                __M_writer(str(twitter_card['creator']))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_pager(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if post.prev_post or post.next_post:
            __M_writer('        <ul class="pager hidden-print">\n')
            if post.prev_post:
                __M_writer('            <li class="previous">\n                <a href="')
                __M_writer(str(post.prev_post.permalink()))
                __M_writer('" rel="prev" title="')
                __M_writer(filters.html_escape(str(post.prev_post.title())))
                __M_writer('">')
                __M_writer(str(messages("Previous post")))
                __M_writer('</a>\n            </li>\n')
            if post.next_post:
                __M_writer('            <li class="next">\n                <a href="')
                __M_writer(str(post.next_post.permalink()))
                __M_writer('" rel="next" title="')
                __M_writer(filters.html_escape(str(post.next_post.title())))
                __M_writer('">')
                __M_writer(str(messages("Next post")))
                __M_writer('</a>\n            </li>\n')
            __M_writer('        </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/sergio/Programas/python-venv/local/lib/python3.5/site-packages/nikola/data/themes/base/templates/post_helper.tmpl", "source_encoding": "utf-8", "uri": "post_helper.tmpl", "line_map": {"16": 0, "21": 2, "22": 11, "23": 23, "24": 40, "25": 69, "26": 85, "27": 106, "33": 87, "39": 87, "40": 88, "41": 89, "42": 90, "43": 95, "44": 96, "45": 97, "46": 98, "47": 98, "48": 98, "49": 99, "50": 100, "56": 42, "66": 42, "67": 43, "68": 44, "69": 44, "70": 44, "71": 45, "72": 45, "73": 46, "74": 46, "75": 47, "76": 48, "77": 48, "78": 48, "79": 49, "80": 50, "81": 50, "82": 50, "83": 52, "84": 53, "85": 53, "86": 53, "87": 55, "88": 60, "89": 61, "90": 61, "91": 61, "92": 63, "93": 64, "94": 65, "95": 65, "96": 65, "102": 3, "110": 3, "111": 4, "112": 5, "113": 6, "114": 7, "115": 7, "116": 7, "117": 7, "118": 7, "124": 13, "130": 13, "131": 14, "132": 15, "133": 16, "134": 17, "135": 18, "136": 18, "137": 18, "138": 18, "139": 18, "140": 21, "146": 71, "151": 71, "152": 72, "153": 73, "154": 73, "155": 73, "156": 74, "157": 75, "158": 75, "159": 75, "160": 76, "161": 77, "162": 77, "163": 77, "164": 79, "165": 80, "166": 80, "167": 80, "168": 81, "169": 82, "170": 82, "171": 82, "177": 25, "182": 25, "183": 26, "184": 27, "185": 28, "186": 29, "187": 30, "188": 30, "189": 30, "190": 30, "191": 30, "192": 30, "193": 33, "194": 34, "195": 35, "196": 35, "197": 35, "198": 35, "199": 35, "200": 35, "201": 38, "207": 201}}
__M_END_METADATA
"""