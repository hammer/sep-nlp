from haystack.question_generator import QuestionGenerator
from haystack.document_store import ElasticsearchDocumentStore
from haystack.retriever import ElasticsearchRetriever
from haystack.pipeline import RetrieverQuestionGenerationPipeline

question_generator = QuestionGenerator()
retriever = ElasticsearchRetriever(document_store=document_store)
rqg_pipeline = RetrieverQuestionGenerationPipeline(retriever, question_generator)
result = rqg_pipeline.run(query="epistemology")
pprint(result)
