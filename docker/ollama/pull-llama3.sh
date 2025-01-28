#!/bin/bash

# Start Ollama server in the background
ollama serve &

# Wait for Ollama server to start
sleep 5

# Pull Llama 2 model
ollama pull llama2

# Wait for Ollama server to finish
wait $!
