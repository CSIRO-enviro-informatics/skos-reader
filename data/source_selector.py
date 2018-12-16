import _config as conf
from data.source_rva import RVA
from data.source_rdf_file import RDFFile
from data.source_vb import VB


def get_vocabulary(vocab_id):
    source_type = conf.VOCABS[vocab_id].get('source')

    if source_type == conf.VocabSource.FILE:
        v = RDFFile(vocab_id).get_vocabulary()
    elif source_type == conf.VocabSource.RVA:
        v = RVA(vocab_id).get_vocabulary()
    elif source_type == conf.VocabSource.VOCBENCH:
        v = VB(vocab_id).get_vocabulary()
    # TODO: add other sources
    else:
        v = None

    return v


def get_object_class(vocab_id, uri):
    source_type = conf.VOCABS[vocab_id].get('source')

    if source_type == conf.VocabSource.FILE:
        c = RDFFile(vocab_id).get_object_class(uri)
    elif source_type == conf.VocabSource.RVA:
        c = RVA(vocab_id).get_object_class(uri)
    elif source_type == conf.VocabSource.VOCBENCH:
        v = VB(vocab_id).get_object_class()
    else:
        # no other sources for now
        c = None

    return c


def get_concept(vocab_id, uri):
    source_type = conf.VOCABS[vocab_id].get('source')

    if source_type == conf.VocabSource.FILE:
        c = RDFFile(vocab_id).get_concept(uri)
    elif source_type == conf.VocabSource.RVA:
        c = RVA(vocab_id).get_concept(uri)
    elif source_type == conf.VocabSource.VOCBENCH:
        v = VB(vocab_id).get_concept()
    else:
        # no other sources for now
        c = None

    return c


def list_concepts(vocab_id):
    source_type = conf.VOCABS[vocab_id].get('source')

    if source_type == conf.VocabSource.FILE:
        v = RDFFile(vocab_id).list_concepts()
    elif source_type == conf.VocabSource.RVA:
        v = RVA(vocab_id).list_concepts()
    elif source_type == conf.VocabSource.VOCBENCH:
        v = VB(vocab_id).list_concepts()
    # TODO: add other sources
    else:
        v = None

    return v
