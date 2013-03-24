# -*- coding: utf-8 -*-
import inspect
import sys
from importlib import import_module
# from django.utils.encoding import smart_unicode
# from django.utils.importlib import import_module

def get_class(classname, default_module=''):
    
    if inspect.isclass(classname):
        return classname
    
    if not isinstance(classname, basestring):
        raise TypeError(u"classname : attendu : chaîne de caractères / fourni : %s." % (classname,))
    
    if classname.find('.') < 0 and len(default_module) > 0:
        classname = '%s.%s' % (default_module, classname)
    
    parts = classname.split('.')
    mod = import_module(".".join(parts[:-1]))
    cls = getattr(mod, parts[-1])
    return cls

def get_class_fullname(kls):
    return '%s.%s' % (kls.__module__, kls.__name__)

def issubclass_strict(kls, parent_kls):
    """Indique si ``kls`` est une classe descendante de ``parent_kls``.
    
    """
    assert inspect.isclass(parent_kls)
    
    return (
        inspect.isclass(kls) and
        issubclass(kls, parent_kls) and
        kls is not parent_kls
    )

def find_subclasses(kls, module=None):
    """Cherche les classes filles de ``kls`` dans le module ``module``.
    
    :returns: Un tableau de tuple ``(nom_de_la_classe, classe)``
    
    """
    kls = get_class(kls)
    if module is None:
        module = inspect.getmodule(kls)
    return inspect.getmembers(module, lambda o: issubclass_strict(o, kls))
