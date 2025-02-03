import os
from datetime import datetime
from dotenv import load_dotenv
import random
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from google.cloud import aiplatform
import numpy as np
from transformers import AutoTokenizer, AutoModelForCausalLM

load_dotenv()



tokenizer = AutoTokenizer.from_pretrained("deepseek-ai/DeepSeek-R1-Distill-Qwen-7B")
model = AutoModelForCausalLM.from_pretrained("deepseek-ai/DeepSeek-R1-Distill-Qwen-7B")
