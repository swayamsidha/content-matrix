from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "microsoft/phi-3-mini-4k-instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float32,
    device_map="auto"
)

def generate(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    output = model.generate(
        **inputs,
        max_new_tokens=250,
        temperature=0.7
    )
    return tokenizer.decode(output[0], skip_special_tokens=True)
