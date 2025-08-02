from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

model_path = "app/model/trained_model"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)
