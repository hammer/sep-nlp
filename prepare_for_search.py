from haystack.preprocessor.preprocessor import PreProcessor
from haystack.preprocessor.utils import convert_files_to_dicts

from haystack.document_store import ElasticsearchDocumentStore

PDFS_PATH = ''

# Preprocessing: NB the process() API changed after 0.9.0
all_docs = convert_files_to_dicts(dir_path=PDFS_PATH)
preprocessor = PreProcessor(
    clean_empty_lines=True,
    clean_whitespace=True,
    clean_header_footer=False,
    split_by="word",
    split_length=200,
    split_respect_sentence_boundary=True
)
nested_docs = [preprocessor.process(d) for d in all_docs]
docs = [d for x in nested_docs for d in x]

document_store = ElasticsearchDocumentStore()
document_store.write_documents(docs)
