from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from huggingface_hub import login
login(token="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")
model_name = "meta-llama/Meta-Llama-3-8B-Instruct"  # You can also use the 70B version

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

llama = pipeline("text-generation", model=model, tokenizer=tokenizer)

prompt = "Explain how a black hole forms in space."

output = llama(prompt, max_new_tokens=200, do_sample=True, temperature=0.7)
print(output[0]["generated_text"])
