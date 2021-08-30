from haystack.preprocessor.preprocessor import PreProcessor
from haystack.preprocessor.utils import convert_files_to_dicts

PDFS_PATH = ''

# Preprocessing: NB the API changed after 0.9.0
all_docs = convert_files_to_dicts(dir_path=PDFS_PATH)
preprocessor = PreProcessor(
    clean_empty_lines=True,
    clean_whitespace=True,
    clean_header_footer=False,
    split_by="word",
    split_length=100,
    split_respect_sentence_boundary=True
)
nested_docs = [preprocessor.process(d) for d in all_docs]
docs = [d for x in nested_docs for d in x]

print(f"n_files_input: {len(all_docs)}\nn_docs_output: {len(docs)}")
