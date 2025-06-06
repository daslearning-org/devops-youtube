from litellm import CustomLLM, completion, acompletion
from litellm.types.utils import GenericStreamingChunk, ModelResponse
from typing import Iterator, AsyncIterator

def my_function(question):
    return f"Question: {question}. \nAnswer: Hello from DasLearning.in"

class MyCustomLLM(CustomLLM):
    def completion(self, *args, **kwargs) -> ModelResponse:
        messages = kwargs.get("messages", [])
        #max_tokens = kwargs.get("max_tokens", 1000)
        prompt = messages[-1]["content"] if messages else "hi"
        return completion(
            model="my-llm/xyz",
            mock_response=my_function(question=prompt),
        )

    async def acompletion(self, *args, **kwargs) -> ModelResponse:
        messages = kwargs.get("messages", [])
        #max_tokens = kwargs.get("max_tokens", 1000)
        prompt = messages[-1]["content"] if messages else "hi"
        return await acompletion(
            model="my-llm/xyz",
            mock_response=my_function(question=prompt),
        )
    
    def streaming(self, *args, **kwargs) -> Iterator[GenericStreamingChunk]:
        messages = kwargs.get("messages", [])
        #max_tokens = kwargs.get("max_tokens", 1000)
        prompt = messages[-1]["content"] if messages else "hi"
        generic_streaming_chunk: GenericStreamingChunk = {
            "finish_reason": "stop",
            "index": 0,
            "is_finished": True,
            "text": my_function(question=prompt),
            "tool_use": None,
            "usage": {"completion_tokens": 0, "prompt_tokens": 0, "total_tokens": 0},
        }
        return generic_streaming_chunk # type: ignore

    async def astreaming(self, *args, **kwargs) -> AsyncIterator[GenericStreamingChunk]:
        messages = kwargs.get("messages", [])
        #max_tokens = kwargs.get("max_tokens", 1000)
        prompt = messages[-1]["content"] if messages else "hi"
        generic_streaming_chunk: GenericStreamingChunk = {
            "finish_reason": "stop",
            "index": 0,
            "is_finished": True,
            "text": my_function(question=prompt),
            "tool_use": None,
            "usage": {"completion_tokens": 0, "prompt_tokens": 0, "total_tokens": 0},
        }
        yield generic_streaming_chunk # type: ignore

my_llm = MyCustomLLM()
